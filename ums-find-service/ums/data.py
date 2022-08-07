from abc import ABC, abstractmethod
from mysql.connector import connect, Error


class UserRepository(ABC):
    @abstractmethod
    def fetch(self, name: Name) -> User:
        pass


def UserNotFoundException(Exception):
    pass


class UserRepositoryImpl(UserRepository):
    def fetch(self, name: Name) -> User:
        try:
            with connect(
                host="mysqldb",
                user="root",
                password="admin",
                database="glarimy",
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM ums_users where name=%s", (name.value, ))
                    row = cursor.fetchone()
                    if cursor.rowcount == -1:
                        raise UserNotFoundException()
                    else:
                        return User(Name(row[0]), PhoneNumber(row[1]), row[2])

        except Error as e:
            raise e
