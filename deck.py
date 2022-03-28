from random import randint
from enum import Enum


class Suit(Enum):
    SPADES = 1
    CLUBS = 2
    HEARTS = 3
    DIAMONDS = 4


class Number(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        if self.number == Number.ACE:
            num_str = "A"
        elif self.number == Number.JACK:
            num_str = "J"
        elif self.number == Number.QUEEN:
            num_str = "Q"
        elif self.number == Number.KING:
            num_str = "K"
        else:
            num_str = str(self.number.value)

        if len(num_str) < 2:
            num_str = " " + num_str

        if self.suit == Suit.SPADES:
            suit_str = "♠"
        elif self.suit == Suit.CLUBS:
            suit_str = "♣"
        elif self.suit == Suit.HEARTS:
            suit_str = "♥"
        else:
            suit_str = "♦"

        return f"|{num_str}{suit_str}|"


class Deck:
    def __init__(self, cards=None, shuffle=False):
        if cards:
            self.cards = cards
        else:
            self.cards = [Card(s, n) for s in Suit for n in Number]

        if shuffle:
            self.shuffle()

    def shuffle(self):
        original_cards = self.cards.copy()
        shuffled_cards = list()
        while original_cards:
            index = randint(0, len(original_cards) - 1)
            shuffled_cards.append(original_cards[index])
            del original_cards[index]

        self.cards = shuffled_cards
