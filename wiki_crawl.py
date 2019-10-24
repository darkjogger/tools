import requests
import time
from bs4 import BeautifulSoup
try:
    from urlparse import urljoin  # Python2
except ImportError:
    from urllib.parse import urljoin  # Python3


def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    article_link = None
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    if article_link:
        return article_link
    else:
        print("Enter a deadend, program quits!")
        quit()


def continue_crawl(search_history, target_url, max_step=25):
    curr_url = search_history[-1]
    if search_history.count(curr_url) == 2:
        print("Enter a loop, failed to find the target. search stops!")
        return False
    if len(search_history) > max_step:
        print("Go throught 25 pages without reaching target. search stops!")
        return False
    if curr_url == target_url:
        print("Find target!!! search stops.")
        return False
    else:
        print("Continue searching!")
        return True


def web_crawl():
    print("pls enter a correct wiki url, or this program will start from a random wiki url.")
    start_url = input("where do you start?  ")
    if "en.wikipedia.org/wiki/" not in start_url:
        print("Wrong input, the program will start with a random wiki url.")
        start_url = "https://en.wikipedia.org/wiki/Special:Random"

    max_step = input("How many websites do you want go throught?    ")
    try:
        max_step = int(max_step)
    except ValueError:
        print("You should enter a integer.")
        quit()

    article_chain = [start_url]
    target_url = "https://en.wikipedia.org/wiki/Philosophy"
    print(start_url)

    while continue_crawl(article_chain, target_url, max_step):
        # download html of last article in article_chain
        # find the first link in that html
        article_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        first_link = urljoin('https://en.wikipedia.org/', article_link)
        article_chain.append(first_link)
        print(article_chain[-1])
        # delay for about two seconds
        time.sleep(1)


if __name__ == "__main__":
    web_crawl()
