from validator_collection import validators

def main():
    email = input("email: ")

    try:
        valid_email = validators.email(email)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()