# albamon.com WebScraper 22.12.25
from bs4 import BeautifulSoup
from selenium import webdriver
from etc import linecut, strClean

def get_albamon_jobs():
    target_url = "https://www.albamon.com/recruit/area?rArea=,1000&sDutyTerm=,10,20,30&rWDate=1"
    results = []

    browser = webdriver.Chrome()
    browser.get(target_url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_wrap = soup.find("div", class_="gListWrap")
    job_list = job_wrap.find("tbody")
    jobs = job_list.find_all("tr")

    for job in jobs:
        area = job.select_one("div")
        location = strClean(area.get_text(), "스크랩")  # to delete unnecessary char
        cName = job.find("p", class_="cName")  # <cName> contains company & links
        anchor = cName.select_one("a")
        company = anchor.string
        link = anchor['href']  # extract link & company
        title = job.find("p", class_="cTit")  # cTit contains title
        anchor = title.select_one("a")
        title = anchor.string  # extract title
        time = job.find_all("td")
        time = strClean(time[-2].string)

        results.append({"Location": location, "Company": company, "link": link, "Title": title, "Time": time})
    return results