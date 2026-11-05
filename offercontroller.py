from classes import Offer, Flexibility

def read_offers_from_file(logger, filename="offers.csv",):
    offers = []
    try:
        with open(filename, "r") as f:
            logger.debug(f"Reading offers from {filename}...")
            for line in f:
                company, origin, destination, price, transfers, duration, luggage, flexibility = line.strip().split(",")
                offer = Offer(company, origin, destination, float(price), int(transfers), float(duration), int(luggage), Flexibility[flexibility])
                offers.append(offer)
    except FileNotFoundError:
        logger.error(f"File {filename} not found. Please ensure the file exists.")
    return offers
