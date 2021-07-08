import bs4
import requests

file_name = 'curs5-homework-file.txt'


def write_in_file(title, content):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(title.find('a').text.strip())
        file.write('\n')
        file.write(content)
        file.write('\n')
        file.write('\n')
        file.write('\n')


def take_content(URL, index):
    contents = ""
    global titles

    page = requests.get(URL)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')

    content = soup.find_all(class_="td-post-content")
    for i in content:
        if i.find('p') is None:
            # titles.pop(index)
            continue
        contents += i.find('p').text

    write_in_file(titles[index], contents)


URL = 'http://frsah.ro/'
page = requests.get(URL)
soup = bs4.BeautifulSoup(page.content, 'html.parser')

titles = soup.find_all(class_="item-details")
sites = soup.find_all()
# contents = soup.find_all("div", {"class": "td-excerpt"})
contents = []

for i in range(len(titles)):
    print(len(titles))

    take_content(titles[i].find('a').get('href'), i)
    #file.write(titles[i].find('a').text.strip())
    ##file.write('\n')
    ###file.write(contents[i])
    ###file.write('\n')
    ##print(titles[i].find('a').text.strip)
    #print(contents[i])

print(len(titles))
print(len(contents))

