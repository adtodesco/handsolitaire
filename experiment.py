import time

from game import play
from deck import Deck


def print_summary(games_played, games_won):
    win_percentage = games_won * 100 / games_played
    print(f"Games played: {games_played}")
    print(f"Games won: {games_won}")
    print(f"Win percentage: {round(win_percentage, 4)}%")


if __name__ == "__main__":
    num_games = 10000000
    games_played, games_won = 0, 0
    deck = Deck()
    start_time = time.time()
    print(f"Playing {num_games} games of hand solitaire...\n")
    for _ in range(num_games):
        deck.shuffle()
        win = play(deck)
        if win:
            games_won += 1
        games_played += 1
        if games_played % 100000 == 0:
            print(f"Played {games_played} of {num_games} games in {round(time.time() - start_time)} seconds.")
            print_summary(games_played, games_won)
            print()
