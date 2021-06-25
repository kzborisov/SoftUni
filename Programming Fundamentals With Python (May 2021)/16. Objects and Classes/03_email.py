# Task 03. Email

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: "\
               f"{self.content}. Sent: {self.is_sent}"


info = input()
emails = []

while not info == "Stop":
    sender, receiver, content = info.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    info = input()

indices = [int(x) for x in input().split(", ")]

for x in indices:
    emails[x].send()

for email in emails:
    print(email.get_info())

