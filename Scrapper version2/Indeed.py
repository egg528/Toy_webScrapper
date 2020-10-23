import requests
# 이 라이브러리는 페이지를 가져올 수 있다.
from bs4 import BeautifulSoup
# 이 라이브러리는 페이지에서 특정 요소를 분리해낼 수 있다.

LIMIT= 50

def get_last_pages(url):
    indeed_result=requests.get(url)
    indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")
    pagination = indeed_soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_pages = pages[-1]
    return max_pages

def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]

    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company.anchor == None:
        company = str(company.string)
    else:
        company = str(company.find("a").string)
    company = company.strip()

    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]

    job_id = html['data-jk']
    return  {'title': title, 'company': company, 'location': location, 'link': f'https://kr.indeed.com/viewjob?jk={job_id}&tk=1el4d5dnj37av000&from=serp&vjs=3'}




def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed page: {page+1}")
        result = requests.get(f"{url}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    url = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch"
    last_page = get_last_pages(url)
    jobs = extract_jobs(1, url)
    return jobs



