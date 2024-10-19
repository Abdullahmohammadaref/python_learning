def main():

    user_greeting = input("Greeting: ").lower().strip()
    print(value(user_greeting))

def value(greeting):

    if greeting.startswith("hello"):
        return f"$0"
    elif greeting.startswith("h"):
        return f"$20"
    else:
        return f"$100"

if __name__ == "__main__":
    main()