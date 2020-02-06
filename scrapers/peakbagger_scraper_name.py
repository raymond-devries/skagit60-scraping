from scrapers import scraper_modules as sm
import pandas as pd
import clean_raw_data
from bs4 import BeautifulSoup

link1 = 'https://www.peakbagger.com/search.aspx?tid=M&ss='
link2 = '&lat=&lon='


def create_search_list():
    search_list = pd.read_csv('../raw_data/Current60.csv')
    search_list['cleaned_names'] = search_list['Mountain'].apply(clean_raw_data.clean_mountain_names,
                                                                 remove_spaces=False)
    search_list = search_list['cleaned_names']
    return search_list


def get_a_tags(html: str):
    html_soup = BeautifulSoup(html, 'html.parser')
    table = html_soup.find('table', attrs={'style': 'margin-left:35px'})
    table_rows = table.find_all('tr')
    wa_table_rows = []
    for tr in table_rows:
        try:
            location = tr.select_one('td:nth-of-type(3)').get_text().strip()
            if location == [] or location == 'USA-WA':
                wa_table_rows.append(tr)
        except AttributeError:
            pass

    a_tags = []
    for tr in wa_table_rows:
        a_tag = tr.find('a')
        a_tags.append(a_tag)

    return a_tags


def create_csv():
    list_of_a_tags = []
    search_list = create_search_list()
    for name in search_list:
        html = sm.download_html(link1 + name + link2)
        list_of_a_tags = list_of_a_tags + get_a_tags(html)

    peaks_dict = sm.create_peaks_dict(list_of_a_tags, 'a', title_retrieval_method=None)
    df = pd.DataFrame(peaks_dict)
    df.to_csv('raw_data/peakbagger_data.csv', index=False)


if __name__ == '__main__':
    create_search_list()
    create_csv()
