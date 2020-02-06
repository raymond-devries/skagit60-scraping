import pandas as pd
import clean_raw_data as cd

if __name__ == '__main__':
    locations = pd.read_csv('cleaned_data/locations.csv')
    links = pd.read_csv('cleaned_data/full_links.csv')
    elevations = pd.read_csv('cleaned_data/elevations.csv')

    locations['cleaned_names'] = locations['name'].apply(cd.clean_mountain_names)
    links['cleaned_names'] = links['Mountain'].apply(cd.clean_mountain_names)

    merged_df = links.merge(locations, 'left', 'cleaned_names')
    merged_df = merged_df.merge(elevations, 'left', 'link')
    merged_df = merged_df[['Mountain', 'name', 'elevation', 'lat', 'long', 'link']]
    renaming_dict = {'name': 'Cleaned Name', 'elevation': 'Elevation', 'lat': 'Latitude', 'long': 'Longitude', 'link': 'Peakbagger Link'}
    merged_df = merged_df.rename(columns=renaming_dict)
    merged_df.to_csv('final_list.csv', index=False)
