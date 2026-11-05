from controllers.offerchecker import OfferChecker
from cli import splash_screen, requester
from testrun import testrequester
import logging
from controllers.offercontroller import read_offers_from_file
import argparse

argument_parser = argparse.ArgumentParser(description="BusBidder Spain CLI")
argument_parser.add_argument("--test", action="store_true", help="Run the program in test mode")
args = argument_parser.parse_args()



logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


def testrun():
    offers = read_offers_from_file(logger, "data/offers.csv")
    req = testrequester(logger)
    for offer in offers:
        checker = OfferChecker(offer, req)
        checker.check_offer()

def runcli():
    offers = read_offers_from_file(logger, "data/offers.csv")
    req = requester()
    for offer in offers:
        checker = OfferChecker(offer, req)
        checker.check_offer()

def main():
    if args.test:
        testrun()
        return
    splash_screen()
    while True:
        print("Type 'test' to run a test, 'cli' for full interface or 'exit' to quit.")
        choice = input("Your choice: ")
        if choice == "test":
            testrun()
        elif choice == "cli":
            runcli()
        elif choice == "exit":
            print("Thank you for using BusBidder Spain!")
            return
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
