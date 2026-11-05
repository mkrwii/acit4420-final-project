from classes import Offer, Flexibility
from offerchecker import OfferChecker
from cli import splash_screen, requester
from testrun import testrequester
import logging



logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

def read_offers_from_file(filename="offers.csv"):
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

def testrun():
    offers = read_offers_from_file("data/offers.csv")
    req = testrequester(logger)
    for offer in offers:
        checker = OfferChecker(offer, req)
        checker.check_offer()

def runcli():
    offers = read_offers_from_file("data/offers.csv")
    req = requester()
    for offer in offers:
        checker = OfferChecker(offer, req)
        checker.check_offer()

def main():
    splash_screen()
    while True:
        print("Type 'test' to run a test, 'cli' for full interface or 'exit' to quit.")
        choice = input("Your choice: ")
        if choice == "test":
            testrun()
            pass
        elif choice == "cli":
            runcli()
        elif choice == "exit":
            print("Thank you for using BusBidder Spain!")
            return
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
