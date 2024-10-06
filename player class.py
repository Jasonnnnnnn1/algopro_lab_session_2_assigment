class Aladdin:
    def __init__(self, name, health=100, mana=100):
        self.name = name
        self.health = health
        self.mana = mana

    def increase_health(self, amount):
        self.health += amount

    def decrease_health(self, amount):
        if self.health >= amount:
            self.health -= amount
        else:
            self.health = 0
            print("u'd die with 0 health smartass")

    def increase_mana(self, amount):
        self.mana += amount

    def decrease_mana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
        else:
            self.mana = 0
            print("No mana lmfao, what is this choice??")


    def display_status(self):

        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        if self.health <= 0:
            print("You're dead.")
        print(f"Mana: {self.mana}")
        if self.mana <= 0:
            print("Better drink ur potions buddy.")

def main():
    name = input("Enter your name: ")
    aladdin = Aladdin(name)

    while True:
        print("\nOptions:")
        print("1. Increase health")
        print("2. Decrease health")
        print("3. Increase mana")
        print("4. Decrease mana")
        print("5. Player Status")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = int(input("Enter amount: "))
            aladdin.increase_health(amount)
        elif choice == "2":
            amount = int(input("Enter amount: "))
            aladdin.decrease_health(amount)
        elif choice == "3":
            amount = int(input("Enter amount: "))
            aladdin.increase_mana(amount)
        elif choice == "4":
            amount = int(input("Enter amount: "))
            aladdin.increase_mana(amount)
        elif choice == "5":
            aladdin.display_status()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()