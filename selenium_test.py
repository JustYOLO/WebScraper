from bs4 import BeautifulSoup
from selenium import webdriver
from separater import linecut

def indeed(pages = 1):
    base_url = "https://kr.indeed.com/jobs?q="
    keyword = "python"
    results = []

    for i in range(pages):
        browser = webdriver.Chrome() # selenium setting
        browser.get(f"{base_url}{keyword}&start={i*10}") # get the webpage's info

        soup = BeautifulSoup(browser.page_source, "html.parser") # get the html code to bs
        job_lists = soup.find("ul", class_ = "jobsearch-ResultsList") # find the <ul> that contains job information
        jobs = job_lists.find_all("li") # these li contains job infos
        for job in jobs:
            zone = job.find("div", class_ = "result") # some of the li doesn't have job infos. 
            if zone != None: # if the tag have<div, class="result" ... this tag doesn't contains job infos
                contents = zone.find("td", class_ = "resultContent") # these tag contains job infos
                anchor = contents.select_one("h2 a") # h2's children tag <a> have the title & links
                title = anchor["aria-label"] # title
                link = "https://kr.indeed.com" + anchor["href"] # href
                company = contents.find("span", class_ = "companyName")
                location = contents.find("div", class_ = "companyLocation")
                
                results.append({
                    "title": title,
                    "link": link,
                    "company": company.string,
                    "location": location.string
                })
        browser.close()

    for job in results:
        print(job)
        linecut()
    print(len(results))

indeed(2)