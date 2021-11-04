import hashlib
import uuid


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self.__password_hash

    @password.setter
    def password(self, value):
        salt = uuid.uuid4().hex
        self.__password_hash = hashlib.sha512((value + salt).encode()).hexdigest()


user1 = User("user1", "12345qwe")
print(user1.password)
