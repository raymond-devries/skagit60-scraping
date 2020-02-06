from bs4 import BeautifulSoup
import scrapers.scraper_modules as sm
import pandas as pd


def get_list_of_links():
    links = pd.read_csv('../cleaned_data/full_links.csv')
    links = links['full_link']
    return links


def get_elevation(html_soup: BeautifulSoup):
    td = html_soup.find('td', attrs={'valign': 'top', 'width': '34%'})
    elevation = td.find('h2').get_text()
    return elevation


def create_csv():
    scraper_links = get_list_of_links()
    links = []
    elevations = []
    for link in scraper_links:
        print(link)
        html = sm.download_html(link)
        html_soup = BeautifulSoup(html, 'html.parser')
        elevation = get_elevation(html_soup)
        elevations.append(elevation)
        links.append(link)
    elevations_df = pd.DataFrame({'link': links, 'elevation': elevations})
    elevations_df.to_csv('../raw_data/elevations.csv', index=False)


if __name__ == '__main__':
    create_csv()
