from seleniumbase import BaseCase

class TestMFALogin(BaseCase):
    def test_mfa_login(self):
        self.open("https://seleniumbase.io/realworld/login")
        self.type("#username", "demo_user")
        self.type("#password", "secret_pass")
        self.enter_mfa_code("#totpcode", "GAXG2MTEOR3DMMDG")  # 6-digit
        self.assert_element("img#image1")
        self.assert_exact_text("Welcome!", "h1")
        self.click('a:contains("This Page")')
        self.save_screenshot_to_logs()
