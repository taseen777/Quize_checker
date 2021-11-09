from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["c_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(logo)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score} out of {quiz.question_number}.")
