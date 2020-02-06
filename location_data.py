import pandas as pd


if __name__ == '__main__':
    location_data = pd.read_csv('raw_data/locations.csv')
    location_data[['lat', 'long']] = location_data['location'].str.split(',', expand=True)
    location_data['lat'] = location_data['lat'].str.strip()
    location_data['long'] = location_data['long'].str.strip()
    location_data = location_data[['name', 'lat', 'long']]
    location_data.to_csv('cleaned_data/locations.csv', index=False)
