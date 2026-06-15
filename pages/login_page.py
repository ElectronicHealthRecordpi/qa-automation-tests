from utils.config import BASE_URL
class LoginPage:
    def __init__(self, page):
        self.page = page
    def open(self):
        self.page.goto(f"{BASE_URL}/auth/login")
    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")
    