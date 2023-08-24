import json

def load_questions(filename="questions.json"):
    with open(filename, "r") as file:
        return json.load(file)

def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        
        answer = int(input("Your choice (1/2/3/4): "))
        
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['options'][q['answer']-1]}\n")
    
    print(f"You scored {score}/{len(questions)}")

if __name__ == "__main__":
    questions = load_questions()
    run_quiz(questions)
