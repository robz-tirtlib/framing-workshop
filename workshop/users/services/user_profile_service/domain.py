from dataclasses import dataclass


@dataclass
class UserDTO:
    id: int
    username: str
    email: str
    password: str


def is_user_allowed(user: UserDTO | None, profile_id: int) -> bool:
    if user is None or profile_id != user.id:
        return False

    return True
