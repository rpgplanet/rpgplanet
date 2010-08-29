# -*- coding: utf-8 -*-
from djangosanetesting.cases import DatabaseTestCase

from rpgcommon.user.user import create_user

class TestAndrosRegistration(DatabaseTestCase):

    def test_andros_properly_slugified(self):
        user = create_user(u"Andrej Tokarčík", "xxx", "tester@example.com")

        self.assert_equals('andrej-tokarcik', user.get_profile().slug)
