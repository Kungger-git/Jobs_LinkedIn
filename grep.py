import requests, colorama
from bs4 import BeautifulSoup as soup


def scrape_contents(locator):
    for content in locator.findAll('div', {'class':'topcard__content-left'})[0:]:
        for title in content.findAll('h1', {'class':'topcard__title'})[0:]:
            print(colorama.Fore.GREEN,
                f'[*] {title.text}', colorama.Style.RESET_ALL)


def parse_job_page(links):
    try:
        print(colorama.Fore.YELLOW,
            f'[!] There are {len(links)} available jobs.',
            colorama.Style.RESET_ALL)
        for job_link in links:
            job_req = requests.get(job_link)
            job_req.raise_for_status()
            
            # Parse HTML
            job_soup = soup(job_req.text, 'html.parser')
            scrape_contents(job_soup)
    except requests.HTTPError as err:
        print(colorama.Fore.RED,
            f'[!!] Something went wrong! {err}', colorama.Style.RESET_ALL)


def extract_jobs(cursor):
    job_links = []
    for res_card in cursor.findAll("li", {"class":"result-card"})[0:]:
        for links in res_card.findAll('a', {'class':'result-card__full-card-link'})[0:]:
            job_links.append(links['href'])
    parse_job_page(job_links)


def web_parsing():
    country = str(input('Enter your country/city: '))
    try:
        req = requests.get(
            f'https://www.linkedin.com/jobs/jobs-in-{country}?trk=homepage-basic_intent-module-jobs&position=1&pageNum=0')
        req.raise_for_status()

        # create beautifulsoup
        page_soup = soup(req.text, 'html.parser')
        extract_jobs(page_soup)
    except requests.HTTPError as err:
        print(colorama.Fore.RED,
            f'[!!] Something went wrong! {err}', colorama.Style.RESET_ALL)


if __name__ == '__main__':
    colorama.init()
    web_parsing()