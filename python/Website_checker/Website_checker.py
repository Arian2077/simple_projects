import csv
import requests
from http import HTTPStatus
from fake_useragent import UserAgent


class WebsiteChecker:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.user_agent = self.get_user_agent()

    def get_websites(self) -> list[str]:
        """Loads websites from a csv file"""
        websites: list[str] = []
        with open(self.csv_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if 'https://' not in row[1] or 'http://' not in row[1]:
                    websites.append(f'https://{row[1]}')
                else:
                    websites.append(row[1])
        return websites

    @staticmethod
    def get_user_agent() -> str:
        """Returns a user agent that can be used with requests"""
        ua = UserAgent()
        return ua.chrome

    @staticmethod
    def get_status_description(status_code: int) -> str:
        """Uses the status code to return a readable description"""
        for value in HTTPStatus:
            if value == status_code:
                description: str = f'({value} {value.name}) {value.description}'
                return description
        return '(???) Unknown status code...'

    def check_website(self, website: str):
        """Gets the status code for a website and prints the result"""
        try:
            code: int = requests.get(website, headers={'User-Agent': self.user_agent}).status_code
            print(website, self.get_status_description(code))
        except Exception:
            print(f'**Could not get information for website: "{website}"')

    def run(self):
        """Main method to check all websites"""
        sites: list[str] = self.get_websites()
        for site in sites:
            self.check_website(site)


if __name__ == '__main__':
    checker = WebsiteChecker('Website_checker/websites.csv')
    checker.run()