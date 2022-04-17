import requests
from bs4 import BeautifulSoup

f_scriere = open('evenimente_sah.txt', 'w', encoding="utf-8")
f_citire = open('evenimente_sah.txt', 'r', encoding="utf-8")

URL = "https://frsah.ro/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

stage_table = soup.find(class_="tribe-events-calendar-month")
event_rows = stage_table.find_all(class_="tribe-events-calendar-month__calendar-event-tooltip-title")
events = []
for event in event_rows:
    event_cell = event.find("a")
    event_name = event_cell.text.strip()
    events.append(event_name)


for e in events:
    f_scriere.write(e)
    f_scriere.write("\n")


f_scriere.close()

print(f_citire.read())
