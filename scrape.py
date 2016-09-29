from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

csv_file = open("email_list.csv", "w")
url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com/" + link ["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        print person_soup.find("div", attrs={"class" : "row"}).find("h1").string
        print person_soup.find("span", attrs={"class" : "email"}).string
        print person_soup.find("span", attrs={"data-city" : True}).string
        name = person_soup.find("div", attrs={"class" : "row"}).find("h1").string
        email = person_soup.find("span", attrs={"class" : "email"}).string
        city = person_soup.find("span", attrs={"data-city" : True}).string
        csv_file.write(name + ";" + email + ";" + city + "\n")

csv_file.close()
