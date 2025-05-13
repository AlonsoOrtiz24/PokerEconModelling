from deck import Deck, Card


class PokerHand:
    """
    Represents a poker hand drawn from a deck of cards.
    Evaluates hand characteristics such as flushes, pairs, straights, etc.
    """

    def __init__(self, deck):
        """
        Initializes a poker hand by dealing 5 cards from the given deck.

        Parameters:
        deck (Deck): An instance of a Deck from which cards are dealt.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Returns the list of cards in the poker hand.

        Returns:
        list: List of Card objects in the hand.
        """
        return self._cards

    def __str__(self):
        """
        Returns a string representation of the poker hand.

        Returns:
        str: String listing the cards in the hand.
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Checks if the hand is a flush (all cards of the same suit).

        Returns:
        bool: True if the hand is a flush, False otherwise.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def number_matches(self):
        """
        Counts the number of times card ranks match (excluding self-comparison).
        For example, a pair contributes 2 matches, trips 6, full house 8.

        Returns:
        int: Total number of rank matches in the hand.
        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Determines if the hand has exactly one pair.

        Returns:
        bool: True if the hand is a single pair, False otherwise.
        """
        return self.number_matches == 2

    @property
    def is_two_pair(self):
        """
        Determines if the hand contains two distinct pairs.

        Returns:
        bool: True if the hand has two pairs, False otherwise.
        """
        return self.number_matches == 4

    @property
    def is_trips(self):
        """
        Determines if the hand contains three cards of the same rank (three-of-a-kind).

        Returns:
        bool: True if the hand has three-of-a-kind, False otherwise.
        """
        return self.number_matches == 6

    @property
    def is_full_house(self):
        """
        Determines if the hand is a full house (three of a kind and a pair).

        Returns:
        bool: True if the hand is a full house, False otherwise.
        """
        return self.number_matches == 8

    @property
    def is_straight(self):
        """
        Checks if the hand is a straight (five cards in sequence, regardless of suit).

        Returns:
        bool: True if the hand is a straight, False otherwise.
        """
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4


# Simulation to estimate probability of getting a straight
count = 0
matches = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_straight:
        matches += 1
    count += 1

print(f"The probability of a straight is {100 * matches / count}%")
