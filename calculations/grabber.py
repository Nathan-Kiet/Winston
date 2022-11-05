import json
#The data structure for what is going to be the grades and the classes
  #* gGrades is the given grade
  #* fgrade is the full grade that you can recieve
  #* weight is the amount that the grades will be mulitpled to create the weighted grade
  #* The method for doing this is grabbing all of the list and then multipling by the weighted area
  #*cName = Class Name
  #* type = class type, 1 = regular, 2 = honors, 3 = ap
  #* level = what level of edu they have, 1 = highschool (Highschool will then allow for checking what class type it is), 2 = college.
  #TODO: Add a if statement to find if they are from college or from highschool
  #TODO: Change redo to status have true false, and none
  #TODO: add farther loops and breakage prevention
  #TODO: Add more stuff for info and stuff
  #TODO: Add Class structure by using objects
  #TODO: Add more stuff to the user add more info and stress test for latancy
  #TODO: Add actually use case (USE a realistic use case of a really good student with sum issues within it)
  #TODO: Give this student 
  #TODO: Research possible array usage within json
grades = {
  1: {
    'work': {
      1 :{
        'aName': 'App Project Lesson 10',
        'date': '11/2/2022',
        'gGrade': False,
        'fGrade': False,
        'redo': False,
        }, 
      2 :{
        'aName': 'Unit 1 Exam',
        'date': '11/14/2022',
        'gGrade': 14,
        'fGrade': 15,
        'redo': False,
        },
      3: {
        'aName': 'Internet Dilemmas Assignment',
        'date': '11/2/2022',
        'gGrade': 24,
        'fGrade': 24,
        'redo': False,
        },
      3: {
        'aName': 'Internet Dilemmas Assignment',
        'date': '11/2/2022',
        'gGrade': 24,
        'fGrade': 24,
        'redo': False,
      },
      },
      'weight': 0.3,
      'type': 'major',
      'topGrade': [],
      'maxGrade': [],
  },
  2: {
    'work': {
      1 :{
        'aName': 'Warmup',
        'date': '11/6/2022',
        'gGrade': 4,
        'fGrade': 5,
        'redo': False,
      },
      2 :{
        'aName': 'PBA',
        'date': '11/1/2022',
        'gGrade': 9,
        'fGrade': 12,
        'redo': False, 
      },
      3 :{
        'aName': 'DBQ',
        'date': '11/5/2022',
        'gGrade': 24,
        'fGrade': 34,
        'redo': False, 
      },
    },
    'weight': 0.7,
    'type': 'minor',
    'topGrade': [],
    'maxGrade': [],
  },
}

