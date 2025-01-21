# Website
# Python Login App

This project is a simple web application that allows users to sign up or log in with two user types: Manager and Employee. It is built using Python and a web framework.

## Project Structure

```
python-login-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── auth             # Authentication module
│   │   ├── __init__.py  # Initializes the auth module
│   │   ├── login.py     # Handles user login functionality
│   │   └── signup.py    # Handles user signup functionality
│   ├── models           # User models
│   │   ├── __init__.py  # Initializes the models module
│   │   └── user.py      # User representation and data management
│   ├── templates        # HTML templates for the application
│   │   ├── login.html   # Login page template
│   │   └── signup.html  # Signup page template
│   └── types            # Type definitions
│       └── __init__.py  # Initializes the types module
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## User Types

- **Manager**: Has access to managerial functionalities.
- **Employee**: Has access to employee functionalities.
