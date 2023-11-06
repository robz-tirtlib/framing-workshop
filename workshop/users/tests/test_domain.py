from django.test import TestCase

from users.services.user_profile_service.domain import is_user_allowed
from users.tests.materials import user_dto


class ProfileDomainTestCase(TestCase):
    def setUp(self):
        self.user = user_dto

    def test_is_user_allowed(self):
        self.assertEqual(is_user_allowed(self.user, 1), True)
        self.assertEqual(is_user_allowed(self.user, 2), False)
        self.assertEqual(is_user_allowed(None, 1), False)
