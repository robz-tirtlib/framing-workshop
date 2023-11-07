from django.test import TestCase

from users.services.auth_service.infrastructure import (
    is_username_unique, is_email_unique, is_unique
)

from users.test.test_auth.materials import (
    user_register, UserDAOMock, FormMock
)


class UniquenessTestCase(TestCase):
    def setUp(self):
        self.user_dao = UserDAOMock()
        self.user = user_register

    def test_is_username_unique(self):
        self.assertEqual(is_username_unique(self.user, self.user_dao), False)

        self.user_dao.username_query_res = None
        self.assertEqual(is_username_unique(self.user, self.user_dao), True)

    def test_is_email_unique(self):
        self.assertEqual(is_email_unique(self.user, self.user_dao), False)

        self.user_dao.email_query_res = None
        self.assertEqual(is_email_unique(self.user, self.user_dao), True)

    def test_is_unique(self):
        self.assertEqual(is_unique(FormMock(), self.user, self.user_dao),
                         False)

        self.user_dao.username_query_res = None
        self.user_dao.email_query_res = None
        self.assertEqual(is_unique(FormMock(), self.user, self.user_dao), True)
