"""
Random Advice Generator
A tiny demo project for the setup workshop.

Fetches a random piece of advice from a public API and prints it
to the terminal. Used to confirm that Python, pip, and your
internet connection are all working together.
"""

import requests
from colorama import init, Fore

# init(autoreset=True) makes colored text reset automatically after each
# print, and makes colors work correctly in Windows terminals.
init(autoreset=True)

ADVICE_API_URL = "https://api.adviceslip.com/advice"


def get_random_advice():
    """Ask the Advice Slip API for one random piece of advice."""
    response = requests.get(ADVICE_API_URL, timeout=5)
    response.raise_for_status()  # raises an error if the request failed
    data = response.json()
    return data["slip"]["advice"]


def main():
    print(Fore.CYAN + "✨ Random Advice Generator ✨\n")

    while True:
        advice = get_random_advice()
        print(Fore.YELLOW + f'"{advice}"\n')

        again = input("Press Enter for more advice, or type 'q' to quit: ")
        if again.strip().lower() == "q":
            print(Fore.CYAN + "\nThanks for stopping by! \U0001F44B")
            break


if __name__ == "__main__":
    main()