user1 = {
  'profile': {
    'name': 'John',
    'level': 1,
    'grade': 10,
  },
  1: {
    1: {
      'grades': {
        1: {
          'work': {
            1 :{
              'aName': 'App Project Lesson 10',
              'date': '11/2/2022',
              'gGrade': False,
              'fGrade': False,
              'redo': False,
              }, 
            2 :{
              'aName': 'Unit 1 Exam',
              'date': '11/14/2022',
              'gGrade': 14,
              'fGrade': 15,
              'redo': False,
              },
            3: {
              'aName': 'Internet Dilemmas Assignment',
              'date': '11/2/2022',
              'gGrade': 24,
              'fGrade': 24,
              'redo': False,
              },
            4: {
              'aName': 'Unit 1 Project - See Rubric',
              'date': '11/2/2022',
              'gGrade': 12,
              'fGrade': 12,
              'redo': False,
              },
            5: {
              'aName': 'Unit 2 Exam',
              'date': '11/2/2022',
              'gGrade': 24,
              'fGrade': 24,
              'redo': False,
              },
            6: {
              'aName': 'Unit 3 Quiz',
              'date': '10/12/2022',
              'gGrade': 10,
              'fGrade': 10,
              'redo': False,
              },
            },
            'weight': 0.3,
            'type': 'major',
            'topGrade': [],
            'maxGrade': []
        },
        2: {
          'work': {
            1 :{
              'aName': 'App Design Reflection Questions',
              'date': '11/6/2022',
              'gGrade': 10,
              'fGrade': 10,
              'redo': False,
            },
            2 :{
              'aName': 'Binary Conversions',
              'date': '11/1/2022',
              'gGrade': 10,
              'fGrade': 10,
              'redo': False, 
            },
            3 :{
              'aName': 'Lession 12 CFU 1',
              'date': '11/5/2022',
              'gGrade': 5,
              'fGrade': 5,
              'redo': False, 
            },
            4: {
              'aName': 'Lesson 4 CFU 1',
              'date': '11/5/2022',
              'gGrade': 5,
              'fGrade': 5,
              'redo': False,
            },
            5: {
              'aName': 'Lesson 5 CFU 3',
              'date': '11/5/2022',
              'gGrade': 5,
              'fGrade': 5,
              'redo': False,
            },
            6: {
              'aName': 'Lesson 9 CFU 3',
              'date': '11/5/2022',
              'gGrade': 5,
              'fGrade': 5,
              'redo': False,
            },
            7: {
              'aName': 'U2 L3 CFU 3',
              'date': '11/6/2022',
              'gGrade': 5,
              'fGrade': 5,
              'redo': False,
            },
            8: {
              'aName': 'U2 Lesson 2 CFU 1',
              'date': '11/5/2022',
              'gGrade': 5,
              'fGrade': 5,
              'redo': False,
            },
            9: {
              'aName': 'U2L4 CFU 3',
              'date': '11/5/2022',
              'gGrade': 5,
              'fGrade': 5,
              'redo': False,
            },
            10: {
              'aName': 'U2L6 CFU 3',
              'date': '11/2/2022',
              'gGrade': 5,
              'fGrade': 5,
              'redo': False,
            },
          },
          'weight': 0.7,
          'type': 'minor',
          'topGrade': [],
          'maxGrade': [],
        },
      },
      'cName': 'COMP SCI',
      'type': 3,
    },
    2: {
      'grades': {
        1: {
          'work': {
            1 :{
              'aName': 'PBD',
              'date': '11/2/2022',
              'gGrade': 12,
              'fGrade': 10,
              'redo': True,
              }, 
            2 :{
              'aName': 'PBA',
              'date': '11/14/2022',
              'gGrade': 15,
              'fGrade': 34,
              'redo': True,
              }, 
            },
            'weight': 0.3,
            'type': 'major',
            'topGrade': [],
            'maxGrade': [],
        },
        2: {
          'work': {
            1 :{
              'aName': 'Warmup',
              'date': '11/6/2022',
              'gGrade': 12,
              'fGrade': 34,
              'redo': False,
            },
            2 :{
              'aName': 'PBA',
              'date': '11/1/2022',
              'gGrade': 9,
              'fGrade': 12,
              'redo': False, 
            },
            3 :{
              'aName': 'DBQ',
              'date': '11/5/2022',
              'gGrade': 24,
              'fGrade': 38,
              'redo': False, 
            },
          },
          'weight': 0.7,
          'type': 'minor',
          'topGrade': [],
          'maxGrade': [],
        },
      },
      'cName': 'Science',
      'type': 1,
    },
    3: {
      'grades': {
        1: {
          'work': {
            1 :{
              'aName': 'PXA',
              'date': '11/2/2022',
              'gGrade': 7,
              'fGrade': 10,
              'redo': True,
              }, 
            2 :{
              'aName': 'PBA',
              'date': '11/14/2022',
              'gGrade': 15,
              'fGrade': 34,
              'redo': True,
              }, 
            },
          'weight': 0.3,
          'type': 'major',
          'topGrade': [],
          'maxGrade': []
        },
        2: {
          'work': {
            1 :{
              'aName': 'Warmup',
              'date': '11/6/2022',
              'gGrade': 4,
              'fGrade': 5,
              'redo': False,
            },
            2 :{
              'aName': 'PBA',
              'date': '11/1/2022',
              'gGrade': 9,
              'fGrade': 12,
              'redo': False, 
            },
            3 :{
              'aName': 'DBQ',
              'date': '11/5/2022',
              'gGrade': 24,
              'fGrade': 34,
              'redo': False, 
            },
          },
          'weight': 0.7,
          'type': 'minor',
          'topGrade': [],
          'maxGrade': [],
        },
      },
      'cName': 'AP HUMAN GEO',
      'type': 1,
    },
  },
}


topGradeLen = 0
maxGradeLen = 0

#*The grade grabber grades all of the grades and then appends them into workable lists.
def gradeGrabber(grades):
  #*these loops go through ad allow for the append to work.
  for i in grades:
    for x in grades[i]['work'].keys():
      #* all of the info is stored within the second layer of the dictionary.
      grades[i]['topGrade'].append(grades[i]['work'][x].get('gGrade'))
      grades[i]['maxGrade'].append(grades[i]['work'][x].get('fGrade'))
      #TODO: add one for redo ablilty      

  return grades 


#* the grabbercheck checks for any other mistakes in the list and if there are any it goes through and gives a fix or it gives a error code.
def checker(user1, topGradeLen, maxGradeLen):
  fullGradeGrabber(user1)
  #loops through the user profile to get access to the above
  for k in user1:
    for i in user1[k]:
      for x in user1[k][i]['grades']:
        print(x)
        for v in user1[i]['grades'][x]:
          topGradeLen = len(user1[k][i]['grades'][x]['topGrade'])
          maxGradeLen = len(user1[k][i]['grades'][x]['maxGrade'])
          comp = topGradeLen - maxGradeLen
          #Error typing
          if len(user1[k][i]['grades'][x]['topGrade']) != len(user1[k][i]['grades'][x]['maxGrade']):
            print("hello")
            if comp < 0:
              #fixes them and adds False to them
              #False means havent been done yet
              while len(user1[k][i]['grades'][x]['topGrade']) < len(user1[k][i]['grades'][x]['maxGrade']):
                user1[k][i]['grades'][x]['topGrade'].append(False)
                #? is the recursion needed?
              checker(user1, topGradeLen, maxGradeLen);
            if comp > 0:
              return True
          else:
            return False
      
          #Returns true error


def fullGradeGrabber(user1):
  for k in user1:
    for i in user1[k]:
      for x in user1[k][i]['grades']:
        for p in user1[k][i]['grades'][x]['work'].keys():
         user1[k][i]['grades'][x]['topGrade'].append(user1[k][i]['grades'][x]['work'][p]['gGrade'])
         user1[k][i]['grades'][x]['maxGrade'].append(user1[k][i]['grades'][x]['work'][p]['fGrade'])
  return user1
  

          


#print(grades)
#checker(user1, topGradeLen, maxGradeLen)




#INFO
#mutiply all of the final grades by there weight.
#todo: add weight to each one of them.


