# 알바천국 job scraper 22.12.25
from requests import get
from bs4 import BeautifulSoup
from etc import linecut

def get_albaheaven_jobs():
    results = [] 

    target_url = "http://www.alba.co.kr/job/area/mainlocal.asp?schnm=LOCAL&viewtype=L&sidocd=044&hidSort=FREEORDER&hidListView=LIST&hidSortCnt=50&hidSortFilter=Y&hidSearchyn=Y&workperiodcd=H02&workperiodcd=H03&workperiodcd=H04"
    base_url = "http://www.alba.co.kr/"

    webdriver = get(target_url)
    soup = BeautifulSoup(webdriver.text, "html.parser")
    content = soup.find("div", id="NormalInfo", class_="goodsList")
    jobs = soup.find_all("tr", class_ = lambda x: x != "summaryView")
    jobs.pop(0)
    for job in jobs:
        location = job.select_one("td").get_text()
        
        class_title = job.find("td", class_="title")
        anchor = class_title.select_one("a")
        link = base_url + anchor['href']
        company = anchor.find("span", class_="company").string
        title = anchor.find("span", class_="title").string

        time = job.find("td", class_="data").get_text()
        results.append({"Location": location, "Company": company, "link": link, "Title": title, "Time": time})
    return results