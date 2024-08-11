from src.widget import mask_account_card


def main():
    card_number = input("Enter your card number: ")
    account_number = input("Enter your account number: ")

    masked_card = mask_account_card(card_number)
    masked_account = mask_account_card(account_number)

    print(f"Original card number: {card_number}")
    print(f"Masked card number: {masked_card}")
    print(f"Original account number: {account_number}")
    print(f"Masked account number: {masked_account}")


if __name__ == "__main__":
    main()
