import random
class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♠", "♥", "♦"]
    def __init__(self, suit, rank):
        """
        Initializes a card with the specified suit and rank.

        Parameters:
        suit (str): One of the four card suits.
        rank (str): One of the standard card ranks.

        Raises:
        ValueError: If the rank or suit is not valid.
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit")
        self._suit = suit
        self._rank = rank

    def __str__(self):
        """
        Returns a string representation of the card.

        Returns:
        str: The card in the format 'RankSuit', e.g., '10♠'.
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Returns the official string representation of the card.

        Returns:
        str: Same as __str__.
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Compares two cards for equality based on rank.

        Parameters:
        other (Card): Another card to compare with.

        Returns:
        bool: True if the ranks are the same, False otherwise.
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compares two cards to determine if this card is of higher rank.

        Parameters:
        other (Card): Another card to compare with.

        Returns:
        bool: True if this card is higher in rank, False otherwise.
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    @property
    def suit(self):
        """
        Gets the suit of the card.

        Returns:
        str: The suit of the card.
        """
        return self._suit

    @property
    def rank(self):
        """
        Gets the rank of the card.

        Returns:
        str: The rank of the card.
        """
        return self._rank


class Deck:
    """
    Represents a standard deck of 52 playing cards.
    Provides methods to shuffle and deal cards.
    """

    def __init__(self):
        """
        Initializes a new deck of 52 cards (one for each combination of rank and suit).
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        Returns a string representation of the entire deck.

        Returns:
        str: A string list of all cards in the deck.
        """
        return str(self._deck)

    def shuffle(self):
        """
        Shuffles the deck in place using Python's random.shuffle().
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Deals (removes and returns) the top card from the deck.

        Returns:
        Card: The card dealt from the top of the deck.

        Raises:
        IndexError: If the deck is empty.
        """
        return self._deck.pop()


if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())