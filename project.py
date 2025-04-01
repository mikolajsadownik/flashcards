import csv
import random

def load_flashcards(filename):
    flashcards = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            flashcards.append({"question": row["question"], "answer": row["answer"]})
    return flashcards

def quiz_user(flashcards):
    print("\n*** Python Flashcards Quiz ***\n")
    random.shuffle(flashcards)
    score = 0
    for i, card in enumerate(flashcards, 1):
        print(f"{i}. {card['question']}")
        user_answer = input("Your answer: ").strip()
        if check_answer(user_answer, card['answer']):
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {card['answer']}\n")
    print(f"Quiz finished! Your score: {score}/{len(flashcards)}")

def check_answer(user_input, correct_answer):
    return user_input.lower() == correct_answer.lower()

def main():
    
    filename = input("Please provide a name of a file with flashcards: ")
    try:
        flashcards = load_flashcards(filename)
        quiz_user(flashcards)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    main()
