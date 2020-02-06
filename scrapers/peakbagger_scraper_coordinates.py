from scrapers import scraper_modules as sm
import pandas as pd
from bs4 import BeautifulSoup

link1 = 'https://www.peakbagger.com/search.aspx?tid=R&lat='
link2 = '&lon='


def create_search_list():
    search_list = pd.read_csv('../cleaned_data/locations.csv')
    search_list = search_list[['lat', 'long']]
    return search_list


def get_a_tag(html: str):
    html_soup = BeautifulSoup(html, 'html.parser')
    table = html_soup.find('table', attrs={'style': 'margin-left:35px'})
    row = table.select_one('tr:nth-of-type(2)')
    a_tag = row.find('a')
    return a_tag


def create_csv():
    list_of_a_tags = []
    search_list = create_search_list()
    for index, row in search_list.iterrows():
        print(row)
        html = sm.download_html(link1 + str(row['lat']) + link2 + str(row['long']))
        list_of_a_tags.append(get_a_tag(html))

    peaks_dict = sm.create_peaks_dict(list_of_a_tags, 'a', title_retrieval_method=None)
    df = pd.DataFrame(peaks_dict)
    df.to_csv('../raw_data/peakbagger_data_location.csv', index=False)


if __name__ == '__main__':
    create_csv()

