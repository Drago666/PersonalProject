#create a class in python

class student:
    def __init__(self, first, last, age, height):
        self.first=first
        self.last=last
        self.age=age
        self.height=height
        num=18-age+21
        self.email=first[0]+last+str(num)+"@lausanneschool.com"
        self.info=self.first+" "+self.last+" is "+str(self.age)+" and is "+str(self.height)+" inches tall. Their email is "+self.email

student1=student("Ryon","Ghodoussi",15, 70)

print(student1.info)



#student1=student.name()

#have not defined "name()" yet
#This is invoking a function using an object, we have yet to create that function

#student1=student()
#print(student1)
#
#This reference is constructing an object.
#student1.name="ab"
#student1.age=1
#student1.height=1

#student2 = student()
#student2.name="faris"
#student2.age=5
#student2.height=0

#print("name",student1.name)
#print("age", student1.age)
#print("height", student1.height)
#This adds the values to a class and allows us to reference it

#print("name",student2.name)
#print("age", student2.age)
#print("height", student2.height)
#Just printing "student1," it only prints the location, not the data on student 1