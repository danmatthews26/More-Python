class user():
    def __init__(self, name, age, ethnicity):
        self.name = name
        self.age = str(age)
        self.ethnicity = ethnicity

    def write_info(self):
        """Dynamically writes user info to file named after user object name"""
        info = open(self.name+".txt", "w+") #write and read
        info.write(self.name + " " + self.age + " " + self.ethnicity)

me = user("Daniel", 11, "Black")        
you = user("Bob",102, "Asian")
user.write_info(me)
user.write_info(you)