from classes import Offer, Flexibility
from request import Request

def testrequester(logger):
    while True:
        input_origin = "Madrid"
        input_destination = "Barcelona"
        input_price = "100"
        input_maxtransfers = "2"
        input_duration = "5"
        input_luggage = "1"
        input_flexibility = "FULL"
        try:
            req = Request(input_origin, input_destination, input_price, input_maxtransfers, input_duration, input_luggage, input_flexibility)
            logger.debug("Request successfully produced!")
            return req
        except Exception as e:
            logger.error(f"Error when generating request: {e}")
            logger.debug("Please try again.")

def main():
    print("This module is not intended to be run directly. Please run main.py instead.")

if __name__ == "__main__":
    main()