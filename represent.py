from common import Node

def extract_nodes(node:Node, width:int):
    stack = [node]
    nodes = []
    while stack:
        node = stack.pop()
        nodes.append(node)
        stack.extend(node.advisors[:width])

    stack = [node]
    while stack:
        node = stack.pop()
        nodes.append(node)
        stack.extend(node.students[:width])
    
    return list(set(nodes))

def toDotFormat(node:Node, width:int):
    output = 'digraph G {\n'
    output += '\tnode [shape=box, style=filled, fillcolor=white];\n'

    nodes = extract_nodes(node, width)

    for node in nodes:
        output += f'\t{node.id} [label="{node.name}" fillcolor="gray"];\n'

    
    for node in nodes:
        for advisor in node.advisors[:width]:
            output += f'\t{node.id} -> {advisor.id} [color="red"];\n'
    
    for node in nodes:
        for student in node.students[:width]:
            if student not in nodes:
                output += f'\t{student.id} [label="{student.name}" color="green"];\n'
                output += f'\t{student.id} -> {node.id}\n'
    
    output += '}\n'

    return output

