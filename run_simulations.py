from random import shuffle, seed

def get_result(tiers, number_of_cards_to_win, n_simulations):
        # create default deck for the simulation
        deck = []
        for tier in tiers.keys():
            deck.extend([tier] * tiers[tier])

        def eval_deck(deck, tiers):
            # initialise card counter to zeros
            cdict = dict([[key, 0] for key in tiers.keys()])
            
            # shuffle deck
            shuffle(deck)
            
            # draw until win
            for card in deck:
                cdict[card] += 1
                if cdict[card] == number_of_cards_to_win:
                    return card
            
            return "Error: None found"

        # run simulations
        results = dict([[key, 0] for key in tiers.keys()])
        seed(33)
        for i in range(n_simulations):
            results[eval_deck(deck.copy(), tiers)] += 1

        # get odds
        result_string = ''
        for key in results.keys():
            try:
                odds = round(n_simulations / results[key], 1)
                result_string += 'Tier {tier!s}: Odds are 1 in {odds!s}.\n'.format(tier=key, odds=odds)
            except ZeroDivisionError:
                if tiers[key] < number_of_cards_to_win:
                    result_string = '\nERROR: Insufficient cards in Tier {tier!s} to win.\n'.format(tier=key)
                else:
                    result_string = '\nERROR: Low likelihood in Tier {tier!s}. Rerun with more simulations.\n'.format(tier=key)
                break

        return result_string