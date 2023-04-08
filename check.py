import stripe
from termcolor import colored

# Set your Stripe API key
with open("key.txt", "r") as key_file:
    stripe.api_key = key_file.read().strip()

def validate_credit_card(card_number, exp_month, exp_year, cvc):
    try:
        # Create a Stripe Token object with the credit card details
        token = stripe.Token.create(
            card={
                "number": card_number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvc,
            }
        )

        # If the token is created successfully, the credit card is valid
        return True
    except stripe.error.CardError:
        # If there's an error creating the token, the credit card is invalid
        return False

# Read credit card data from file and validate each credit card
valid_cc = []
with open("cclist.txt", "r") as cc_file:
    for line in cc_file:
        card_data = line.strip().split("|")
        card_number = card_data[0]
        exp_month = int(card_data[1])
        exp_year = int(card_data[2])
        cvc = card_data[3]
        if validate_credit_card(card_number, exp_month, exp_year, cvc):
            valid_cc.append(line)

            # Print the credit card number with a green "Valid" message
            print(colored(f"{card_number} >> Valid", "green"))
        else:
            # Print the credit card number with a red "Invalid" message
            print(colored(f"{card_number} >> Invalid", "red"))

# Write the valid credit cards to file
with open("ccvalid.txt", "w") as valid_file:
    valid_file.writelines(valid_cc)
