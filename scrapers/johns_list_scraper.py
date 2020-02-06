from scrapers import scraper_modules as sm
import pandas as pd
from bs4 import BeautifulSoup


link = 'https://listsofjohn.com/PeakStats/select.php?R=P&sort=&P=0&S=WA'


def get_a_tags(html: str):
    html_soup = BeautifulSoup(html, 'html.parser')
    table_rows = html_soup.find_all('tr')
    a_tags = []
    for tr in table_rows:
        a_tag = tr.find('a')
        a_tags.append(a_tag)

    return a_tags


def create_csv():
    html = sm.download_html(link)
    list_of_a_tags = get_a_tags(html)
    peaks_dict = sm.create_peaks_dict(list_of_a_tags, 'a', title_retrieval_method=None)
    df = pd.DataFrame(peaks_dict)
    df.to_csv('raw_data/johns_list_data.csv', index=False)


if __name__ == '__main__':
    create_csv()
