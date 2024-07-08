import random

# Define the questions and answers
questions = [
    {
        "question": "What is the capital of Germany?",
        "options": ["A) Berlin", "B) Werder", "C) Nauen", "D) Teltow"],
        "answer": "A"
    },
    {
        "question": "What is the name of the tallest mountain peak in the world?",
        "options": ["A) K2", "B) Mount Everest", "C) Kangchenjunga", "D) Mount Fuji"],
        "answer": "B"
    },
    {
        "question": "What is the largest lake on Earth?",
        "options": ["A) Lake Superior", "B) Caspian Sea", "C) Lake Victoria", "D) Lake Huron"],
        "answer": "B"
    },
    {
        "question": "Which state is the richest state in India?",
        "options": ["A) Punjab", "B) Bihar", "C) Maharashtra", "D) Kerala"],
        "answer": "C"
    },
    {
        "question": "What is the commonly used value of pi?",
        "options": ["A) 3.45", "B) 3.14", "C) 2.71", "D) 4.63"],
        "answer": "B"
    }
]

def ask_question(question):
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Enter the letter of your answer: ").upper()
    return answer == question["answer"]

def run_quiz(questions):
    score = 0
    

    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")

    print(f"\nYour final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    run_quiz(questions)
