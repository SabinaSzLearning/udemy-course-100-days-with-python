class QuizBrain:

    def __init__(self, qst_list):
        self.question_number = 0
        self.question_list = qst_list
        self.score = 0

    def next_question(self):
        cur_question =self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q{self.question_number} - {cur_question.question} - True/False?  ")
        print(self.check_answer(ans))

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer):
        cur_question = self.question_list[self.question_number-1]
        correct_answer = cur_question.answer
        if correct_answer.lower() == answer.lower():
            self.score += 1
            return f"Correct, the answer was {correct_answer}, SCORE: {self.score}/{self.question_number} \n\n"
        else:
            return f"Wrong, the answer was {correct_answer}, SCORE: {self.score}/{self.question_number} \n\n"
