import time

from bs4 import BeautifulSoup
from requests import get

from plugins.send_messages import send_messages_to_users


def get_page(url):
    """
    Get the page from a given url
    :param url: url of the page
    :return: the response text
    """
    return get(url).text


def extract_data(page):
    """
    Extract data from the page
    :param page: the response text
    :return: the data
    """
    soup = BeautifulSoup(page, 'html.parser')
    main_div = soup.css.select_one('html body.archive.post-type-archive.post-type-archive-tour > div:nth-of-type(3) div')
    no_tour = main_div.css.select_one("div:nth-child(2) p:nth-child(2)")
    if no_tour is not None and no_tour.text == "No Tour Dates right now":
        return None
    
    tours = main_div.select("div:first-child>div:not(:first-child)")
    data = []
    for tour in tours:
        date = tour.css.select_one(":nth-child(1)").text.strip()
        location = tour.css.select_one(":nth-child(2)").text.strip()
        venue = tour.css.select_one(":nth-child(3)").text.strip()
        purchase_link = tour.css.select_one(":nth-child(4) > a")['href']
        data.append({
            'date': date,
            'location': location,
            'venue': venue,
            'purchase_link': purchase_link
        })
    return data


def get_tour_info():
    """
    Get the tour info from the website
    :return: the tour info
    """
    url = "https://www.acdc.com/tour/"
    page = get_page(url)
    tours = extract_data(page)
    if tours is None:
        return
    send_messages_to_users(tours)


def start():
    time.sleep(5)
    while 1:
        get_tour_info()
        time.sleep(120)
