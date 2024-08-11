from src.masks import get_mask_card_number, get_mask_account

def main():
    card_number = input("Enter your card number: ")
    account_number = input("Enter your account number: ")

    masked_card = get_mask_card_number(int(card_number))
    masked_account = get_mask_account(int(account_number))

    print(f"Original card number: {card_number}")
    print(f"Masked card number: {masked_card}")
    print(f"Original account number: {account_number}")
    print(f"Masked account number: {masked_account}")

if __name__ == "__main__":
    main()