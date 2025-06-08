def display_student_summary():   
      print ("here is your list!")    
      for name , grade in student_list :
        print(name, grade,"/100")
def get_avg_grade():
    sum=0
    for name, grade in student_list :
        sum+= grade
    return sum / stud_num
def get_heighest_grade() :
   highest_student = max(student_list)
   print("the top student is :" , highest_student)
def count_passed():
    for name , grade in student_list:
        if grade >= 60 :
            print("the students who passed are :" ,student_list)
    
student_list=[] 

stud_num=int( input("enter the numbers of student \n "))

for i in range(stud_num) :
    name=input("please enter the name of the student \n " )
    grade=float(input("enter its full grade out of 100 \n "))
    student_list.append((name,grade))

display_student_summary()

average = get_avg_grade()

print("the average is :" , average) 

get_heighest_grade()

count_passed()




