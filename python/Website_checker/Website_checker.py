import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' in row[1]:
                websites.append(f'http://{row[0]}')