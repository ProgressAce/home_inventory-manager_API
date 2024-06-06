"""Tests defined for the accounts app."""
from django.contrib.auth import get_user_model
from django.test import TestCase


class HomeAccountsManagersTests(TestCase):
    """Tests for the `account` model's manager (database interacting object)"""

    def test_create_account(self):
        """Ensure that `create_account` method creates a new user."""
        HomeAccount = get_user_model()
        home_account = HomeAccount.objects.create_account(
            email="normal@user.com", password="jojo"
        )
        self.assertEqual(home_account.email, "normal@user.com")
        self.assertTrue(home_account.is_active)
        self.assertFalse(home_account.is_staff)
        self.assertFalse(home_account.is_superaccount)
        try:
            # username does not exist as AbstractBaseUser class is inherited
            self.assertIsNone(home_account.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            HomeAccount.objects.create_account()
        with self.assertRaises(TypeError):
            HomeAccount.objects.create_account(email="")
        with self.assertRaises(ValueError):
            HomeAccount.objects.create_account(email="", password="dynamite")

    def test_create_superaccount(self):
        """Ensure that `create_account` method creates a new super user."""
        HomeAccount = get_user_model()
        admin_account = HomeAccount.objects.create_account(
            email="super@user.com", password="jojo"
        )
        self.assertEqual(admin_account.email, "normal@user.com")
        self.assertTrue(admin_account.is_active)
        self.assertTrue(admin_account.is_staff)
        self.assertTrue(admin_account.is_superaccount)
        try:
            # username does not exist as AbstractBaseUser class is inherited
            self.assertIsNone(admin_account.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            HomeAccount.objects.create_superaccount(
                email="super@user", password="dynamite", is_superaccount=False
            )
