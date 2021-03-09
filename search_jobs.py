import requests, colorama, csv
from bs4 import BeautifulSoup as soup


def write_data(data):
    with open(f'jobs_in_{place}.csv', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows([data])


def scrape_contents(locator):
    my_data = []
    # Topcard scraping
    for content in locator.findAll('div', {'class':'topcard__content-left'})[0:]:
        for title in content.findAll('h1', {'class':'topcard__title'})[0:]:
            print(colorama.Fore.GREEN,
               f'[*] {title.text}', colorama.Style.RESET_ALL)
            my_data.append(title.text.replace(',','.'))
        for location in content.findAll('span', {'class':'topcard__flavor topcard__flavor--bullet'})[0:]:
            my_data.append(location.text.replace(',','.'))

    # Criteria scraping
    for criteria in locator.findAll('span', {'class':'job-criteria__text job-criteria__text--criteria'})[:4]:
        my_data.append(criteria.text)

    write_data(my_data)


def parse_job_page(links):
    try:
        print(colorama.Fore.YELLOW,
            f'[!] There are {len(links)} available jobs.\n',
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


def web_parsing(location):    
    with open(f'jobs_in_{location}.csv', 'w', encoding='utf-8') as f:
        headers = ['Job Title', 'Location', 'Seniority Level',
                   'Employment Type', 'Job Function', 'Industries']
        write = csv.writer(f)
        write.writerow(headers)
    try:
        req = requests.get(
            f'https://www.linkedin.com/jobs/jobs-in-{location}?trk=homepage-basic_intent-module-jobs&position=1&pageNum=0')
        req.raise_for_status()

        # create beautifulsoup
        page_soup = soup(req.text, 'html.parser')
        extract_jobs(page_soup)
    except requests.HTTPError as err:
        print(colorama.Fore.RED,
            f'[!!] Something went wrong! {err}', colorama.Style.RESET_ALL)


if __name__ == '__main__':
    colorama.init()

    place = str(input('Enter country/city/state: '))
    web_parsing(place)