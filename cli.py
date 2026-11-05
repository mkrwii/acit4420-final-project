from classes.classes import Offer, Flexibility
from classes.request import Request

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


def splash_screen():
    ascii_art()
    print("Welcome to BusBidder Spain, your Python-powered Bus ticket marketplace.")

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


def main():
    print("This module is not intended to be run directly. Please run main.py instead.")


if __name__ == "__main__":
    main()