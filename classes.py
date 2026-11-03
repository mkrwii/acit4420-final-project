from enum import Enum


class Flexibility(Enum):
    NONE = 1
    REBOOKABLE = 2
    FULL = 3


class Offer:
    def __init__(self, company, price, transfers, duration, luggage, flexibility):
        self.company = company
        self.price = price
        self.transfers = transfers
        self.duration = duration
        self.luggage = luggage
        self.flexibility = flexibility


class Request:
    def __init__(self, budget, maxtransfers, duration, luggage, flexibility):
        self.budget = float(budget)
        self.maxtransfers = int(maxtransfers)
        self.duration = float(duration)
        self.luggage = int(luggage)
        self.flexibility = Flexibility[flexibility.upper()]