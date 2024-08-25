#Higher Lower Game
import sys
#Establish data
class Data:
    def __init__(self,number,name,age,job,contry):
        self.number = number
        self.name = name
        self.age = age
        self.job = job
        self.contry = contry
        
Emma_Watson = Data(1,"Emma Watson",33,'Actress, Activist',"United Kingdom")
Leonardo_DiCaprio = Data(2,"Leonardo DiCaprio",49," Actor, Film Producer"," United States")
BTS = Data(3,"BTS","Members' ages vary (as of my last update, in 2022, their ages ranged from 24 to 29)"," K-pop Group (Singers, Dancers)","South Korea")
Cristiano_Ronaldo = Data(4,"Cristiano Ronaldo",39,"Professional Soccer Player","Portugal")
Priyanka_Chopra_Jonas = Data(5,"Priyanka Chopra Jonas",41,"Actress, Singer, Film Producer",'India')
Dwayne_TheRock_Johnson = Data(6,"Dwayne (The Rock)Johnson",51,"Actor, Producer, Former Professional Wrestler","United States")
Adele = Data(7,"Adele",35,"Singer-Songwriter"," United Kingdom")
Shakira = Data(8,"Shakira",46,"Singer-Songwriter, Dancer","Colombia")
Chris_Hemsworth = Data(9,"Chris Hemsworth",40,"Actor","Australia")
Gisele_Bündchen = Data(10,"Gisele Bündchen",43,"Model, Environmental Activist","Brazil")

Data_list = {Emma_Watson,Leonardo_DiCaprio,BTS,Cristiano_Ronaldo,Priyanka_Chopra_Jonas,Dwayne_TheRock_Johnson,Adele,Shakira,Chris_Hemsworth,Gisele_Bündchen}
#Create a logo
def logo1():
    print("""
          __      __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/  
                                    |  
          """)

def logo2():
    print("""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
          """)


#Main loop
score = 1
i=0
while i<100:
    logo1()

    random_name = [Dwayne_TheRock_Johnson, Emma_Watson, BTS, Priyanka_Chopra_Jonas, Leonardo_DiCaprio, Adele,Shakira, Chris_Hemsworth, Cristiano_Ronaldo, Gisele_Bündchen]
    
    print("Compare A:",random_name[i].name,",",random_name[i].age,",",random_name[i].job,",",random_name[i].contry)

    logo2()

    print("Against B:",random_name[i+1].name,",",random_name[i+1].age,",",random_name[i+1].job,",",random_name[i+1].contry)

    choice = input("Who has more followers? Type 'A' or 'B': ")

       

    if  random_name[i].number < random_name[i+1].number:
        answer = 'A'
    elif random_name[i].number > random_name[i+1].number:
        answer = 'B'
        

    if answer == choice:
        score +=1
        print("You'r right! Current score:",score)    
    if answer!= choice :   
        print("Sorry, that's wrong. Final score:",score)
        sys.exit()
    i+=1
         
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          