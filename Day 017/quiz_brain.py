class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    
    def next_question(self):
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {next_question.text}. (true/false)? ").lower()
        self.check_answer(user_answer, next_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print('You got that right!')
            self.score += 1
        else:
            print('You got that wrong!')
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is {self.score}/{self.question_number}\n')