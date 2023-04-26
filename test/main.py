class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False


class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None


class UserService:
    def __init__(self, account_repo):
        self.account_repo = account_repo

    def register_user(self, username, password, email, phone, address):
        user = User(username, password, email, phone, address)
        self.account_repo.add_user(user)
        return user

    def login_user(self, username, password):
        user = self.account_repo.get_user_by_username(username)
        if user and user.password == password:
            user.is_logged_in = True
            return user
        return None

    def logout_user(self, user):
        user.is_logged_in = False


class User:
    def __init__(self, username, password, email, phone, address):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.address = address
        self.is_logged_in = False

    def update_profile(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address


# Usage example
user_repo = UserRepository()
user_service = UserService(user_repo)

user1 = user_service.register_user(
    "user1", "password1", "user1@gmail.com", "1234567890", "HCM")
user2 = user_service.register_user(
    "user2", "password2", "user2@gmail.com", "0987654321", "HN")

user = user_service.login_user("user1", "password2")
if user:
    print(f"{user.username} logged in")
else:
    print("Login failed")


        