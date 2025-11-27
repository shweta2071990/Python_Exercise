from datetime import datetime

# ---------------------------------
# Base class
# ---------------------------------
class Publication:
    def __init__(self, text):
        self.text = text

    def format(self):
        """Method to be overridden by children."""
        pass

    def publish(self):
        """Appending formatted publication to the file."""
        with open("news_feed.txt", "a", encoding="utf-8") as f:
            f.write(self.format() + "\n\n")


# ---------------------------------
# NEWS block
# ---------------------------------
class News(Publication):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def format(self):
        return (
            "News -------------------------\n"
            f"{self.text}\n"
            f"{self.city}, {self.date}"
        )


# ---------------------------------
# PRIVATE AD block
# ---------------------------------
class PrivateAd(Publication):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        self.days_left = (self.expiration_date - datetime.now()).days

    def format(self):
        return (
            "Private Ad -------------------\n"
            f"{self.text}\n"
            f"Expires on: {self.expiration_date.date()}. "
            f"Days left: {self.days_left}"
        )


# ---------------------------------
# UNIQUE PUBLICATION TYPE
# Motivational Quote (random rating added)
# ---------------------------------
class MotivationalQuote(Publication):
    def __init__(self, text, author):
        super().__init__(text)
        self.author = author
        self.timestamp = datetime.now().strftime("%A, %d %B %Y")

    def format(self):
        # Custom rule: Each quote is wrapped in stars and stamped with date + author
        return (
            "Motivational Quote ************\n"
            f"\"{self.text}\"\n"
            f"- {self.author}\n"
            f"Published on: {self.timestamp}"
        )


# ---------------------------------
# System Menu
# ---------------------------------
def user_menu():
    while True:
        print("\nChoose what you want to publish:")
        print("1 - News")
        print("2 - Private Ad")
        print("3 - Motivational Quote (unique type)")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            text = input("Enter news text: ")
            city = input("Enter city: ")
            News(text, city).publish()
            print("News published!")

        elif choice == "2":
            text = input("Enter ad text: ")
            date = input("Enter expiration date (YYYY-MM-DD): ")
            PrivateAd(text, date).publish()
            print("Ad published!")

        elif choice == "3":
            text = input("Enter your quote: ")
            author = input("Enter author name: ")
            MotivationalQuote(text, author).publish()
            print("Quote published!")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")


# ---------------------------------
# Run Tool
# ---------------------------------
if __name__ == "__main__":
    user_menu()