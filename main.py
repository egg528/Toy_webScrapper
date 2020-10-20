import requests

indeed_resul = requests.get\
    ("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=021703718563a5b3")

print((indeed_resul.text))
