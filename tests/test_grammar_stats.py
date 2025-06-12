import pytest
from lib.grammar_stats import GrammarStats

"""
Given text which starts with a capital letter and ends with a fullstop
returns true
"""
def test_check_true_if_text_correct():
    gramamar_stats = GrammarStats()
    
    actual = gramamar_stats.check("This is a sentence.")

    expected = True

    assert actual == expected

"""
Given text which doesn't start with a capital letter and ends with a fullstop
returns true
"""
def test_check_false_if_text_doesnt_start_with_capital():
    gramamar_stats = GrammarStats()
    
    actual = gramamar_stats.check("this is a sentence.")

    expected = False

    assert actual == expected

"""
Given text which  starts with a capital letter and doesn't end with a fullstop
returns true
"""
def test_check_false_if_text_doesnt_end_with_fullstop():
    gramamar_stats = GrammarStats()
    
    actual = gramamar_stats.check("This is a sentence")

    expected = False

    assert actual == expected

"""
Given empty text 
throws an error
"""
def test_empty_ext_throws_error():
    gramamar_stats = GrammarStats()
    
    with pytest.raises(Exception) as err:
        gramamar_stats.check("")

    error_message = str(err.value)

    expected = "Cannot check empty string"

    assert error_message == expected

"""
Given 3 lines of text
returns percentage of correct text
"""
def test_percntage_good_returns_percentage():
    gramamar_stats = GrammarStats()
    
    gramamar_stats.check("this is a sentence")
    gramamar_stats.check("This is a sentence")
    gramamar_stats.check("This is a sentence.")

    actual = gramamar_stats.percentage_good()
    
    expected = 33

    assert actual == expected