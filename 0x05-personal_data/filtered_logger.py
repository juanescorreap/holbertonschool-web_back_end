#!/usr/bin/env python3
"""
Class containing methods to format personal data in a way that is safe
"""
from typing import List
import re
import logging
import os
import mysql.connector
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        "Class constructor"
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Method to filter values in incoming log
        records using filter_datum
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function called filter_datum that returns the log
    message obfuscated
    """
    for field in fields:
        message = re.sub(fr'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}',
                         message)
    return message


def get_logger() -> logging.Logger:
    """
    Function that takes no arguments and returns a
    logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(RedactingFormatter(PII_FIELDS)))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Function that returns a connector to the database
    """
    mydb = mysql.connector.connect(
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''))
    return mydb


def main():
    """
    Function will obtain a database connection using
    get_db and retrieve all rows in the users table
    and display each row under a filtered format
    """
    database_connection = get_db()
    cursor = database_connection.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        message = ""
        for key in row:
            message = message + "{}={}; ".format(key, row[key])
        print(message)
    cursor.close()
    database_connection.close()


if __name__ == "__main__":
    main()
