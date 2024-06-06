"""Define custom model for user accounts.
"""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomAccountManager


class CustomAccount(AbstractBaseUser, PermissionsMixin):
    """
    An account model customed from scratch to hold a user's details.
    An account is specified according to types: home,
    home_member (individual belonging to a house) and the superaccount.
    """

    choices = (  # index 0 for django, index 1 for the database
        ('HOME', 'home'),
        ('HOUSE_MEMBER', 'house_member'),
        ('ADMIN', 'admin'),
    )

    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(
        max_length=50,
        blank=False,
        help_text="identifier of the home, individual user, or admin"
    )
    type = models.CharField(choices=choices, blank=False, max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # password and last_login are inherited fields from AbstractBaseUser

    normal_monthly_expense = models.PositiveIntegerField(
        help_text="The total expense figure you normally reach for the month.",
        blank=True,
    )
    budget = models.PositiveSmallIntegerField(blank=True)
    amount_spent = models.PositiveSmallIntegerField(default=0)
    total_savings = models.PositiveSmallIntegerField(default=0)
    savings_spent = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['password', 'name', 'type']

    objects = CustomAccountManager()

    def __str__(self):
        # already a string - only done to get rid of warning
        return str(self.email)
