<h1>handsolitaire</h1>
<h2>The game</h2>
Hand solitaire is a simple card game where the player flips cards from the back of a standard 52-card deck comparing the
top card with the 4th card behind it.  If the top card and 4th card have the same suit, the player "drops" the middle 
two cards (i.e. the 2nd and 3rd cards).  If the top card and 4th card have the same number, the player "drops" all four
cards (i.e. the top, 2nd, 3rd, and 4th cards). The game is won if the player "drops" all 52 cards.  

<b>Example</b>
```
| K♦|
| K♦|  | 5♣|
| K♦|  | 5♣|  |10♦|
| K♦|  | 5♣|  |10♦|  | 9♥|
| K♦|  | 5♣|  |10♦|  | 9♥|  | Q♦|
| K♦|  | 5♣|  |10♦|  | 9♥|  | Q♦|  | A♦|  # Matching suits (diamands) -> Drop middle two cards 
| K♦|  | 5♣|  |10♦|  | A♦|                # Matching suits (diamonds) -> Drop middle two cards
| K♦|  | A♦|
| K♦|  | A♦|  |10♣|
| K♦|  | A♦|  |10♣|  | 2♠|
| K♦|  | A♦|  |10♣|  | 2♠| | A♠|          # Matching numbers (Aces) -> Drop all four cards
| K♦|
... (continue until all cards have been flipped) 
```

This is a game of luck since all the player does is following the simple rules.  The order of the cards in the deck
determines whether the player will win.  

<h2>A story</h2>

My dad taught me this game when I was 10 (or so).  At the time, after playing the hand solitaire for nearly 40 years, he
had never won once.

I won on my first try.

My dad told me to never play again. To go out on top.  But alas, it's too easy of a game to play when you're sitting on
the couch, or in an airport, or in between hands of another card game.  And so I've played again and again, dropping my
winning percentage from 100% down to a fraction of a percent.  And so I wondered, how lucky was I to actually win on my
first try?

My undergrad probability course did not give me this mathematical power. And given there are 52-factorial
ways to order a deck of cards (that's 80658175170943878571660636856403766975289505440883277824000000000000 for those
counting), I knew I wasn't coming up with an exact answer, but I built this package to give it a good estimate. 

I "played" 100 million games of hand solitaire using the `experiment.py` script and am happy to say I've won again! <insert wins>
times to be exact.  But I've also now lost (more than) <insert games lost> times.  From my experiment, it looks like the
probability of winning a game of hand solitaire is around <insert percent here>.  So I was definitely lucky, though it
seems like my dad was also very unlucky for many years. Though I am happy to say that my dad has since won a game of
hand solitaire, and he hasn't played since.