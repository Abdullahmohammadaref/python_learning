class People:

    def __init__(self, name, money_paid):
        self.name = name
        self.money_paid = money_paid
        self.should_pay_money = 0
        self.should_get_money = 0
        self.should_pay = True
        self.should_get_paid = False

    def __str__(self):
        return f"{self.name} spent {self.money_paid}TL"

    def total(self):
        total = 0
        for person in self.money_paid:
            total += person.money
        return total

    def should_pay(self):
        for person in self.money_paid:
            if person.money < People.total(person):
                continue
            elif person.money > People.total(person):
                self.should_pay = False
                self.should_get_paid = True
            else:
                self.should_pay = False
                self.should_get_paid = False

    def should_pay_or_get_paid_price(self):
        People.should_pay()
        print(f"Total_money_spent: {People.total()}")
        for person in self.money_paid:
            if self.should_pay == True and self.should_get_paid == False:
                self.should_pay_money = People.total(person) - self.money_paid
                print(f"{person.name} should pay {self.should_pay_money}TL")
            elif self.should_pay == False and self.should_get_paid == True:
                self.should_get_money = self.money_paid - person.total(person)
                print(f"{person.name} should get {self.should_get_money}TL")
            else:
                continue

def main():
    people = []
    while True:
        name = input("Name: ")
        money_paied = input("Money paid: ")
        person = People(name, money_paied)
        people.append(person)
        user_status = input("Are you done?")
        if user_status == "yes":
            break

    People.should_pay_or_get_paid_price(people)


