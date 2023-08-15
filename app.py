import time
import random
import threading

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question, choices):
        print(question)
        for i, choice in enumerate(choices, start=0):
            print(f"{chr(65 + i)}. {choice}")

    def take_quiz(self):
        for question, choices, correct_choice in self.questions:
            self.display_question(question, choices)

            user_choice = input("Select your answer (A/B/C/D) or type 'SKIP' to skip: ").upper().strip()

            if user_choice == "SKIP":
                continue

            user_choice_index = ord(user_choice) - 65
            if user_choice_index == correct_choice:
                print("Correct answer!\n")
                self.score += 20
            else:
                print("Wrong answer.\n")
                self.score -= 20

    def show_result(self):
        print("Quiz completed!")
        print(f"Your score: {self.score}/100")
        
# Questions and multiple-choice options for the "medium" level
medium_questions = [
    ("What does the acronym 'IDE' stand for in the context of programming?",
     ["Integrated Development Environment", "Interactive Design Elements", "Interface Development Entity", "Intelligent Debugging Engine"],
     0),
    ("In programming, what is a 'syntax error'?",
     ["A type of runtime error", "A mistake in program logic", "An issue with memory allocation", "Incorrect arrangement of code elements"],
     3),
    ("What does OOP stand for in programming?",
     ["Object-Oriented Protocol", "Order of Operation Principles", "Object-Oriented Programming", "Object Optimization Process"],
     2),
    ("What is the purpose of a 'constructor' in object-oriented programming?",
     ["To create an instance of a class", "To modify the visibility of class members", "To define static methods", "To handle exceptions"],
     0),
    ("Which programming paradigm promotes organizing code as reusable functions?",
     ["Procedural programming", "Functional programming", "Imperative programming", "Logical programming"],
     1),
]

# Questions and multiple-choice options for the "hard" level
hard_questions = [
    ("In multithreading, what is a 'race condition'?",
     ["A situation where two threads compete in a sprint", "An error that occurs when multiple threads access shared data concurrently, leading to unpredictable outcomes",
      "A synchronization technique for preventing deadlocks", "A form of thread prioritization"],
     1),
    ("What is a 'closure' in programming, and in which programming languages is it commonly used?",
     ["A type of memory leak; used in low-level languages", "A feature that allows encapsulation of data and functions; commonly used in JavaScript and functional programming languages",
      "A security mechanism used in network programming", "A method of implementing polymorphism; used in object-oriented languages"],
     1),
    ("What is the significance of the 'volatile' keyword when applied to a variable in programming?",
     ["It indicates that the variable cannot be modified", "It ensures that the variable's value is cached for optimization purposes",
      "It instructs the compiler to avoid optimizing the variable's access, making it suitable for concurrent programming", "It specifies that the variable is a constant"],
     2),
    ("Explain the concept of 'memoization' in the context of programming.",
     ["A technique for optimizing memory usage in embedded systems", "A method of encrypting data for secure transmission",
      "A strategy for caching the results of expensive function calls to improve performance", "A process of organizing code into modular components"],
     2),
    ("What are 'monads' in functional programming, and how do they relate to managing side effects?",
     ["Monads are mathematical structures used in graphics programming", "Monads are a form of debugging tools in development environments",
      "Monads are a programming concept that provides a structured way to manage side effects, ensuring predictable and controlled program behavior",
      "Monads are a type of error handling mechanism in concurrent programming"],
     2),
]

def main():
    level = input("Select quiz level (medium/hard): ")
    
    if level == "medium":
        quiz = Quiz(medium_questions)
    elif level == "hard":
        quiz = Quiz(hard_questions)
    else:
        print("Invalid level choice.")
        return

    print("Welcome to the QuizzyPy")
    print("Each correct answer adds 20 points, while each wrong answer deducts 20 points.\n")
    input("Press Enter to start...")
    
    quiz.take_quiz()
    quiz.show_result()

    # Tambahkan respons visual dan pesan motivasi
    if quiz.score == len(quiz.questions):
        print("\nCongratulations! You got all the answers correct!")
        print("Here's a star for your achievement:\n")
        print("   *   ")
        print("  ***  ")
        print(" ***** ")
        print("*******")
        print(" ***** ")
        print("  ***  ")
        print("   *   ")
    else:
        print("\nRemember, even the greatest success stories are woven with threads of setbacks. Use your failures as stepping stones to rise higher and achieve your goals.")
        print("Stay determined and keep pushing forward!\n")
        print("  :-)  ")

if __name__ == "__main__":
    main()