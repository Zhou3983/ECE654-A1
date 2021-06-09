import ast
from astmonkey import visitors, transformers

def check_identifiers_with_length_equal_13(program):
    identifiers_with_length_equal_13_set = set()
    root = ast.parse(program)
    bfs = [root]
    
    while bfs:
        current_node = bfs.pop(0)
        if (current_node.__class__.__name__ =="Name"):
            if len(current_node.id) == 13:
                identifiers_with_length_equal_13_set.add(current_node.id)
        for child in ast.iter_child_nodes(current_node):
            bfs.append(child)
            
    identifiers_with_length_equal_13_counter = len(identifiers_with_length_equal_13_set)
    if identifiers_with_length_equal_13_counter > 1:
        print(f'{identifiers_with_length_equal_13_counter} identifiers with length equal 13 in this program.')
    elif identifiers_with_length_equal_13_counter == 1:
        print(f'{identifiers_with_length_equal_13_counter} identifier with length equal 13 in this program.')
    elif identifiers_with_length_equal_13_counter == 0:
        print('There is no identifiers with length equal 13')
    return identifiers_with_length_equal_13_counter

def check_max_control_structure_nesting_of_4(program):
    nodes_nesting_greater_than_4 = 0
    root = ast.parse(program)
    bfs = [root]
    control_structure_counter = {root:0}
    while bfs:
        current_node = bfs.pop(0)
        if current_node.__class__.__name__ in ['If', 'While', 'For']:
            control_structure_counter[current_node] += 1
            if control_structure_counter[current_node] > 4:
                nodes_nesting_greater_than_4 += 1
        for child in ast.iter_child_nodes(current_node):
            bfs.append(child)
            control_structure_counter[child] = control_structure_counter[current_node]
            
    print(f'{nodes_nesting_greater_than_4} nodes have control structure nesting greater than 4')
    return nodes_nesting_greater_than_4

def visualize_ast(program):
    root = ast.parse(program)
    graphNode = transformers.ParentChildNodeTransformer().visit(root)
    graphVisitor = visitors.GraphNodeVisitor()       
    graphVisitor.visit(graphNode)
    graphVisitor.graph.write_png('graph.png')
    return True