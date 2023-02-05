class QuizBrain:
    def __init__(self, q_list):
        self.user_answer = None
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        return answer

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, answer):
        question = self.question_list[self.question_number - 1]
        # print(question.answer)
        if answer.lower() == question.answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"That's wrong!")
        print(f"The correct answer was: {question.answer}. \nYour current score is: {self.score}/{self.question_number}.")