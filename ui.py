from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.label_score = Label(text= "Score: 0",bg=THEME_COLOR,fg="white")
        self.label_score.grid(row=0,column=1)


        self.canvas = Canvas(width=300,height=250,bg="white")

        self.text_quiz = self.canvas.create_text(150,125,text="hi",fill=THEME_COLOR,font=("Arial",20,"italic"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)


        self.check = PhotoImage(file="./images/true.png")
        self.correct = Button(image=self.check,pady=20,padx=20,highlightthickness=0,command=self.correct)
        self.correct.grid(row=2,column=0)
        self.cross = PhotoImage(file="./images/false.png")
        self.incorrect = Button(image=self.cross,pady=20,padx=20,highlightthickness=0,command=self.incorrect)
        self.incorrect.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text_quiz,text=q_text)

    def correct(self):
        self.update_Score(self.quiz.check_answer("True"))

    def incorrect(self):
        self.update_Score(self.quiz.check_answer("False"))
    def update_Score(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.label_score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.text_quiz,text=f"GAME OVER \n You got {self.quiz.score}/10")
            self.correct.config(state="disabled")
            self.incorrect.config(state="disabled")

