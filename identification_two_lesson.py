# we consider our class has 20 students and here we will calculate GPA of math lesson

name = input('Please Inter Your Username : ')  # inter first name for identification
family = input('Please Inter Your Password : ') # inter last name for identification


dict_math = dict() # Defining a dictionary to store student names and grades
dict_physics = dict()

def math(a,b):
    dict_math[a] = b
    return dict_math

def physics(a,b):
    dict_physics[a] = b
    return dict_physics

if name == 'mohammad' and family == 'javad' :

    print('You Have Permission')

    for i in range(0,2):

        lesson = input('Please Inter Lesson : ')

        if lesson == 'math':

            for i in range(0,10) :

                name_1 = input('Please Inter Name Of Student : ')
                score = int(input('Please Inter %s math Score : ' % name_1))
                math(name_1,score)

            m = list(dict_math.keys())
            n = list(dict_math.values())
            p = sum(n) / len(m)

            for t,u in list(dict_math.items()) :

                print(t,':',u)

            print('GPA_math = %f' %p)
            

        if lesson == 'physics' :

            for i in range(0,10) :

                name_1 = input('Please Inter Name Of Student : ')
                score = int(input('Please Inter %s physics Score : ' % name_1))
                physics(name_1,score)

            m = list(dict_physics.keys())
            n = list(dict_physics.values())
            p = sum(n) / len(m)

            for t,u in list(dict_physics.items()) :

                print(t,':',u)

            print('GPA_physics = %f' %p)
        

else :
    print('You Dont Have Permission')

