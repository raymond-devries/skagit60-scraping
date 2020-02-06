from bs4 import BeautifulSoup
import pandas as pd
from scrapers import scraper_modules as sm

peaks_links = ('https://en.wikipedia.org/wiki/Category:Mountains_of_Washington_(state)',
               'https://en.wikipedia.org/w/index.php?title=Category:Mountains_of_Washington_('
               'state)&pagefrom=Hibox+Mountain#mw-pages',
               'https://en.wikipedia.org/w/index.php?title=Category:Mountains_of_Washington_('
               'state)&pagefrom=Tekoa+Mountain+%28Washington%29#mw-pages')


def get_list_of_peak_a_tags(html: str):
    html_soup = BeautifulSoup(html, 'html.parser')
    content_div = html_soup.find('div', attrs={'class': 'mw-category'})
    a_tags = content_div.find_all('a')
    return a_tags


def create_csv():
    peak_a_tags = []

    for link in peaks_links:
        wiki_html = sm.download_html(link)
        peak_a_tags = peak_a_tags + get_list_of_peak_a_tags(wiki_html)

    peaks_dict = sm.create_peaks_dict(peak_a_tags, 'title')

    df = pd.DataFrame(peaks_dict)
    df.to_csv('raw_data/wiki_data.csv', index=False)


if __name__ == '__main__':
    create_csv()
