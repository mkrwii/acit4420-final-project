from classes import Flexibility

class Request:
    def __init__(self, origin, destination, budget, maxtransfers, duration, luggage, flexibility):
        """
        Initializes a Request object. For each attribute, it stores a tuple containing the value and a boolean indicating whether the attribute is a hard requirement (True) or a soft preference (False).
        """
        self.data = {
            "origin": (origin, True),
            "destination": (destination, True),
            "budget": (float(budget), True),
            "maxtransfers": (int(maxtransfers), True),
            "duration": (float(duration), True),
            "luggage": (int(luggage), True),
            "flexibility": (Flexibility[flexibility.upper()], True)
        }
