"""Defines an `account model` custom manager for interacting with the database
"""
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    """
    An account model manager customed to use email as the unique identifier
    for authentication instead of usernames.
    """

    def create_account(self, email, password, **extra_fields):
        """
        Create and save a new home account with the given arguments.
        The `email`, `passsword`, and `name` are required.
        """
        if not email:
            raise ValueError(_('The Email must be set.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superaccount(self, email, password, **extra_fields):
        """
        Create and save a new super account with the given arguments.
        The `email`, `passsword`, and `homename` are required.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superaccount", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superaccount must have is_staff=True."))
        if extra_fields.get("is_superaccount") is not True:
            raise ValueError(_("Superaccount must have is_Superaccount=True."))

        return self.create_account(email, password, **extra_fields)
