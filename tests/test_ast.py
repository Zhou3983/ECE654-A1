
from src import ast_util

def test_equal_13():
    with open('tests/samples/sample_1.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 2
    
def test_nest_max_4():
    with open('tests/samples/sample_1.py') as f:
        program = f.read()
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 1