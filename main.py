from ui import Quizui
from question_bank import QuestionBank
from data import questions
from quiz import QuizBrain
questions_list=[]
for question in questions:
    ques=question['question']
    ans=question['correct_answer']
    questionbank= QuestionBank(ques,ans)
    questions_list.append(questionbank)
quiz=QuizBrain(questions_list)
screen=Quizui(quiz)




