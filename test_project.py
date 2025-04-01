import pytest
from project import load_flashcards, check_answer

def test_check_answer_exact_match():
    assert check_answer("Python", "Python")

def test_check_answer_case_insensitive():
    assert check_answer("python", "PYTHON")

def test_check_answer_incorrect():
    assert not check_answer("Java", "Python")

def test_load_flashcards(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    file = d / "test_flashcards.csv"
    file.write_text("question,answer\nWhat is Python?,A programming language\n")

    cards = load_flashcards(file)
    assert len(cards) == 1
    assert cards[0]['question'] == "What is Python?"
    assert cards[0]['answer'] == "A programming language"
