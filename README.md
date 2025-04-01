# Flashcards Quiz

## Description

Flashcards Quiz is a terminal-based Python application that helps users learn Python programming concepts through an interactive flashcard quiz. The program loads questions and answers from a CSV file, shuffles them, and evaluates the user's answers. The quiz score is displayed at the end.

## How to Run

1. Ensure you have Python 3 installed.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the quiz:
```bash
python project.py
```

## Files

- `project.py`: Main program logic
- `test_project.py`: Unit tests for core functions
- `python_flashcards.csv`: Source of flashcard data
- `requirements.txt`: Required dependencies
- `README.md`: Project documentation

## Video Demo

📺 [Demo Video](https://youtu.be/your_demo_link_here)

## Design

This project includes:
- Modular functions: `load_flashcards`, `quiz_user`, `check_answer`, `main`
- Testing with `pytest`
- Error handling for missing CSV file
- CSV-based data separation for easy flashcard editing

## Author

Your Name
