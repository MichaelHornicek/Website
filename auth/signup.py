class SignupHandler:
    def handle_signup(self, username, password, user_type):
        if self.create_user(username, password, user_type):
            return "User signed up successfully!"
        return "Signup failed!"

    def create_user(self, username, password, user_type):
        # Logic to create a new user and save to the database
        # This is a placeholder for actual user creation logic
        return True  # Assume user creation is successful for this example