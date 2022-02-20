import requests

__all__ = [ 'getbyname', 'getbyid' ]

_namesearchapi = 'https://genealogy.math.ndsu.nodak.edu/quickSearch.php'
_idsearchapi = 'https://www.mathgenealogy.org/id.php?id={}'


def getbyname(name:str):
    response = requests.post(_namesearchapi, {
        'Submit': 'Search',
        'searchTerms': name
    })
    return response.text


def getbyid(id:str):
    response = requests.get(_idsearchapi.format(id))
    return response.text

