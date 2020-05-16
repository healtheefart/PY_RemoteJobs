import requests
from bs4 import BeautifulSoup


def so_scrapper(SO_url):
  result = requests.get(SO_url)
  soup = BeautifulSoup(result.text, "html.parser")
  title_list = soup.find_all("h2", {"class": "mb4 fc-black-800 fs-body3"})
  company_list = soup.find_all("h3", {"class":"fc-black-700 fs-body1 mb4"})
  so_list = []
  for i in range(len(title_list)):
    title = title_list[i].find("a")["title"]
    company = company_list[i].find("span").get_text().strip().replace("\n","").replace("\r","")
    link_yet = title_list[i].find("a")["href"]
    link = f"https://stackoverflow.com{link_yet}"
    so_list.append({"title":title, "company":company, "link":link})
  return so_list

def wwr_scrapper(WWR_url):
  result = requests.get(WWR_url)
  soup = BeautifulSoup(result.text, "html.parser")
  all_job = soup.find_all("li",{"class":"feature"})
  wwr_list = []
  for i in range(len(all_job)):
    common = all_job[i].find_all("a")
    try:
      title = common[1].find("span",{"class":"title"}).get_text()
    except:
      title = "None"
    try:
      company = common[1].find("span",{"class":"company"}).get_text()
    except:
      company = "None"
    try:
      link_yet = common[1]["href"]
      link = f"https://weworkremotely.com{link_yet}"
    except:
      link = "None"
    wwr_list.append({"title":title, "company":company, "link":link})
  return wwr_list

  
def ro_scrapper(RO_url):
  result = requests.get(RO_url)
  soup = BeautifulSoup(result.text, "html.parser")
  title_list = soup.find_all("h2", {"itemprop": "title"})
  company_list = soup.find_all("h3", {"itemprop":"name"})
  link_list = soup.find_all("a",{"itemprop":"url"})
  ro_list = []
  for i in range(len(title_list)):
    title = title_list[i].get_text()
    company = company_list[i].get_text()
    link_yet = link_list[i]["href"]
    link = f"https://remoteok.io{link_yet}"
    ro_list.append({"title":title, "company":company, "link":link})
  return ro_list