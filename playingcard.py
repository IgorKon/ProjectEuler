import enum

class CardName(enum.Enum):
    Unknown = 0
    Two = 1
    Three = 2
    Four = 3
    Five = 4
    Six = 5
    Seven = 6
    Eight = 7
    Nine = 8
    Ten = 9
    Jack = 10
    Queen = 11
    King = 12
    Ace = 13

class CardSuit(enum.Enum):
    Unknown = 0
    Spades = 1
    Clubs = 2
    Hearts = 3
    Diamonds = 4

class Card:
    def __init__(self, str_card_description):
        self.Name = CardName.Unknown
        self.Suit = CardSuit.Unknown
        if len(str_card_description) == 2:
            sname = str_card_description[0]
            ssuit = str_card_description[1]
            if sname == '2':
                self.Name = CardName.Two
            elif sname == '3':
                self.Name = CardName.Three
            elif sname == '4':
                self.Name = CardName.Four
            elif sname == '5':
                self.Name = CardName.Five
            elif sname == '6':
                self.Name = CardName.Six
            elif sname == '7':
                self.Name = CardName.Seven
            elif sname == '8':
                self.Name = CardName.Eight
            elif sname == '9':
                self.Name = CardName.Nine
            elif sname == 'T':
                self.Name = CardName.Ten
            elif sname == 'J':
                self.Name = CardName.Jack
            elif sname == 'Q':
                self.Name = CardName.Queen
            elif sname == 'K':
                self.Name = CardName.King
            elif sname == 'A':
                self.Name = CardName.Ace

            if ssuit == 'S':
                self.Suit = CardSuit.Spades
            elif ssuit == 'C':
                self.Suit = CardSuit.Clubs
            elif ssuit == 'H':
                self.Suit = CardSuit.Hearts
            elif ssuit == 'D':
                self.Suit = CardSuit.Diamonds
