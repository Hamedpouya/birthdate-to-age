import datetime



user_name = input("please enter your name : " )
user_birthdate = input("please enter your birthdate: ")

class birthdate_to_age:
   

    def __init__(self, name, birthdate):
            self.name = name
            self.birthdate = birthdate
            print(f"{self.name} to {self.birthdate} sale hasti")
        
    @classmethod
    def show(cls, name, birthdate):
        return cls(name, datetime.datetime.now().year - int(birthdate) ) 
 

user_input = birthdate_to_age.show(user_name, user_birthdate)
    
   
    
   