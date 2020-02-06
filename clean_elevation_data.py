import pandas as pd
import re


def clean_elevation(elevation: str):
    elevation = re.sub(r'[\W]+', '', elevation)
    elevation = re.search(r'[\d]+', elevation).group()
    return elevation


if __name__ == '__main__':
    elevation_df = pd.read_csv('raw_data/elevations.csv')
    elevation_df['elevation'] = elevation_df['elevation'].apply(clean_elevation)
    elevation_df.to_csv('cleaned_data/elevations.csv', index=False)
