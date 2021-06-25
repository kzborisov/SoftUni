# Task 02. Party

class Party:
    def __init__(self):
        self.people = []


person = input()
party = Party()

while not person == "End":
    party.people.append(person)
    person = input()


print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
