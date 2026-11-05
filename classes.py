from enum import Enum


class Flexibility(Enum):
    NONE = 1
    REBOOKABLE = 2
    FULL = 3


class Offer:
    def __init__(self, company, origin, destination, price, transfers, duration, luggage, flexibility):
        self.company = company
        self.origin = origin
        self.destination = destination
        self.price = price
        self.transfers = transfers
        self.duration = duration
        self.luggage = luggage
        self.flexibility = flexibility


class Request:
    def __init__(self, origin, destination, budget, maxtransfers, duration, luggage, flexibility):
        self.origin = origin
        self.destination = destination
        self.budget = float(budget)
        self.maxtransfers = int(maxtransfers)
        self.duration = float(duration)
        self.luggage = int(luggage)
        self.flexibility = Flexibility[flexibility.upper()]