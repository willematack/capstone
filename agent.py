from itertools import count
from decimal import Decimal
import numpy as np
import random

class Agent:
    _ids = count(0)

    def __init__(self, emax):
        self._id = next(self._ids)
        self.emax = emax
        self.profit = [0]
        self.inventory = [0]
        return

    def settle(self,sellOrder, bid, buyWinner, buyOrder, ask, sellWinner):
        # print('sell: ' + str(sellOrder*ask))
        # print('buy: ' + str(buyOrder*bid))
        # print('\n')
        if self._id == buyWinner:
            print('bid: ' + str(bid))
            self.inventory.append(self.inventory[-1] + buyOrder)
            self.profit.append(self.profit[-1] - buyOrder*bid)
        elif self._id == sellWinner:
            print('ask: ' + str(ask))
            self.inventory.append(self.inventory[-1] - sellOrder)
            self.profit.append(self.profit[-1] + sellOrder*ask)
        else:
            self.profit.append(self.profit[-1])

    def quote(self, price, buyOrder, sellOrder):
        """
        gets the bid and ask spread,
        """
        bidSpread, askSpread = self.spread()
        bid, ask = self.bid_ask(price, bidSpread, askSpread, buyOrder, sellOrder)
        return bid, ask

    def bid_ask(self, price, bidSpread, askSpread, buyOrder, sellOrder):
        bid = round(Decimal(price*(1-bidSpread)),2)
        ask = round(Decimal(price* (1+ askSpread)),2)
        return bid, ask

    def spread(self):
        """
        normalize: This will normalize the spread value to something that makes
            sense. Because prevDemand floats between ~ 100 and -100, it has been
            set to som value between 75 and 100.

        prevDemand: The demand in the last iteration. Assumption for now is that
            the bid-ask will adjust on past demand. Reminder that the demand is
            the difference between buy-sell. Low absolute demand means balance.

        spread: gonna be the value that the bid-ask is from the reference; however,
            a skew may be used as well.

        bidSpread / askSpread: This will adjust the spreads so that they are skewed
            in the favourable direction. i.e. if the prevDemand is less than 0,
            more people are selling, thus the ask price should be cheaper.
        """
        # normalize = random.uniform(75,100)
        # spread = abs(prevDemand/normalize)
        # bidSpread = spread - 0.05 if prevDemand > 0 else spread
        # askSpread = spread - 0.05 if prevDemand < 0 else spread
        bidSpread = random.uniform(0, self.emax)
        askSpread = random.uniform(0, self.emax)
        return bidSpread, askSpread
