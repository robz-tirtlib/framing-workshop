from django.test import TestCase
from django.test.client import RequestFactory

from users.services.user_profile_service.infrastructure import (
    get_user_from_request, get_response
)
from users.tests.materials import (
    user_dto, NotAuthenticatedUserMock, AuthenticatedUserMock)


class ProfileInfrastructureTestCase(TestCase):
    def setUp(self):
        self.request = RequestFactory()

    def test_get_user_from_request(self):
        self.request.user = NotAuthenticatedUserMock
        self.assertIs(get_user_from_request(self.request), None)

        self.request.user = AuthenticatedUserMock
        user = user_dto
        self.assertEqual(get_user_from_request(self.request), user)

    def test_get_response(self):
        self.request.user = NotAuthenticatedUserMock
        self.assertEquals(get_response(self.request, None, 2).status_code, 403)

        self.request.user = AuthenticatedUserMock
        response = get_response(self.request, self.request.user, 2)
        self.assertEquals(response.status_code, 403)

        response = get_response(self.request, self.request.user, 1)
        self.assertEquals(response.status_code, 200)
