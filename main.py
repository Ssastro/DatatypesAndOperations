# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this lineSportief2021!

#opdracht1 deel 1

scoorder1 = ' Marco Van Basten'
scoorder0= ' Ruud Gullit'


#opdracht 2 deel 1
goal_0=32
goal_1=54


#opdracht 3 deel 1 # check 
scorers=scoorder0 + str(goal_0), scoorder1 + str(goal_1)


#opdracht 4 deel 1 #deze gecheckt

second ='nd'
third ='th'
Report =f'{scoorder0}' + ' scored in the ' +f'{goal_0}'  + f'{second}' + ' minute ' '\n'+f'{scoorder1}' + ' scored in the ' +f'{goal_1}' +f'{third}' + ' minute'

  




#part 2

#opdracht 1 deel 2
player= 'Ruud Gullit' 

#opdracht 2 deel 2

#find
mystring="Ruud Gullit"
print(mystring.find("Ruud"))

#slicing check
first_name=player[0:5]

#opdracht 3 deel 2 check!!!!

#find
mystring="Ruud Gullit"
print("The position of Gullit using find()is at:", mystring.find("Gullit"))

#len
last_name_len='Gullit'
print(last_name_len,len(last_name_len))

#slicing
last_name=player[6:]
print(last_name)

#opdracht 4 deel 2 

name_short=((first_name[0:5])+ ' '+ (last_name))
print(name_short)


#opdracht 5 deel 2 
chant= ((first_name) + '!' + ' ') *(len(first_name))


#opdracht 6 
good_chant= (' '!=chant.strip()[-1])
print(good_chant)



