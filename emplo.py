class Employee:
    def __init__(self, nm, id, sal,dept):
        self.name = nm
        self.EID = id
        self.salary = sal
        self.department = dept
        
        
    def getInfo(self):
        return self.name,self.EID,self.salary,self.department
        
    def __str__(self):
        return str(self.EID) + self.name   
        
        
        
  