import html
class QuizBrain():
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
    def still_has_question(self):
        return len(self.question_list)>self.question_number
    
    def next_question(self):
        self.current_question=self.question_list[self.question_number]
        self.question_number+=1
        return f"Q.{self.question_number}:{html.unescape(self.current_question.question)}"
        # self.check_answer(ques,current_question.answer)

    def check_answer(self,answer):
        self.correct_answer=self.current_question.answer
        return answer.lower()==self.correct_answer.lower()
            
        