# Problem Statement: Use the existing Event class by adding an instance attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

class Event():
    def __init__(self, name, date, participant_count = 0):
        self.name = name
        self.date = date
        self.participant_count = participant_count

    def add_participant(self):
         while True:
                try:
                    guests = int(input(f"How many people are you going to bring to {self.name}?"))
                    self.participant_count += guests
                    print(f"{guests} guests have been added to the {self.name} event.")
                    break
                except TypeError:
                    print("Please enter a valid number of guests you are bringing.")
                    continue

    def get_participant_count(self):
        print(f"There are currently {self.participant_count} guest coming to the {self.name} that is happening on {self.date}.")

Book_club = Event('Book Club', '06/25/2024')
BabyShower = Event('Baby Shower', '08/25/2024')
Wedding = Event('Wedding', '10/15/2025')


Book_club.add_participant()
Book_club.get_participant_count()


Wedding.add_participant()
Wedding.get_participant_count()
