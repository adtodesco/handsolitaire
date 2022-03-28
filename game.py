from deck import Deck


def print_hand(hand):
    for card in hand:
        print(card, end="  ")
    print()


def play(deck, print_game=False):
    hand = list()
    for card in deck.cards:
        hand.append(card)
        if print_game:
            print_hand(hand)
        while len(hand) >= 4:
            if hand[-1].suit == hand[-4].suit:
                for _ in range(2):
                    del hand[-2]
            elif hand[-1].number == hand[-4].number:
                for _ in range(4):
                    del hand[-1]
            else:
                break
            if print_game:
                print_hand(hand)

    if len(hand) == 0:
        return True

    return False
