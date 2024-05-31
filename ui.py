from tkinter import *
from quiz import QuizBrain

class Quizui():
    def __init__(self,QuesQuiz:QuizBrain):

        self.cques=QuesQuiz
        self.cscore=0
        self.screen=Tk()
        self.screen.config(height=400,width=300,bg='#000')
        self.screen.title('Quiz Application')
        self.canvas=Canvas(bg='#fff')
        self.score=Label(text=f"Score:{self.cscore}",font=('Arital',14,'italic'),fg='#fff' ,bg='#000')
        self.score.grid(row=0,column=1,pady=10)
        self.question=self.canvas.create_text(200,150,text='Enter Your Text Here' ,fill='#000',font=('Arial',22,'italic'),width=350)
        self.canvas.grid(row=1,column=0,padx=20,pady=100,columnspan=2)
        right_image=PhotoImage(file='images/true.png')
        self.right=Button(image=right_image,command=self.check_correct)
        self.right.grid(row=2,column=0,pady=10)
        wrong_image=PhotoImage(file='images/false.png')
        self.wrong=Button(image=wrong_image,command=self.check_wrong)
        self.wrong.grid(row=2,column=1,pady=10)
        self.get_next_question()
        self.screen.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='#fff')
        if self.cques.still_has_question():
            curr_question=self.cques.next_question()
            self.canvas.itemconfig(self.question,text=curr_question)
        else:
            self.canvas.itemconfig(self.question,text=f"Quiz Ended \n Your Final Score is {self.cscore}")
            self.right.config(state='disabled')
            self.wrong.config(state='disabled')

    def check_correct(self):
        answer=self.cques.check_answer('True')
        self.feedback(self.cques.check_answer('True'))
           
    def check_wrong(self):
        answer=self.cques.check_answer('False')
        self.feedback(answer)

        
    def feedback(self,is_right):
        if is_right:
            self.cscore+=1
            self.score.config(text=f"Score:{self.cscore}")
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.screen.after(1000,self.get_next_question)
        
