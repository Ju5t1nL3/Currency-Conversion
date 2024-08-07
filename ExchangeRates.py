"""
Converts between any two currencies.
"""

from SecretApiKey import api_key
import requests
import time

BASE_URL = "https://v6.exchangerate-api.com/v6/"
API_KEY = api_key

UP_ONE = "\033[1A"
CLEAR_LINE = "\033[K"

UP_AND_CLEAR = UP_ONE + CLEAR_LINE


JSON = f"{BASE_URL}{api_key}/latest/"


def clear_input():
    """
    Clears two lines of code and returns cursor up 3.
    """
    print(f"{UP_AND_CLEAR}{UP_AND_CLEAR}{UP_ONE}")


def get_base():
    """
    Gets the base currency and returns the json for that currency.
    """
    while True:
        base_code = input(
            "Enter the ISO 4217 3-letter currency code for the base currency: ").strip().upper()
        new_json = JSON + base_code

        if requests.get(new_json).json()["result"] != "success":
            print("That is not a valid ISO 4217 3-letter currency code. Try again")
            time.sleep(1)
            clear_input()

        else:
            break

    return new_json


def get_amount():
    """
    Get the amount of money and return it.
    """
    while True:
        try:
            amount = float(input("Enter the amount of that base currency: "))
            break
        except ValueError:
            print("That is not a valid float number. Try again.")
            time.sleep(1)
            clear_input()

    return amount


def new_code(json):
    """
    Get the new currency and return it.
    """
    while True:
        try:
            new_code = input(
                "Enter the currency you want to convert to: ").strip().upper()
            requests.get(json).json()["conversion_rates"][new_code]
            break
        except Exception as e:
            print("That is not a valid ISO 4217 3-letter currency code. Try again.")
            time.sleep(1)
            clear_input()

    return new_code


def convert(json, amount):
    """
    Takes in the json base code and amount of that currency and converts it to the new currency.
    """
    code = new_code(json)
    rate = requests.get(json).json()["conversion_rates"][code]
    return f"{(amount * rate):.2f} {code}"


# start program
json = get_base()
amount = get_amount()

print(convert(json, amount))
