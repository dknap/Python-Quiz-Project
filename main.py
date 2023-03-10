from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(text=question["text"], answer=question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    answer = quiz.next_question()
    quiz.check_answer(answer)

quiz.final_statement()