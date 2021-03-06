from search import (
    search_advisors,
    search_students,
    searchNodeByName
)

from represent import (
    toDotFormat
)

name = input('Enter name: ')



# in following parameters, up means the node is the parent of the node or advisors of students
# down means the node is the child of the node or students of each teacher

# we recursively search for the advisor of the student
# how many times we recurse is the depth of the search:
up_depth, down_depth = -1, -1 # -1 means no limit

# as the graph widens, the number of nodes we search increases exponentially
# to limit the number of nodes in each iteration, use following parameters:
up_width, down_width = 2, 2

node = searchNodeByName(name)
node = search_advisors(node, up_depth, up_width)
node = search_students(node, down_depth, down_width)

# even with setting width to 2, each node is connected to all of its children and all of its parents, width just prevents 
# the algorithm to search for all of those nodes in each iteration
# to put a limit on the number of nodes which would be printed in the graph, use the following parameters:
presentation_width = 5


output = toDotFormat(node, presentation_width)

with open('output.dot', 'w', encoding='utf-8') as f:
    f.write('// Generated by console.py\n')
    f.write(f'// parameters: up depth={up_depth}, down depth={down_depth}, up width={up_width}, down width={down_width}, presentation width={presentation_width}\n')
    f.write(output)

print('Done!')
print('output.dot is generated.')
print('use "dot -Tpng output.dot -o output.png" to generate image.')