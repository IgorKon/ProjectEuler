import enum
import playingcard

class Rank(enum.Enum):
    Unknown = 0
    HighCard = 1
    OnePair = 2
    TwoPairs = 3
    ThreeOfaKind = 4
    Straight = 5
    Flush = 6
    FullHouse = 7
    FourOfaKind = 8
    StraightFlush = 9
    RoyalFlush = 10

class HandRank:
    def __init__(self, rank, highCard = playingcard.CardName.Unknown, secondCard = playingcard.CardName.Unknown):
        self.rank = rank
        self.highCard = highCard
        self.secondCard = secondCard

class CardsHand:
    def __init__(self, str_arr):
        self.Cards = list()
        if len(str_arr) == 5:
            for i in range(5):
                c = playingcard.Card(str_arr[i])
                self.Cards.append(c)
            self.Cards.sort(key = lambda card: card.Name.value)
            self.Ranks = self.CalculateRanks()

    def CalculateRanks(self):
        res = list()
        bIs, r = self.IsRoyalFlush()
        if bIs:
            res.append(r)
        else:
            bIs, r = self.IsStraightFlush()
            if bIs:
                res.append(r)
            else:
                bIs, r1, r2 = self.IsFourOfaKind()
                if bIs:
                    res.append(r1)
                    res.append(r2)
                else:
                    bIs, r = self.IsFullHouse()
                    if bIs:
                        res.append(r)
                    else:
                        bIs, r = self.IsStraight()
                        if bIs:
                            res.append(r)
                        else:
                            bIs, ranks = self.IsThreeOfaKind()
                            if bIs:
                                for r in ranks:
                                    res.append(r)
                            else:
                                bIs, r1, r2 = self.IsTwoPairs()
                                if bIs:
                                    res.append(r1)
                                    res.append(r2)
                                else:
                                    bIs, ranks = self.IsOnePair()
                                    if bIs:
                                        for r in ranks:
                                            res.append(r)
                                    else:
                                        res.append(HandRank(Rank.HighCard,  self.Cards[4].Name))
                                        res.append(HandRank(Rank.HighCard,  self.Cards[3].Name))
                                        res.append(HandRank(Rank.HighCard,  self.Cards[2].Name))
                                        res.append(HandRank(Rank.HighCard,  self.Cards[1].Name))
                                        res.append(HandRank(Rank.HighCard,  self.Cards[0].Name))
        return res

    def IsRoyalFlush(self):
        for i in range(1, 5):
            if self.Cards[i].Suit != self.Cards[0].Suit:
                return False, HandRank(Rank.Unknown)
        if self.Cards[0].Name.value == playingcard.CardName.Jack.value:
            return True, HandRank(Rank.RoyalFlush,  playingcard.CardName.Ace)
        return False, HandRank(Rank.Unknown)

    def IsStraightFlush(self):
        for i in range(1, 5):
            if (self.Cards[i].Suit != self.Cards[0].Suit) or ((self.Cards[i].Name.value - self.Cards[i-1].Name.value) != 1):
                return False, HandRank(Rank.Unknown)
        return True, HandRank(Rank.StraightFlush,  self.Cards[4].Name)
    
    def IsFourOfaKind(self):
        if self.Cards[0].Name.value == self.Cards[1].Name.value and self.Cards[1].Name.value == self.Cards[2].Name.value and self.Cards[2].Name.value == self.Cards[3].Name.value:
            return True, HandRank(Rank.FourOfaKind,  self.Cards[0].Name), HandRank(Rank.HighCard,  self.Cards[4].Name)
        if self.Cards[1].Name.value == self.Cards[2].Name.value and self.Cards[2].Name.value == self.Cards[3].Name.value and self.Cards[3].Name.value == self.Cards[4].Name.value:
            return True, HandRank(Rank.FourOfaKind,  self.Cards[1].Name), HandRank(Rank.HighCard,  self.Cards[0].Name)
        return False, HandRank(Rank.Unknown), HandRank(Rank.Unknown)

    def IsFullHouse(self):
        if (self.Cards[0].Name.value == self.Cards[1].Name.value and self.Cards[1].Name.value == self.Cards[2].Name.value) and\
            (self.Cards[3].Name.value == self.Cards[4].Name.value):
            return True, HandRank(Rank.FullHouse,  self.Cards[0].Name, self.Cards[3].Name)
        if (self.Cards[2].Name.value == self.Cards[3].Name.value and self.Cards[3].Name.value == self.Cards[4].Name.value) and\
            (self.Cards[0].Name.value == self.Cards[1].Name.value):
            return True, HandRank(Rank.FullHouse,  self.Cards[2].Name, self.Cards[0].Name)
        return False, HandRank(Rank.Unknown)

    def IsFlush(self):
        for i in range(1, 5):
            if self.Cards[i].Suit != self.Cards[0].Suit:
                return False, HandRank(Rank.Unknown)
        return True, HandRank(Rank.Flush, self.Cards[4].Name)

    def IsStraight(self):
        for i in range(1, 5):
            if ((self.Cards[i].Name.value - self.Cards[i-1].Name.value) != 1):
                return False, HandRank(Rank.Unknown)
        return True, HandRank(Rank.Straight,  self.Cards[4].Name)

    def IsThreeOfaKind(self):
        ranks = []
        if self.Cards[0].Name.value == self.Cards[1].Name.value and self.Cards[1].Name.value == self.Cards[2].Name.value:
            ranks.append(HandRank(Rank.ThreeOfaKind,  self.Cards[2].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[4].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[3].Name))
            return True, ranks
        if self.Cards[1].Name.value == self.Cards[2].Name.value and self.Cards[2].Name.value == self.Cards[3].Name.value:
            ranks.append(HandRank(Rank.ThreeOfaKind,  self.Cards[3].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[4].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[0].Name))
            return True, ranks
        if self.Cards[2].Name.value == self.Cards[3].Name.value and self.Cards[3].Name.value == self.Cards[4].Name.value:
            ranks.append(HandRank(Rank.ThreeOfaKind,  self.Cards[4].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[1].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[0].Name))
            return True, ranks
        return False, ranks

    def IsTwoPairs(self):
        if self.Cards[0].Name.value == self.Cards[1].Name.value and self.Cards[2].Name.value == self.Cards[3].Name.value:
            r1 = HandRank(Rank.TwoPairs,  self.Cards[3].Name, self.Cards[1].Name)
            r2 = HandRank(Rank.HighCard,  self.Cards[4].Name)
            return True, r1, r2
        if self.Cards[0].Name.value == self.Cards[1].Name.value and self.Cards[3].Name.value == self.Cards[4].Name.value:
            r1 = HandRank(Rank.TwoPairs,  self.Cards[4].Name, self.Cards[1].Name)
            r2 = HandRank(Rank.HighCard,  self.Cards[2].Name)
            return True, r1, r2
        if self.Cards[1].Name.value == self.Cards[2].Name.value and self.Cards[3].Name.value == self.Cards[4].Name.value:
            r1 = HandRank(Rank.TwoPairs,  self.Cards[4].Name, self.Cards[2].Name)
            r2 = HandRank(Rank.HighCard,  self.Cards[0].Name)
            return True, r1, r2
        return False, HandRank(Rank.Unknown), HandRank(Rank.Unknown)

    def IsOnePair(self):
        ranks = []
        if self.Cards[0].Name.value == self.Cards[1].Name.value:
            ranks.append(HandRank(Rank.OnePair,  self.Cards[1].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[4].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[3].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[2].Name))
            return True, ranks
        if self.Cards[1].Name.value == self.Cards[2].Name.value:
            ranks.append(HandRank(Rank.OnePair,  self.Cards[2].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[4].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[3].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[0].Name))
            return True, ranks
        if self.Cards[2].Name.value == self.Cards[3].Name.value:
            ranks.append(HandRank(Rank.OnePair,  self.Cards[3].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[4].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[1].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[0].Name))
            return True, ranks
        if self.Cards[3].Name.value == self.Cards[4].Name.value:
            ranks.append(HandRank(Rank.OnePair,  self.Cards[4].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[2].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[1].Name))
            ranks.append(HandRank(Rank.HighCard,  self.Cards[0].Name))
            return True, ranks
        return False, ranks

    def IsWon(self, other):
        res = False
        r_self_len = len(self.Ranks)
        r_other_len = len(other.Ranks)
        if r_self_len > 0 and r_other_len > 0:
            r_min = min(r_self_len, r_other_len)
            for i in range(r_min):
                if self.Ranks[i].rank.value > other.Ranks[i].rank.value:
                    return True
                else:
                    if self.Ranks[i].rank.value < other.Ranks[i].rank.value:
                        return False
                    else:
                        # self.Ranks[0].rank.value == other.Ranks[0].rank.value:
                        if self.Ranks[i].highCard.value > other.Ranks[i].highCard.value:
                            return True
                        else:
                            if self.Ranks[i].highCard.value < other.Ranks[i].highCard.value:
                                return False
                            else:
                                # self.Ranks[i].highCard.value == other.Ranks[i].highCard.value
                                if self.Ranks[i].secondCard.value > other.Ranks[i].secondCard.value:
                                    return True
                                else:
                                    if self.Ranks[i].secondCard.value < other.Ranks[i].secondCard.value:
                                        return False
                                # if self.Ranks[i].secondCard.value == other.Ranks[i].secondCard.value than goto next Rank
            # r_min was too small to calculate who won
            if r_self_len > r_other_len:
                return True
        print("Error")
        return res

