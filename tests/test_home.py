from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):
        # open login page
        self.open("http://ask-qa.portnov.com")

        # assert page title
        self.assert_title("Assessment Control @ Portnov")

        # assert page url contains login
        self.assert_url_contains("logout")

