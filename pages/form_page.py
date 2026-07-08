class FormPage:
    URL = "https://testautomationpractice.blogspot.com/"

    def __init__(self, page):
        self.page = page
        self.name_field = page.locator("#name")
        self.email_field = page.locator("#email")
        self.tuesday_checkbox = page.locator("#tuesday")
        self.country_dropdown = page.locator("#country")

    def goto(self):
        self.page.goto(self.URL)

    def fill_name(self, name):
        self.name_field.fill(name)

    def fill_name(self, email):
        self.name_field.fill(email)

    def check_tuesday(self):
        self.tuesday_checkbox.check()

    def select_country(self, label):
        self.country_dropdown.select_option(label=label)