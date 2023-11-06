from users.services.user_profile_service.domain import UserDTO


user_id = 1
username = "some_username"
email = "someemail@mail.ru"
password = "somepassword123"

user_dto = UserDTO(
            id=user_id,
            username=username,
            email=email,
            password=password,
            )


class NotAuthenticatedUserMock:
    is_authenticated = False


class AuthenticatedUserMock:
    is_authenticated = True
    id = user_id
    username = username
    email = email
    password = password
