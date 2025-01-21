class LoginHandler:
    def __init__(self, user_model):
        self.user_model = user_model

    def handle_login(self, username, password):
        if self.validate_user(username, password):
            return "Login successful"
        return "Invalid username or password"

    def validate_user(self, username, password):
        user = self.user_model.get_user_by_username(username)
        if user and user.password == password:
            return True
        return False