from dataclasses import dataclass


@dataclass
class UserRegisterDTO:
    username: str
    email: str
    password: str


@dataclass
class UserLoginDTO:
    username: str
    password: str
