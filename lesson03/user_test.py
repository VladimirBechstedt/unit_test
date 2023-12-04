import unittest
from user import User
from user_repository import UserRepository


class UserTest(unittest.TestCase):
    def test_user_logout_test(self):
        repository = UserRepository()
        repository.add_user(User("user1", "1111", True))
        repository.add_user(User("user2", "2222", False))
        repository.add_user(User("user3", "3333", True))
        repository.all_users_logout()
        for user in repository.users:
            self.assertTrue(user.admin)
