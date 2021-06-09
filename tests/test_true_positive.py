from src import ast_util

def test_true_negative_1():
    with open('tests/samples/true_positive_1.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 0
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 0
    
def test_negative_2():
    with open('tests/samples/true_positive_2.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 0
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 0
    
def test_negative_2():
    with open('tests/samples/true_positive_3.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 0
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 0
    
def test_negative_2():
    with open('tests/samples/true_positive_4.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 0
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 0
    
def test_negative_2():
    with open('tests/samples/true_positive_5.py') as f:
        program = f.read()
    equal_13_counter = ast_util.check_identifiers_with_length_equal_13(program)
    assert equal_13_counter == 0
    max_4_counter = ast_util.check_max_control_structure_nesting_of_4(program)
    assert max_4_counter == 0
    

