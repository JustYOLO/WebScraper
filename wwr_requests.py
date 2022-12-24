from requests import get # to get the website data (in html)
from bs4 import BeautifulSoup # to organize website data

base_url = "https://weworkremotely.com/remote-jobs/search?term=" # data url
search_term = "python" # type of language

response = get(f"{base_url}{search_term}") # get data from url. (response is a object, not a string)

if response.status_code != 200: #Code 200 means the request is successful
    print("Can't request website")
else:
    job_list = [] # save jobs in this list using dic
    soup = BeautifulSoup(response.text, "html.parser") # .text gets the html data from the website
    jobs = soup.find_all('section', class_ = 'jobs') # search jobs in the website. ex) <section class="jobs">
    for section in jobs: # search jobs from different selections
        job_posts = section.find_all('li', class_ = lambda x: x != "view-all") #exclude "view-all" button
        for job in job_posts:
            anchors = job.find_all('a')
            anchor = anchors[1] # <div class="tooltip"> is not needed
            link = anchor['href'] # get the link (hypertext)
            company, kind, region = anchor.find_all("span", class_ = "company") # get company, kind and region from span tag
            title = anchor.find("span", class_ = "title") # important! find_all returns list-like object, so if u use find_all: you cannot use .string
            job_list.append({'company': company.string, 'region': region.string, 'title': title.string, 'link': f"https://weworkremotely.com{link}"})

for job in job_list:
    print(job)
    print("\n/////////////////////")