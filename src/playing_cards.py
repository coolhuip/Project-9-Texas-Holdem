"""
Classes related to playing cards.
"""
class Card():
    """
    A `Card` objects represents a single playing card.

    How to Initialize:
    ------------------
    <arg_1> = rank
    1 = Ace
    2 = Two
    3 = Three
    ...
    9 = Nine
    10 = Ten
    11 = Jack
    12 = Queen
    13 = King

    <arg_2> = suit
    s = Spades
    h = Hearts
    d = Diamonds
    c = Clubs
    
    Sample Usage:
    -------------
    >>> c1 = Card(1, 's')
    >>> c1.rank()
    Ace
    >>> c1.suit()
    Spades
    >>> c1.print()
    Ace of Spades
    >>> c2 = Card(12, 'h')
    >>> c2.rank()
    Queen
    >>> c2.suit()
    Hearts
    >>> c2.print()
    Queen of Hearts
    >>> c3 = Card(13, 'c')
    >>> c3.rank()
    King
    >>> c3.suit()
    Clubs
    >>> c3.print()
    King of Clubs
    """
    SUITS = {'c': 'Clubs', 'd': 'Diamonds', 'h': 'Hearts', 's': 'Spades'}
    RANKS = {13: 'King', 12: 'Queen', 11: 'Jack', 10: 'Ten', 9: 'Nine',
             8: 'Eight', 7: 'Seven', 6: 'Six', 5: 'Five', 4: 'Four',
             3: 'Three', 2: 'Two', 1: 'Ace'}
    _str_rank: str
    _rank: int
    _suit: str

    def __init__(self, rank: int, suit: str) -> None:
        """
        Initialize a single playing card.
        """
        self._str_rank = Card.RANKS[rank]
        self._rank = rank
        self._suit = Card.SUITS[suit]
    
    def print(self) -> str:
        """
        Return AND print the card to console.
        """
        print(f'{self._str_rank} of {self._suit}')
    
    def rank(self) -> str:
        """
        Return AND print the suit of this 'Card'.
        """
        print(self._str_rank)
    def suit(self) -> str:
        """
        Return AND print the suit of this 'Card'.
        """
        print(self._suit)


class Deck():
    """
    A bare-bone simulation of a standard 52-card deck.

    When initializing, optionally pass in `jokers=True` to include two jokers:
    one black & one colored, for a total of 54 cards.

    Sample Usage:
    -------------
    >>> deck = Deck(jokers=True)
    >>> deck.size()
    54
    >>> deck = Deck()
    >>> deck.size()
    52
    >>> c1 = deck.draw_card()
    Ace of Spades
    >>> c2 = deck.draw_card()
    Two of Spades
    >>> c3 = deck.draw_card()
    Three of Spades
    """
    SUITS = {'c': 'Clubs', 'd': 'Diamonds', 'h': 'Hearts', 's': 'Spades'}
    RANKS = {13: 'King', 12: 'Queen', 11: 'Jack', 10: 'Ten', 9: 'Nine',
             8: 'Eight', 7: 'Seven', 6: 'Six', 5: 'Five', 4: 'Four',
             3: 'Three', 2: 'Two', 1: 'Ace'}

    _count: int   # number of cards in the deck
    _card_stack: list[Card]


    def __init__(self, jokers: bool=False) -> None:
        """
        Initialize a deck of cards.
        """
        self._count = 54 if jokers else 52
        for suit in Deck.SUITS:
            for rank in Deck.SUITS:
                self._card_stack.append(Card(rank, suit))
                
            

    def size(self) -> int:
        """
        Return the number of cards in the deck.
        """
        return self._count

    def shuffle(self) -> None:
        """
        Shuffle the deck as it currently is.
        """
        pass
    
    def draw_card(self) -> None:
        """
        Draw a card from the top of the deck.
        """
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()