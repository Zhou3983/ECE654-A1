
from src import ast_util

def test_true_negative_1():
    with open('tests/samples/true_negative_1.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 1
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 1
    
def test_negative_2():
    with open('tests/samples/true_negative_2.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 2
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 1
    
def test_negative_2():
    with open('tests/samples/true_negative_3.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 1
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 1
    
def test_negative_2():
    with open('tests/samples/true_negative_4.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 3
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 2
    
def test_negative_2():
    with open('tests/samples/true_negative_5.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 4
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 2
    


    
