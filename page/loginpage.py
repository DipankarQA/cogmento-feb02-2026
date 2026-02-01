from playwright.sync_api import expect



class LoginPage():
    def __init__(self, page):
        self.page = page 
        self.username = "//*[@name ='email']"
        self.password="//*[@name ='password']"
        self.submit_button = "//*[text() ='Login']"
        self.homepage_heading="//*[text() ='Deals Summary']"

    def login_verify(self, user, password):
        self.page.goto("https://ui.cogmento.com/")
        self.page.locator(self.username).fill(user)
        self.page.locator(self.password).fill(password)
        self.page.locator(self.submit_button).click()
        self.page.wait_for_selector(self.homepage_heading, timeout = 5000)
        actual_heading = self.page.locator(self.homepage_heading).inner_text()
        print(actual_heading)
        expected_heading = "Deals Summary"
        expect(self.page.locator(self.homepage_heading)).to_have_text("Deals Summary")
        assert expected_heading.lower().strip()== actual_heading.lower().strip()
