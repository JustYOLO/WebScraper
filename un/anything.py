# albamon.com WebScraper 22.12.25

from requests import get

target_url="https://www.albamon.com/recruit/area?rArea=,1000&sDutyTerm=,10,20,30&rWDate=1"

response = get(target_url)
print(response.status_code)