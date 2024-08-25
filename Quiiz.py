#from data import question_data
#from question_model import Question
#from quiz_brain import QuizBrain


#Inside the Question_model file
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#inside the quizbrain file    

class QuizBrain:
    
    
    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0
        
        
    def examine(self, ans, correct_answer):
         if ans.lower() == correct_answer.lower():
             print("Yes, you are right")
             self.score += 1
         else:
             print("Oppss.. Looks like you need to read more")
             self.score -= 1   
         print(f"Your score = {self.score}")
        
    def next_question(self):
        current_question = self.q_list[self.question_number]

        self.question_number += 1

        User_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False) : ")
        self.examine(User_ans, current_question.answer)
        

    
    def still_has_questions(self):
        if len(self.q_list) > self.question_number:
            return True
        else:
            return False
        
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Inside the data file
   
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

#-------------------------------------------------------------------------------------------------------------------------------------------
#Create a list called "question Bank" 
QuestionBank = []

for i in range(len(question_data)):
    Question_dict= question_data[i]
    Question_text = Question_dict["text"]
    Question_answer = Question_dict["answer"]
    
    final_question = Question(Question_text, Question_answer)
    QuestionBank.append(final_question)
    
    
Display_question = QuizBrain(QuestionBank)

while Display_question.still_has_questions():      
    
    Display_question.next_question()
    
    
    

