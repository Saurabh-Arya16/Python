#program to create quiz game using tuples

def quiz_game():
    questions = (
        "What is the capital of France?",
        "What is 2+2?",
        "What color do you get when you mix red and white?"
    )
    
    options = (
        ("A: Paris", "B: London", "C: Berlin", "D: Madrid"),
        ("A: 3", "B: 4", "C: 5", "D: 6"),
        ("A: Pink", "B: Purple", "C: Orange", "D: Yellow")
    )
    
    answers = ("A", "B", "A")  # Correct answer for the third question should be "A" not "C"

    score = 0
    print("Welcome to the Quiz Game!")
    
    for i in range(len(questions)):
        print(questions[i])
        for option in options[i]:
            print(option)
        user_answer = input("Your answer (A, B, C, D): ").strip().upper()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answers[i]}")
    
    print(f"You got {score} out of {len(questions)} questions correct.")

if __name__ == "__main__":
    quiz_game()
