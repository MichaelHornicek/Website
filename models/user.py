class User:
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    def save(self):
        # Logic to save user data to a database or file
        pass

    @classmethod
    def retrieve(cls, username):
        # Logic to retrieve user data from a database or file
        pass