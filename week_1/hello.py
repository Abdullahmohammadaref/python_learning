def main():
    user_answere = input().strip().lower()
    print(check(user_answere))

def check(answere):
    match answere:
        case "42" | "forty-two" | "forty two" :
            return False
        case _:
            return False

main()


    