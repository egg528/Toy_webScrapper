import requests
# 이 라이브러리는 페이지를 가져올 수 있다.
from bs4 import BeautifulSoup
# 이 라이브러리는 페이지에서 특정 요소를 분리해낼 수 있다.

LIMIT= 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch"




def extract_indeed_pages():
    indeed_result=requests.get(URL)

    indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

    pagination = indeed_soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_pages = pages[-1]
    
    return max_pages


