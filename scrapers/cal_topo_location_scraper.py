from bs4 import BeautifulSoup
import pandas as pd


def get_html_content():
    with open('../raw_data/location_info.txt', 'r') as file:
        html = file.read()
    return html


def get_location_data(html: str):
    html_soup = BeautifulSoup(html, 'html.parser')
    table_rows = html_soup.find_all('tr')
    names = []
    locations = []
    for td in table_rows:
        try:
            name = td.select_one('td:nth-of-type(1)').get_text()
            location = td.select_one('td:nth-of-type(3)').get_text()
            names.append(name)
            locations.append(location)
        except AttributeError:
            pass
    pd.DataFrame({'name': names, 'location': locations}).to_csv('../raw_data/locations.csv', index=False)


if __name__ == '__main__':
    cal_topo_html = get_html_content()
    get_location_data(cal_topo_html)



