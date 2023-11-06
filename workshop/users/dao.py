from dataclasses import dataclass

from django.contrib.auth.models import User

from .services.auth_service.domain import UserRegisterDTO


@dataclass
class UserEntity:
    id: int
    username: str
    email: str


class UserDAO:
    def _orm_to_entity(self, user_obj: User):
        return UserEntity(
            id=user_obj.id,
            username=user_obj.username,
            email=user_obj.email,
        )

    def filter_by_username(self, username: str) -> list[UserEntity] | None:
        result = User.objects.filter(username=username)

        if result:
            return list(map(self._orm_to_entity, result))
        return None

    def filter_by_email(self, email: str) -> list[UserEntity] | None:
        result = User.objects.filter(email=email)

        if result:
            return list(map(self._orm_to_entity, result))
        return None

    def create_user(self, user: UserRegisterDTO) -> User:
        user_obj = User.objects.create_user(
            username=user.username,
            email=user.email,
            password=user.password,
        )
        user_obj.save()
        return user_obj
