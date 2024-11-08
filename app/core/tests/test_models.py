"""
Tests for models.
"""
from unittest.mock import patch
from decimal import Decimal
import os

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def create_user(email='user@example.com', password='testpass123'):
    """Create and return a new user"""
    return get_user_model().objects.create_user(email,password)

class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email='test@example.com'
        password='testpass123'
        user=get_user_model().objects.create_user(email=email,password=password)
        
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password,password)

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails=[['test1@EXAMPLE.com','test1@example.com'],
                       ['Test2@Example.com','Test2@example.com'],
                       ['TEST3@EXAMPLE.COM','TEST3@example.com'],
                       ['test4@example.COM','test4@example.com'],
        ]

        for email,excepted in sample_emails:
            user=get_user_model().objects.create_user(email,'sample123')
            self.assertEqual(user.email,excepted)


    def test_new_user_wihout_email_raises_error(self):
        """Test that creating without email raises a Value error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','test123') 

    def test_create_superuser(self):
        """test creating a super user"""
        user= get_user_model().objects.create_superuser('test@eample.com','test123',)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)



    def test_create_book(self):
        """Test creating a book is successful"""
        user=get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        book=models.Book.objects.create(
            user=user,
            book_name='Sample book name',
            author_name='Sample author name',
            genre='Sample book genre',
        )

        self.assertEqual(str(book),book.book_name)