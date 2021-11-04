import re


class Profile:
    username_min_length = 5
    username_max_length = 15

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __validate_username(self, username):
        if len(username) not in range(self.username_min_length, self.username_max_length):
            raise ValueError("The username must be between 5 and 15 characters.")

    def __validate_password(self, password):
        if not re.match(r"\b[A-Za-z\d]{8,}", password):
            raise ValueError("The password must be 8 or more "
                             "characters with at least 1 digit and 1 uppercase letter.")

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def password(self):
        return "*" * len(self.__password)

    @password.setter
    def password(self, value):
        self.__validate_password(value)
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" '\
               f'and password: {self.password}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
