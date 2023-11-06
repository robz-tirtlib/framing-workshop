from users.services.auth_service.domain import UserRegisterDTO

from users.dao import UserEntity


user1 = UserEntity(
    id=1,
    username="user1",
    email="user1@mail.ru",
)

user_register = UserRegisterDTO(
    username="user1",
    email="user1@mail.ru",
    password="password1",
)


class UserDAOMock:
    def __init__(self):
        self.email_query_res = [user1]
        self.username_query_res = [user1]

    def filter_by_email(self, _):
        return self.email_query_res

    def filter_by_username(self, _):
        return self.username_query_res


class FormMock:
    def add_error(self, _, __):
        return
