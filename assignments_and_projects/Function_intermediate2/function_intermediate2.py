x = [[5,2,3],[10,8,9]]
x[1][0] = 15
print(x)
students = [{'first_name': 'Michael','last_name':'Jordan'},
            {'first_name': 'John','last_name':'Roasales'}
]
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan','James','Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)
z = [{'x':10, 'y':20} ]
z[0]['y']=30
#################
students = [
          {'first_name':'Micheal','last_name':'Jorden'},
          {'first_name':'John','last_name':'Rosales'},
          {'first_name':'Mark','last_name':'Guillen'},
          {'first_name':'KB','last_name':'Tonel'},
]
def iteratDictionary(some_list):
    for x in range(len(some_list)):
        print(f"first_name - {some_list[x]['first_name']},last_name - {some_list[x]['last_name']}")
   
iteratDictionary(students)

####################

def iteratDictionary2(key_name,some_list):
    for x in range(len(some_list)):
        print(f"{some_list[x][key_name]}")
            
iteratDictionary2('first_name', students)
iteratDictionary2('last_name', students)

####################
dojo={
    'locations':['san Jose','seattle','Dallas','chicago','Tulsa','DC','Burbank'],
    'instructors':['Michael','Amy','Eduardo','Josh','Graham','Patrick','Minh','Devon']
}
def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for x in some_dict[key]:
            print(x)
printInfo(dojo)