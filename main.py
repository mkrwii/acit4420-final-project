import random
from classes import Offer, Request, Flexibility


def ascii_art():
    art = r"""
    ████        ▄▄▄▄    ▄▄▄▄     ▄▄▄▄▄▄▄ ████        ████        ████        ████ ▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄    
    █▀░▀▀▀▓█▀▄  █▀ ░    █▀▄█  ▄▀█▓▀ ▀░▀█ █▀░▀▀▀▓█▀▄  █▀░▀  ▄▀█▓▀▀▀░▀█  ▄▀█▓▀▀▀░▀█ █▀ ▀ ▀▓█▀▄  █▀ ░ ▀▓█▀▄ 
    ▌░█░  ▐▌░▐▌ ▌█░▒    ▌░▐▓ ▐▌░▐▌  ░█░▐ ▌░█░  ▐▌░▐▌ ▀▀▀▀ ▐▌░▐▌  ░█░▐ ▐▌░▐▌  ░█░▐ ▌░░▒  ▐▌▒▐▌ ▌█░▒  ▐▌░▐▌
    ▀■░▒   ▌█▀░ ▀░■░    ▌█▀░ ░▀█▐        ▀■░▒   ▌█▀░ ▀■░▒ ░▀█▐   ▒░■▀ ░▀█▐   ▒░■▀ ▀ ■░   ▌░▀░ ▀░■░   ▌░▀░
    ▒░█░   ▒░░▒ ░▒░░    ▒░░▒  ▀▀▀▀▀▀▒░░▒ ▒░█░   ▒░░▒ ▒░█░ ▒░░▒   ░█░▒ ▒░░▒   ░█░▒ ▒░░ ▀▀▀▀▀▀▀ ░▒░░       
    ▄■ ▄   ▄■█░ ▄░■░    ▄■█░ ▄■ ▄   ▄■█░ ▄■ ▄   ▄■█░ ▄■ ▄ ░█■▄   ▄ ■▄ ░█■▄   ▄ ■▄ ▄■█░   ▒■▄░ ▄░■░       
    ▌░█▐  ▐▌░█▌ ▌░░▐   ▐▌░█▌ ▌░█▐  ▐▌░█▌ ▌░█▐  ▐▌░█▌ ▌░█▐ ▐█░▐▌  ▌█░▐ ▐█░▐▌  ▌█░▐ ▌░░▐  ▐░▐█▌ ▌░░▐       
    ▓▄▄█ ▄██▄▀  █▄▄▓  ▄██▄▀  ▓▄▄█ ▄██▄▀  ▓▄▄█ ▄██▄▀  ▓▄▄█  ▀▄██▄ █▄▄▓  ▀▄██▄ █▄▄▓ █▄▄▓ ▄▄▄█▀  █▄▄▓       
    ▀▀▀▀▀▀▀     ▀▀▀▀▀▀▀▀     ▀▀▀▀▀▀▀     ▀▀▀▀▀▀▀     ▀▀▀▀     ▀▀▀▀▀▀▀     ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀     ▀▀▀▀       
    
    """
    print(art)

def requester():
    while True:
        input_origin = input("Please enter the city you want to travel from: ")
        input_destination = input("Please enter the city you want to travel to: ")
        input_price = input("Please enter your max budget for the trip, in EUR: ")
        input_maxtransfers = input("Please enter your maximum number of transfers: ")
        input_duration = input("Please enter your preferred duration of trip, in hours: ")
        input_luggage = input("Please enter how many pieces of luggage you intend to carry: ")
        print("Levels of flexibility available are:")
        print("Fully refundable: enter FULL")
        print("Rebookable but not refundable: enter REBOOKABLE")
        print("Not refundable or rebookable: enter NONE")
        input_flexibility = input("Please tell us your preferred level of flexibility: ")
        try:
            req = Request(input_origin, input_destination, input_price, input_maxtransfers, input_duration, input_luggage, input_flexibility)
            print("Request successfully produced!")
            return req
        except Exception as e:
            print(f"Error when generating request: {e}")
            print("Please try again.")

def check_offer(offer_obj, request_obj):
    checks = {
        "Origin": offer_obj.origin == request_obj.origin,
        "Destination": offer_obj.destination == request_obj.destination,
        "Budget": offer_obj.price <= request_obj.budget,
        "Transfers": offer_obj.transfers <= request_obj.maxtransfers,
        "Duration": offer_obj.duration <= request_obj.duration,
        "Luggage": offer_obj.luggage >= request_obj.luggage,
        "Flexibility": offer_obj.flexibility.value >= request_obj.flexibility.value,
    }

    print(f"Checking offer from {offer_obj.company}:")
    print(f"  Origin: {offer_obj.origin}")
    print(f"  Destination: {offer_obj.destination}")
    print(f"  Price: {offer_obj.price} EUR")
    print(f"  Transfers: {offer_obj.transfers}")
    print(f"  Duration: {offer_obj.duration} hours")
    print(f"  Luggage: {offer_obj.luggage} pieces")
    print(f"  Flexibility: {offer_obj.flexibility.name}")

    for criterion, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"  {criterion}: {status}")

    overall = all(checks.values())

    if overall:
        print("=> Offer is within the requested values.")
    else:
        print("=> Offer does NOT meet the requested values.")

    return overall

def test_offers(seed, num_offers):
    """
    Generates a list of Offer objects for testing purposes. The number of offers generated is determined by num_offers.
    """
    offers = []
    if seed is not None:
        random.seed(seed)
    else:
        random.seed(186)
    companies = ["SolRuta", "Camino Express", "CostaLink", "VerdeBus", "NocheVia"]
    for _ in range(num_offers):
        company = random.choice(companies)
        price = round(random.uniform(10, 100), 2)
        transfers = random.randint(0, 3)
        duration = round(random.uniform(1, 10), 1)
        luggage = random.randint(0, 5)
        flexibility = random.choice(list(Flexibility))
        offers.append(Offer(company, price, transfers, duration, luggage, flexibility))
    return offers

def read_offers_from_file(filename="offers.csv"):
    offers = []
    try:
        with open(filename, "r") as f:
            print(f"Reading offers from {filename}...")
            for line in f:
                company, origin, destination, price, transfers, duration, luggage, flexibility = line.strip().split(",")
                offer = Offer(company, origin, destination, float(price), int(transfers), float(duration), int(luggage), Flexibility[flexibility])
                offers.append(offer)
    except FileNotFoundError:
        print(f"File {filename} not found. Please ensure the file exists.")
    return offers

def main():
    ascii_art()
    offers = read_offers_from_file("data/offers.csv")
    print("Welcome to BusBidder Spain, your Python-powered Bus ticket marketplace.")
    req = requester()
    for offer in offers:
        check_offer(offer, req)
    
        



if __name__ == "__main__":
    main()
