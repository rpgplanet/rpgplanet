from djangosanetesting import SeleniumTestCase

from rpgcommon.user.models import InvitedEmail

class TestRegistration(SeleniumTestCase):
    fixtures = ['sites']

    def test_registration_of_invited_user(self):
        InvitedEmail.objects.create(email='testorz@example.com')
        self.transaction.commit()

        s = self.selenium
        s.open('/registrace/')
        s.wait_for_page_to_load(30000)

        s.type('id_username', 'testorz')
        s.type('id_email', 'testorz@example.com')
        s.type('id_password1', 'xxx')
        s.type('id_password2', 'xxx')
        s.click("//input[@name='traditional_registration']")
        s.wait_for_page_to_load(30000)

        self.assert_equals('testorz.rpghrac.cz', s.get_text("//a[@name='user-homepage']"))
