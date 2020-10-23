import requests
# 이 라이브러리는 페이지를 가져올 수 있다.
from bs4 import BeautifulSoup
# 이 라이브러리는 페이지에서 특정 요소를 분리해낼 수 있다.


def get_last_pages(url):
    stackoverflow_result = requests.get(url)
    stackoverflow_soup = BeautifulSoup(stackoverflow_result.text,"html.parser")
    pages = stackoverflow_soup.find("div", {"class": 's-pagination'}).find_all('a')
    last_pages = pages[-2].get_text(strip=True)
    return int(last_pages)




def extract_job(html):
    title = html.find('a', {'class': 'stretched-link'}).get_text()
    company, location = html.find('h3', {'class': 'fc-black-700'}).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    link = html['data-preview-url']
    return {'title': title, "company": company, "location": location, 'link': f'https://stackoverflow.com{link}'}





def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SOF page: {page+1}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")

        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}"
    last_page = get_last_pages(url)
    jobs = extract_jobs(1, url)
    return jobs
