class car:
    def __init__(self , company , model , manufac_year , color):
       self.company = company 
       self.model = model 
       self.manufac_year = manufac_year
       self.color = color
    def drive(self):
       print(f"Drive {self.company} {self.model}")

    def stop(self):
       print(f"Stop {self.company} {self.model}")
    