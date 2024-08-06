class User:
    def set_name(self):
        name=input("Please Enter Your Name: ")
        self.name=name
    def get_name(self):
        return self.name
    
class Game:
    secret_name="ali"
    limit_of_counter=4
    current_counter=0
    is_loser=True
    def __init__(self):
        self.user=User()

    
    def excute_guessing_operation(self):
        self.user.set_name()
        while self.current_counter<self.limit_of_counter:
            current_guess=input("Enter Your Guessing: ")
            self.current_counter+=1
            if current_guess==self.secret_name:
                self.is_loser=False
                break
            else:
                print("Enter correct guess name!")
        if self.is_loser:
            print("Game Over !")
            print(f"{self.user.get_name()} is loser !")
        else:
            print("Game Over !")
            print(f"{self.user.get_name()} is winner !")


game=Game()
game.excute_guessing_operation()
# user=User()
# user.set_name()
# user.get_name()
