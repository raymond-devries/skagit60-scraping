import pandas as pd

if __name__ == '__main__':
    website = 'https://www.peakbagger.com/'

    links = pd.read_csv('raw_data/links.csv')
    links['full_link'] = website + links['link']
    full_links = links[['Mountain', 'full_link']]
    full_links = full_links.rename(columns={'full_link': 'link'})
    full_links.to_csv('cleaned_data/full_links.csv', index=False)
