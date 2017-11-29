## Names ##
# Part 1 #

students = [
     {'first_name' :  'Michael',     'last_name' : 'Jordan'},
     {'first_name' : 'John',         'last_name' : 'Rosales'},
     {'first_name' : 'Mark',         'last_name' : 'Guillen'},
     {'first_name' : 'KB',           'last_name' : 'Tonel'}
]
for student in students: ## For the singular in the plural ##
    print student['first_name'], student['last_name'] ## or use + "" + to join them ##

# Part 2 #

users = {
 'Students': [
     {'first_name' : 'Michael',     'last_name' : 'Jordan'},
     {'first_name' : 'John',        'last_name' : 'Rosales'},
     {'first_name' : 'Mark',        'last_name' : 'Guillen'},
     {'first_name' : 'KB',          'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael',     'last_name' : 'Choi'},
     {'first_name' : 'Martin',      'last_name' : 'Puryear'}
  ]
 }

sCount=0

print "Students"

for sUser in users["Students"]:                             ##
    sCount = sCount +1                                      ##
    firstLength = len(sUser["first_name"])                  ##
    lastLength = len(sUser["last_name"])                    ##
    print sCount, "-",  sUser["first_name"], sUser["last_name"], "-", firstLength+lastLength ##

iCount=0

print "Instructors"

for iUser in users["Instructors"]:
    iCount = iCount +1
    firstLengthIns = len(iUser["first_name"])
    lastLengthIns = len(iUser["last_name"])
    print iCount, "-", iUser["first_name"], iUser["last_name"], "-", firstLengthIns+lastLengthIns