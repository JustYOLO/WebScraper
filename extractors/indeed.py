from bs4 import BeautifulSoup
from selenium import webdriver

def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="

    browser = webdriver.Chrome()
    browser.get(f"{base_url}{keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", attrs={'aria-label': "pagination"})
    buttons = pagination.find_all("div")
    count = len(buttons)
    browser.close()
    if count >= 5:
        return 5
    elif count == 0:
        return 1
    else:
        return count
    

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    base_url = "https://kr.indeed.com/jobs"
    results = []

    for page in range(pages):
        browser = webdriver.Chrome()
        browser.get(f"{base_url}?q={keyword}&start={page*10}")

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li', recursive=False) # recursive=False means returns only the children dir of the element
        for job in jobs:
            zone = job.find('div', class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a") # search h2 -> search a from the result
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                results.append({
                'Company': company.string.replace(",    ", " "),
                'Position': title.replace(",", " "),
                'Location': location.string.replace(",", " "),
                'URL': f"https://kr.indeed.com{link}",
                })
        browser.close()
    return results