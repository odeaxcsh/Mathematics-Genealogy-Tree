import re
import bs4 as bs

from common import Node

__all__ = [ 'extract_information' ]


def _extract_id(url:str):
    r = re.compile(r"id\.php\?id=(\d+)")
    return r.search(url).group(1)

def extract_information(html:str) -> Node:
    soup = bs.BeautifulSoup(html, 'html.parser')
    
    name = soup.find('h2').text.split('\n')[1]
    id = re.compile(r"noting this mathematician's MGP ID of (\d+) for the advisor ID").search(html).group(1)

    advisors = soup.find('div', id='paddingWrapper').find_all('p')[1].find_all('a')
    advisors = [
        Node(
            _extract_id(advisor['href']), 
            advisor.string
        )
        for advisor in advisors
    ]

    students = [ child.find_all('td')[0].find('a') for child in soup.find_all('tr')[1:] ]
    students = [
        Node(
            _extract_id(student['href']), 
            student.string
        )
        for student in students
    ]

    return Node(id, name, advisors, students)
