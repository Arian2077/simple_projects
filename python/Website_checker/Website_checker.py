import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
            
        return websites
    
def get_user_agent() -> str:
    user_agent = UserAgent()
    return user_agent.chrome


def get_status_description(url: int) -> str:
    for value in HTTPStatus:
        if value == url:
            description: str = f'({value} {value.name}) {value.description}'
            return description
        
    return '(???) Unknown status code...'

def check_website_status(websites:str , user_agent):
    try:
        code:int = requests.get(websites, headers={'User-Agent': user_agent}).status_code
        print(websites,get_status_description(code)) 
    except Exception:
        print(websites, 'Error: Unable to connect to the website.')