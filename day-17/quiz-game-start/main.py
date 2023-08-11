from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

new_quiz_brain = QuizBrain(question_bank)

while new_quiz_brain.still_has_questions():
    new_quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {new_quiz_brain.score}/{new_quiz_brain.question_number}")
