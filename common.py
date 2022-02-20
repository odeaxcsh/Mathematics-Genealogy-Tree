
__all__ = ['Node']

class Node:
    __slots__ = ['students', 'advisors', 'name', 'id']

    def __init__(self, id:str, name:str, advisors:list=None, students:list=None)-> None:
        self.id = id
        self.name = name
        self.advisors = advisors if advisors is not None else []
        self.students = students if students is not None else [] 

    def __repr__(self) -> str:
        return f'{self.name}({self.id})'

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Node) and self.id == __o.id

    def __hash__(self) -> int:
        return 0 if self.id is None else int('1001' + self.id)

