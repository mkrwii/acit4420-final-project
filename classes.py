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

