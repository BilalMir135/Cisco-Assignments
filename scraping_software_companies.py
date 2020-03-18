import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.goodfirms.co/directory/country/top-software-development-companies/pakistan")
soup = BeautifulSoup(page.content,'html.parser')

data={
    "Names":["Cubix"],
    "Websites":[],
    "Hourly Rates":[],
    "Employees":[],
    "Cities":[],
    "Countries":[]
}

content = soup.find(class_="directory-content").find_all(class_="company-profile directory-page")
for i in range(1,len(content)):
    data["Names"].append(content[i].find(class_="c_name_head detail_page").get_text())

content = (soup.find(class_="directory-content")).find_all(class_="firms-r")
for i in range(len(content)):
    data["Websites"].append(content[i].find(class_="visit-website block default-blue-btn c_visit_website")["href"])
    data["Hourly Rates"].append(content[i].find(class_="firm-pricing").get_text())
    data["Employees"].append(content[i].find(class_="firm-employees").get_text())
    temp=(content[i].find(class_="firm-location").get_text()).split(',')
    data["Cities"].append(temp[0][1:])
    data["Countries"].append(temp[1][1:])

pd.DataFrame(data).to_csv("Software Companies.csv")