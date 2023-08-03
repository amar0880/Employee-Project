from emplo import *

from utility import *

db=[]


class Test:
    
    def DashBoard(self):
        
        print("""
              
                    Welcome To Employee Managment System
                             ----Menu----
                             
                        1. Create a New Employee
                        2. Display The Employee
                        3. Update The Employee
                        4. Delete The Employee
                        5. Search Employee
                        
              """)


    def createEmployee(self):
        try :
            uname= input("Enter Name of The Employee : ")
            uid =eval (input("Enter The Uid of the Employee : "))
            usalary=eval (input("Enter the salary of the Employee :"))
            udept= input("Enter The Employee Department : ")
            e1=Employee(nm=uname,id=uid,sal=usalary,dept=udept)
            
            db.append(e1)
            print(f"Employee {uname} Added Successfully In database....")
        except Exception as e:
            print(f"Error: An unexpected error occurrred : {e}")
            
            
    def displayEmployee(self):
        print("-"*85)
        print("|{i:^20}|{n:^20}|{s:^20}|{d:^20}|".format (i="E_ID", n="Name", s="Salary",d="Department"))
        print("-"*85)
        
        for i in range(len(db)):
            print("|{id:^20}|{n:^20}|{s:^20}|{d:^20}|".format (id=db[i].EID, n=db[i].name, s=db[i].salary,d=db[i].department))
            print("-"*85)
            
    def searchEmployee(self):
        try:
            uid = eval(input("Enter Employee ID : "))
            
            for i in range(len(db)):
                if db[i].EID == uid:
                    return 1
            return -1
        except ValueError :
            print("Invalid Emloyee ID..Please Enter a Valid ID Number")
            return -1
        
    def updateEmployee(self):
        i = self.searchEmployee()
        if i>= 0:
            try :
                uname=input("Enter Updated Name of The Employee : ")
                usalary=eval(input("Enter The updated salary of the Employee : "))
                udept = input("Enter The Updated Employee Department : ")
                
                db[i].name=uname
                db[i].salary=usalary
                db[i].department=udept
                
                print(f"Employee {db[i].name} updated successfully in db...")
            except ValueError :
                print("Invalid salary. Please enter a valid number.")
                
    def deleteEmployee(self):
        i =self.searchEmployee()
        if i>=0:
            del db[i]
        

demmy= Employee('Amar',101,2500,"IT")
db.append(demmy)

new1= Employee('Amruta',201,2400,"HR")
db.append(new1)

new2= Employee('Pratiksha',301,2200,"HR")
db.append(new2)



obj=Test()

while True:
    obj.DashBoard()
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        obj.createEmployee()
       
    elif choice == 2:
        var =validate_db(db)
        if var :
            obj.displayEmployee()
        else :
            print("Database is Empty ! ")
            
    elif choice ==3:
        var = validate_db(db)
        if var :
            obj.updateEmployee()
        else:
            print("Database is Empty ! ")
            
    elif choice ==4:
        var = validate_db(db)
        if var:
            obj.deleteEmployee()
        else:
            print("Database is Empty ! ")
        
    elif choice ==5:
        var = validate_db(db)
        if var :
            i = obj.searchEmployee()
            if i>=0 :
                print(f"Employee Found at index {i}")
                
            else :
                print("Invaild Employee ID !")
    else:
        print("Database is Empty ! ")
    
    
    ch=input("Do You Want to Continue y/n ? : ")
    if ch.lower() !='y':
        for i in range(len(db)):
            print(db[i])
            break

    
    
    
    
    
    