from random import shuffle, seed

if __name__ == '__main__':
    while True:
        tiers = {}
        tier = 0
        n_cards = None
        print(
        '''
#######################################################
# Configure tiers for simulation.                     #
# Press ENTER without any value to stop adding tiers. #
#######################################################\n
        '''
        )
        while n_cards != '' :
            tier += 1
            while True:
                try:
                    n_cards = input('How many cards in Tier {tier!s}?    '.format(tier=tier))
                    if n_cards == '':
                        break
                    n_cards = int(n_cards)
                    assert n_cards > 0
                    break
                except (ValueError, AssertionError):
                    print('\nERROR: Please only enter a positive integer value for number of cards. Please try again, or press ENTER to finish configuring tiers.\n')

            if n_cards == '':
                break
            tiers[str(tier)] = int(n_cards)

        while True:
            try:
                number_of_cards_to_win = int(input('How many cards drawn of one tier are required to win?    '))
                assert number_of_cards_to_win > 0
                break
            except (ValueError, AssertionError):
                print('\nERROR: Please only enter a positive integer value.\n...')

        while True:
            try:
                n_simulations = int(input('How many many simulations (e.g. 100000)?    '))
                assert n_simulations > 0
                break
            except (ValueError, AssertionError):
                print('\nERROR: Please only enter a positive integer value.\n...')


        # create default deck for the simulation, based on the above configuration
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

            print("Error: None found")
            
            return None

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
                    print('\nERROR: Insufficient cards in Tier {tier!s} to win.\n'.format(tier=key))
                else:
                    print('\nERROR: Low likelihood in Tier {tier!s}. Rerun with more simulations.\n'.format(tier=key))
                break
        print(result_string)
        end = input('Press any key to run another simulation, or close the window to exit.')
