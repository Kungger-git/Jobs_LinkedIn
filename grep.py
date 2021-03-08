import requests, colorama
from bs4 import BeautifulSoup as soup


def extract(cursor):
    for res_card in cursor.findAll("div", {"class":"result-card__contents"})[0:]:
        print(res_card.text)


def web_parsing():
    country = str(input('Enter your country/city: '))
    try:
        req = requests.get(
            f'https://www.linkedin.com/jobs/jobs-in-{country}?trk=homepage-basic_intent-module-jobs&position=1&pageNum=0', timeout=1)
        req.raise_for_status()

        # create beautifulsoup
        page_soup = soup(req.text, 'html.parser')
        extract(page_soup)
    except requests.HTTPError as err:
        print(colorama.Fore.RED,
            f'[!!] Something went wrong! {err}', colorama.Style.RESET_ALL)

if __name__ == '__main__':
    colorama.init()
    web_parsing()