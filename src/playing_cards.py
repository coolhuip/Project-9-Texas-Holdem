from __future__ import annotations
from typing import Optional, Union, Any
import random as rand

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
    SUITS = {'s': 'Spades', 'h': 'Hearts', 'd': 'Diamonds', 'c': 'Clubs'}
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
    A bare-bone simulation of a standard 52-card deck. No jokers in the deck.

    Sample Usage:
    -------------
    >>> deck = Deck()
    >>> deck.size()
    52
    >>> c1 = deck.draw_card()
    >>> c1.print()
    King of Clubs
    >>> c2 = deck.draw_card()
    >>> c2.print()
    Queen of Clubs
    >>> c3 = deck.draw_card()
    >>> c3.print()
    Jack of Clubs

    __Dev Doctest:
    --------------
    >>> deck = Deck()
    >>> deck._DEV_draw_cards(50)
    >>> deck.draw_card().print()
    Two of Spades
    >>> deck.draw_card().print()
    Ace of Spades
    """
    SUITS = ['s', 'h', 'd', 'c']
    RANKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    _size: int   # number of cards in the deck
    _card_stack: list[Card]


    def __init__(self) -> None:
        """
        Initialize a deck of cards.
        """
        self._card_stack = []
        for suit in Deck.SUITS:
            for rank in Deck.RANKS:
                self._card_stack.append(Card(rank, suit))
                
        self._size = len(self._card_stack)

    def size(self) -> int:
        """
        Return the number of cards in the deck.
        """
        return self._size

    def shuffle(self) -> None:
        """
        Shuffle the deck as it currently is.
        """
        rand.shuffle(self._card_stack)
    
    def draw_card(self) -> Optional[Card]:
        """
        Pop & return a card from the top of the deck.

        If there are no cards left in the deck, print an error message.
        """
        if self._size == 0:
            print("DECK ERROR: No more cards left in the deck :(")
        else:
            self._size -= 1
            return self._card_stack.pop()
    
    def _DEV_draw_cards(self, num: int) -> None:
        """
        (FOR DEVELOPER TESTING!)
        Draw <num> number of cards from the top.
        """
        draw_count = 0
        for _ in range(num):
            if self._size != 0:
                self._card_stack.pop()
                self._size -= 1
                draw_count += 1
            else:
                print("Deck Error: No more cards left in the deck.")
                print(f"Total Number of Cards Drawn: {draw_count}")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
