# we consider our class has 20 students and here we will calculate GPA of math lesson

name = input('Please Inter Your First_Name : ')  # inter first name for identification
family = input('Please Inter Your Last_Name : ') # inter last name for identification

doc = dict() # Defining a dictionary to store student names and grades

def save(a,b):
    doc[a] = b
    return doc

if name == 'mohammad' and family == 'javad' :
    print('You Have Permission')
    for i in range(0,3) :
        name_1 = input('Please Inter Name Of Student : ')
        score = int(input('Please Inter %s Score : ' % name_1))
        save(name_1,score)
    m = list(doc.keys())
    n = list(doc.values())
    p = sum(n) / len(m)
    for t,u in list(doc.items()) :
        print(t,u)
    print('GPA = %f' %p)
    #print(doc)

else :
    print('You Dont Have Permission')

