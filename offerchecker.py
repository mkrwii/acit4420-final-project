from classes import Offer, Flexibility
from request import Request

class OfferChecker:
    def __init__(self, offer, request):
        self.offer = offer
        self.request = request

    def check_offer(self):
        checks = {
            "Origin": self.offer.origin == self.request.data["origin"][0],
            "Destination": self.offer.destination == self.request.data["destination"][0],
            "Budget": self.offer.price <= self.request.data["budget"][0],
            "Transfers": self.offer.transfers <= self.request.data["maxtransfers"][0],
            "Duration": self.offer.duration <= self.request.data["duration"][0],
            "Luggage": self.offer.luggage >= self.request.data["luggage"][0],
            "Flexibility": self.offer.flexibility.value >= self.request.data["flexibility"][0].value,
        }


        overall = all(checks.values())
        if overall:
            print("This offer meets all your requirements!")
        else:
            print("This offer does not meet all your requirements.")
            for key, value in checks.items():
                if not value:
                    print(f"  - Requirement not met: {key}")

        return overall