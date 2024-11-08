"""
Django command to wait for the database to be available
"""

import time
from typing import Any
from psycopg2 import OperationalError as Psycopg20pError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database """
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except(Psycopg20pError,OperationalError):
                self.stdout.write('Database Unavailabe, waiting 1 sec...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Successful'))

