import datetime


class UserBaseException(Exception):
    ...


class UserFullNameException(UserBaseException):
    ...


class UserDateException(UserBaseException):
    ...


class UserPhoneException(UserBaseException):
    ...


class User:
    def __init__(self,
                 full_name: str,
                 date: datetime.datetime,
                 phone: str):
        if not isinstance(full_name, str):
            raise UserFullNameException("Имя пользователя должно иметь тип str")
        self.full_name = full_name
        self.date = date
        self.phone = phone

    def add_full_name_str(self, st: str):
        self.full_name += st

try:
    full_name = 123
    user = User(full_name, 345, 675)
except UserFullNameException:
    user = User(str(full_name), 345, 675)
print(user)
user.add_full_name_str('asdgf')