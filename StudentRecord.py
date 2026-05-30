
import os;
studentData={};

def addStudent():
    f=open("student.txt","a");
    iid=int(input("Enter id"));
    name=input("Enter Name");
    address=input("Enter Address");
    roll=input("Enter Roll no")
    grade=input("Enter grade");
    studentData[iid]={
        "Id":iid,
        "Name":name,
        "Address":address,
        "RollNo" : roll,
        "Grade" : grade
    }
    f.write(str(studentData[iid]) + "\n")
    print("Added Sucessful");
    f.close();
    
def viewStudent():
    f=open("student.txt","r");
    print(" Datas of Student  are \n");
    print(f.read());
    
def searchStudent():
    dataSearch = input("Enter id to search: ")
    f = open("student.txt", "r")
    found = False
    for line in f:
        if dataSearch in line:
            print("Data Found!!\n")
            print(line)
            found = True
            break
    if not found:
        print("Data Not Found")
    f.close() 

def deleteStudent():
    delete_id = input("Enter ID to delete: ")

    f = open("student.txt", "r")
    temp = open("temp.txt", "w")

    found = False

    for line in f:
        if f"'Id': {delete_id}" in line:
            found = True
            continue  # skip this record
        temp.write(line)

    f.close()
    temp.close()

    import os
    os.remove("student.txt")
    os.rename("temp.txt", "student.txt")

    if found:
        print("Student deleted successfully")
    else:
        print("ID not found")
        
        
while(True):
           os.system("cls") 
           print(" Welcome to our student record management system")
           print(" Press 1 for Add student");
           print("Press 2 for view student");
           print ("Press 3 for Search Student ");
           print("Press 4 for delete student");
           print("Press 5 for exit");
           choice = int(input(" Enter a choice"))

           if(choice>0 and choice<6):
            match(choice):
             case 1:
                 
                addStudent();
                input("Press Enter to continue...") 
             case 2:
                 viewStudent();
                 input("Press Enter to continue...") 
             case 3:
              searchStudent();
              input("Press Enter to continue...") 
             case 4:
              deleteStudent();
              input("Press Enter to continue...") 
             case 5:
              print("Byeee")
              exit(0);
             case _:
              print(" Wrong choice")
              input("Press Enter to continue...") 
            os.system("cls");
    
    