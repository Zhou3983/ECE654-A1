import argparse
import ast_util
parser = argparse.ArgumentParser('Analysis on AST')
parser.add_argument('--program', type=str, default='sample.py')

if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.program) as f:
        program = f.read()
        
    ast_util.check_identifiers_with_length_equal_13(program)
    ast_util.check_max_control_structure_nesting_of_4(program)
    ast_util.visualize_ast(program)
    
    