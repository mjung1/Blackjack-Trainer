
class Blackjack:
    def __init__(self):
        """
        stores all the relevant data members for the blackjack object
        store best play chart
        store current card count
        store player bankroll
        stores hands for current round
        """
        self._current_count = 0
        self._player_bankroll = None
        self._all_players = None
        self._hands = []
        self.round()

    def round(self):
        """
        create round method to siimulate a new round of blackjack
        - asks user how many players currently for the round (excluding dealer)
        - iterates through the number of players including the dealer
            - takes in cards for each players hand
            - press c for completed hand
            stores each hand as a list
        """
        players = input("How many players are playing this round? (excluding dealer): ")
        self._all_players = int(players) + 1
        for i in range(self._all_players-1):
            temp_hand = []
            c = 1
            while True:
                card = input("Please input card " + str(c) + " of Player " + str(i+1) + "'s hand. Press 'd' when done: ")
                if card == 'd':
                    break
                c += 1
                temp_hand.append(card)
            self._hands.append(temp_hand)
        dealer_hand = [input("Please input Dealer's hand: ")]
        self._hands.append(dealer_hand)
        self.card_count()
        self.best_play()

    def best_play(self):
        """
        create method for best play recommendation that takes in current hands as parameter and designate which player is you
        identifies your hand and dealer's hands as important
        references best play chart and identifies specific recommendation based on users hand and dealers hand
        prints out recommendation based on chart
        """
        player_hand_num = input("Please enter your player number: ")
        player_hand_index = int(player_hand_num) - 1
        player_hand = self._hands[player_hand_index]
        dealer_hand = int(self._hands[-1][0])
        hand_total = 0
        hit = None
        for card in player_hand:
            hand_total += int(card)
        # code below represents process for determining best play
        # let 10 represent 10, J, Q, K; 11 represent Ace
        # pair splitting
        while hand_total <= 21:
            """
            # SPLITTING PAIRS FUNCTIONALITY
            if player_hand[0] == player_hand[1]:
                if player_hand[0] == '11':
                    print('Split the Pair')
                elif player_hand[0] == '9':
                    if dealer_hand < 7 or dealer_hand == 8 or dealer_hand == 9:
                        print('Split the Pair')
                    else:
                        print("Don't Split the Pair")
                elif player_hand[0] == '8':
                    print('Split the Pair')
                elif player_hand[0] == '7':
                    if dealer_hand < 8:
                        print('Split the Pair')
                    else:
                        print("Don't Split the Pair")
                elif player_hand[0] == '6':
                    if 3 <= dealer_hand <= 6:
                        print('Split the Pair')
                    else:
                        print("Don't Split the Pair")
                elif player_hand[0] == '3':
                    if 4 <= dealer_hand <= 7:
                        print('Split the Pair')
                    else:
                        print("Don't Split the Pair")
                elif player_hand[0] == '2':
                    if 4 <= dealer_hand <= 7:
                        print('Split the Pair')
                    else:
                        print("Don't Split the Pair")
                else:
                    print("Don't Split the Pair")
            # soft totals (A as one card)
            """
            if player_hand[0] == 11 or player_hand[1] == 11:
                if hand_total == 21:
                    print("Blackjack!")
                    hit = False
                else:
                    if hand_total == 20:
                        print("Stand")
                        hit = False
                    elif hand_total == 19:
                        print("Stand")
                        hit = False
                    elif hand_total == 18:
                        if dealer_hand <= 8:
                            print("Stand")
                            hit = False
                        else:
                            print("Hit")
                            hit = True
                    else:
                        print("Hit")
                        hit = True
            # hard totals
            elif hand_total <= 17:
                if hand_total == 17:
                    print("Stand")
                    hit = False
                elif 13 <= hand_total <= 16:
                    if dealer_hand <= 6:
                        print("Stand")
                        hit = False
                    else:
                        print("Hit")
                        hit = True
                elif hand_total == 12:
                    if 4 <= dealer_hand <= 6:
                        print("Stand")
                        hit = False
                    else:
                        "Hit"
                        hit = True
                elif hand_total == 11:
                    print("Double Down")
                    hit = True
                elif hand_total == 10:
                    if dealer_hand <= 9:
                        print('Double Down')
                        hit = True
                    else:
                        print('Hit')
                        hit = True
                elif hand_total == 9:
                    if 3 <= dealer_hand <= 6:
                        print("Double Down")
                        hit = True
                    else:
                        print('Hit')
                        hit = True
                elif hand_total <= 8:
                    print('Hit')
                    hit = True
            else:
                if hand_total >= 18:
                    print('Stand')
                    hit = False
            if hit == True:
                card_to_add = input("What's the new card: ")
                player_hand.append(card_to_add)
                hand_total += int(player_hand[-1])
                if hand_total > 21:
                    for card in range(len(player_hand)):
                        if int(player_hand[card]) == 11:
                            player_hand[card] = 1
                    hand_total = 0
                    for card in player_hand:
                        hand_total += int(card)
                        break
            else:
                break
            if hand_total > 21:
                print('Bust')

    def card_count(self):
        """
        create method for card counting tutor that takes in current hands as parameters
        using hi-lo card system
        for i in hands:
            if cards in between range 2 and 6,
                add 1 to count:
            elif cards in between range 7 and 9,
                count remains same
            else:
                subtract 1 from count
        print count info
        prompt user if they would like to play a new round
        """
        for hand in self._hands:
            for card in hand:
                if int(card) <= 6:
                    self._current_count += 1
                elif 7 <= int(card) <= 9:
                    continue
                else:
                    self._current_count -= 1
        print('The current count is ' + str(self._current_count))


def main():
    g = Blackjack()

if __name__ == '__main__':
    main()




