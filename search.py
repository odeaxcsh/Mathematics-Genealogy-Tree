from data import (
    getbyid,
    getbyname
)

from soup import (
    extract_information,
    Node
)


__all__ = [
    'searchNodeByName',
    'searchNodeById',
    'search_advisors'
    'search_students'
]

def searchNodeByName(name:str):
    result = getbyname(name)
    return extract_information(result)

def searchNodeById(id:str):
    result = getbyid(id)
    return extract_information(result)



def _bfsSearch(root:Node, depth:int, diam:int, attr:str):
    currentLevel, levelIndex = set([root]), 0

    while levelIndex != depth and len(currentLevel):
        print()
        print(f'searching for {attr} in level {levelIndex}')
        print(f'number of nodes in current level: {len(currentLevel)}')
        print(f'nodes in current level: {currentLevel}')

        nextLevel = set()
        for node in currentLevel:
            adj = set()
            for i, parent in enumerate(getattr(node, attr), 1):
                newNode = searchNodeById(parent.id)
                adj = adj.union(set([newNode]))
                if i == diam:
                    break # to make sure that we only select the first `diam` advisors to extend
            setattr(node, attr, list(adj))
            nextLevel = nextLevel.union(adj)
        currentLevel, levelIndex = nextLevel, levelIndex + 1
    return root


def search_advisors(node:Node, depth:int, diam:int):
    return _bfsSearch(node, depth, diam, 'advisors')


def search_students(node:Node, depth:int, diam:int):
    return _bfsSearch(node, depth, diam, 'students')