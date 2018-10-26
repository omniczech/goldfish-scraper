from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv

browser = webdriver.Chrome()

browser.get('https://www.mtggoldfish.com/tournament/pauper-challenge-11659820#paper')

elem = browser.find_element_by_class_name('tournament-decklist-collapse')  # Find the search box
elem.click()
page = browser.find_element_by_class_name('container-fluid')
time.sleep(5)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup.title)
tables = soup.select('.tab-pane.active .deck-view-deck-table')
results = []
for table in tables:
    # tablesoup = BeautifulSoup(table, 'html.parser')
    trs = table.select('tr')
    deck = []
    for tr in trs:
        quantity = tr.select('.deck-col-qty')
        card_names = tr.select('.deck-col-card')
        card_quantity = 0
        card_name = ""
        for quant in quantity:
            # print(quant.text)
            card_quantity=int(quant.text)
        for name in card_names:
            card_name = name.text.replace('\n','')
        for x in range(0, card_quantity):
            deck.append(card_name)
        # print(card_quantity, card_name)
    results.append(deck)
print(results, len(results))
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(results)
# for link in links:
#     print link
# lists = []
# lists = browser.find_elements_by_class_name('deck-view-deck-table')
# print lists
#
# for list in lists:
#     print list.get_attribute('innerHTML')


browser.quit()
