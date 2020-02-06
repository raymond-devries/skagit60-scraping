from scrapers import scraper_modules as sm
from bs4 import BeautifulSoup
import pandas as pd

wta_link = 'https://www.wta.org/go-outside/hikes?b_start:int='


def get_list_of_peak_info(html: str):
    html_soup = BeautifulSoup(html, 'html.parser')
    a_tags = html_soup.find_all('a', attrs={'class': 'listitem-title'})
    return a_tags


def create_list_of_links():
    list_of_links = []
    i = 0
    while i < 3721:
        list_of_links.append(wta_link + str(i))
        i += 30
    return list_of_links


def create_csv():
    links = create_list_of_links()
    a_tags = []
    for link in links:
        html = sm.download_html(link)
        a_tags = a_tags + get_list_of_peak_info(html)
        print(link)

    peaks_dict = sm.create_peaks_dict(a_tags, 'span', title_retrieval_method='find')
    df = pd.DataFrame(peaks_dict)
    df.to_csv('raw_data/wta_data.csv', index=False)


if __name__ == '__main__':
    create_csv()
