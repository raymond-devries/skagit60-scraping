import requests


def download_html(link: str):
    response = requests.get(link)
    page_html = response.content
    return page_html


def create_peaks_dict(a_tags: list, title_type: str, title_retrieval_method='get'):
    list_of_peak_titles = []
    list_of_peak_links = []

    for a_tag in a_tags:
        try:
            if title_retrieval_method == 'get':
                title = a_tag.get(title_type)
            elif title_retrieval_method == 'find':
                title = a_tag.find(title_type).get_text()
            else:
                title = a_tag.get_text()

            href = a_tag.get('href')
            list_of_peak_titles.append(title)
            list_of_peak_links.append(href)

        except AttributeError:
            pass

    peaks_dict = {'name': list_of_peak_titles, 'link': list_of_peak_links}

    return peaks_dict
