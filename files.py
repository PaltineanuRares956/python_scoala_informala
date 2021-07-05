# with open('my_file.txt', 'w') as file:
#   file.write('Hello!')

import csv

with open('cars.csv', 'r') as csv_file:
    rows = csv.reader(csv_file, delimiter=',')

    for row in rows:
        print(row)


import requests
from bs4 import BeautifulSoup
