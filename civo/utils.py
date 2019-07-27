"""
File to handle all utils
"""


def filter_list(data: dict, filter: str) -> list:
    """
    Function to handle filter in all list of the api
    :param data: object json
    :param searchs: the filter in this format (label:Home, id:6224cd2b-d416-4e92-bdbb-db60521c8eb9)
    :return: the found object in json format
    """
    filter_split = filter.split(':')
    search_in = filter_split[0]
    search = filter_split[1]

    try:
        search = int(search)
    except ValueError:
        pass

    return [element for element in data if element[search_in] == search]
