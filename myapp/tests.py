from django.test import TestCase
import json

def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file)
    except TypeError as err:
        raise err
    except IOError as err:
        raise err

def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError as err:
        raise err
    except IOError as err:
        raise err
# Create your tests here.
test_data = {
    'pk': 4,
    'title': 'Test Title',
    'published_date': '2024-06-23',
    'publisher': 6,
    'price': 9.99,
    'discounted_price': 3.56,
    'is_bestseller': True,
    'is_banned': False,
    'genres': [1, ]
}