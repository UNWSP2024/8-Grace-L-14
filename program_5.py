'''Course Info Program
By Grace LeVoir
3 - 20 - 26'''


# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.


'''Pseudocode'''
#Create dictionary
#Collect user input (the key)
#If key starts with subject
#   print subject and course
#   mark that subject exists
#If subject does not exist
#   print error message
''''''

courses = {'COS 2005':'Python Programming', 'COS 2105':'C++ Programming', 'COS 2656':'JavaScript Programming',
           'MAT 2122':'Calculus II', 'MAT 2002':'Calculus I', 'MAT 2232':'Pre-Calculus',
           'SCI 2266':'Chemistry', 'SCI 2215':'Physics', 'SCI 2231':'Biology', 'SCI 2214':'Life Science'}

subject = input('Please enter a subject: ')

found = False

for ID in courses:
    if ID.startswith(subject):
        print(ID, courses[ID])

        found = True

if found == False:
    print('This subject does not exist')