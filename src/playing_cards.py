"""
Classes related to playing cards.
"""

SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
RANKS = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King']


class Card():
    """
    A `Card` objects represents a single playing card.
    """
    _suit: str
    _rank: int

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
    """
    _count: int   # number of cards in the deck
    __inventory: dict[str, int]   # inventory of cards in the deck


    def __init__(jokers: bool=False) -> None:
        """
        Initialize a deck of cards.
        """
        

    def size() -> int:
        """
        Return the number of cards in the deck.
        """
        pass

    def shuffle() -> None:
        """
        Shuffle the deck as it currently is.
        """
        pass
    
    def draw(location='top') -> None:
        """
        Draw a card from the top of the deck.
        """
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()