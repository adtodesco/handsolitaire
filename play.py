from game import play
from deck import Deck


if __name__ == "__main__":
    deck = Deck(shuffle=True)
    win = play(deck, print_game=True)
    if win:
        print("Victory!")
    else:
        print("Better luck next time!")
