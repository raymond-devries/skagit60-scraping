import pandas as pd
import re


def clean_mountain_names(mountain_name: str, remove_spaces=True):
    mountain_name = mountain_name.lower()
    words_to_remove = ['mountain', 'mount', 'mt', 'peak', 'the', ',', '"']
    for word in words_to_remove:
        mountain_name = mountain_name.replace(word, '')

    mountain_name = re.sub(r'\(.*\)', '', mountain_name)
    mountain_name = mountain_name.strip()
    if remove_spaces:
        mountain_name = mountain_name.replace(' ', '')

    return mountain_name


def create_skagit_60_df():
    skagit_60_peaks = pd.read_csv('raw_data/Current60.csv')
    skagit_60_peaks = skagit_60_peaks[['Mountain']]
    skagit_60_peaks['cleaned_names'] = skagit_60_peaks['Mountain'].apply(clean_mountain_names)
    return skagit_60_peaks


if __name__ == '__main__':
    data_files = ['wta_data.csv', 'johns_list_data.csv', 'peakbagger_data.csv',
                  'wiki_data.csv', 'peakbagger_data_location.csv']

    skagit_60 = create_skagit_60_df()

    for data in data_files:
        df = pd.read_csv('raw_data/' + data)
        df['cleaned_names'] = df['name'].apply(clean_mountain_names)
        merged_df = skagit_60.merge(df, 'left', 'cleaned_names')
        save_name = 'cleaned_data/' + data.replace('data', 'links')
        merged_df.to_csv(save_name)
