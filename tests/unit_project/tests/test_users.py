# -*- coding: utf-8 -*-
from djangosanetesting.cases import DatabaseTestCase
from djangosanetesting.utils import mock_settings

from rpgcommon.user.user import create_user
from ella.core.models import Category

class TestRegistration(DatabaseTestCase):

    def test_andros_properly_slugified(self):
        user = create_user(u"Andrej Tokarčík", "xxx", "tester@example.com")

        self.assert_equals('andrej-tokarcik', user.get_profile().slug)

    def test_registering_same_email_causes_error(self):
        create_user(u"Andrej Tokarčík", "xxx", "tester@example.com")

        self.assert_raises(ValueError, create_user, u"Neumětel", "xerox", "tester@example.com")

    def test_registering_same_slug_error(self):
        create_user(u"Andrej Tokarčík", "xxx", "tester@example.com")

        self.assert_raises(ValueError, create_user, u" Andrej-Tokarcik   ", "xerox", "hustor@example.com")

class TestCategoryHandling(DatabaseTestCase):

    def test_root_category_created(self):
        user = create_user(u"Andrej Tokarčík", "xxx", "tester@example.com")

        self.assert_equals(1, len(Category.objects.filter(site=user.get_profile().site, tree_path="")))
        
    @mock_settings("DYNAMIC_RPGPLAYER_CATEGORIES", [
        {
            "tree_path" : "rpg",
            "parent_tree_path" : "",
            "title" : "RPG",
            "slug" : "rpg",
        },
        {
            "tree_path" : "rpg/drd",
            "parent_tree_path" : "rpg",
            "title" : "Draci Doupe",
            "slug" : "drd",
        },
    ])
    @mock_settings("USER_MANDATORY_DYNAMIC_CATEGORIES", ["rpg", "rpg/drd"])
    def test_mandatory_categories_created(self):
        user = create_user(u"Andrej Tokarčík", "xxx", "tester@example.com")

        self.assert_equals(3, len(Category.objects.filter(site=user.get_profile().site)))

