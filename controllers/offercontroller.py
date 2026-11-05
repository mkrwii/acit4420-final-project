from classes.classes import Offer, Flexibility
from controllers.offerchecker import OfferChecker

def read_offers_from_file(logger, filename="data/offers.csv",):
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

def filter_offers(request, offers):
    output_offers = []
    for offer in offers:
        checker = OfferChecker(offer, request)
        if checker.check_offer():
            output_offers.append(offer)
    return output_offers

def rank_offers(request, offers):
    # Placeholder for future implementation of ranking offers based on user preferences
    pass


def run_offer_checker(request, logger):
    offers = read_offers_from_file(logger)
    filtered_offers = filter_offers(request, offers)
    if not filtered_offers:
        logger.info("No offers meet your requirements.")
    else:
        for offer in filtered_offers:
            print(f"Company: {offer.company}, Origin: {offer.origin}, Destination: {offer.destination}, Price: {offer.price}, Transfers: {offer.transfers}, Duration: {offer.duration}, Luggage: {offer.luggage}, Flexibility: {offer.flexibility.name}")