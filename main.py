# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this lineSportief2021!

#opdracht1 deel 1 checked

scoorder1='Marco van Basten'
scoorder0='Ruud Gullit'

#opdracht 2 deel 1 checked
goal_0=32
goal_1=54


#opdracht 3 deel 1 # checked
scorers=scoorder0 + " " + str(goal_0)+ "," + scoorder1 + " " + str(goal_1)
print(scorers)

#opdracht 4 deel 1 #dchecked

Report =f'{scoorder0} scored in the {goal_0}nd minute \n'f' {scoorder1}  scored in the {goal_1}th minute'
print(Report)

#part 2

#opdracht 1 deel 2 checked
player='Ruud Gullit' 

#opdracht 2 deel 2 checked

#slicing check
first_name=player[0: player.find(' ')]
print(first_name)

#slicing check andere manier
first_name=player[:player.find(' ')]
print(first_name)

#len
first_name_len=(len(first_name))
print(first_name_len)

#opdracht 3 deel 2 check!!!!

last_name=player[player.find(' ')+1:]
print(last_name)

#len
last_name_len=(len(last_name))
print(last_name_len)

player='Ruud Gullit'
last_name=player[player.find(' ')]
print(last_name)


#opdracht 4 deel 2 

name_short=((first_name[0])+'.'+''+(last_name))
print(name_short)


#opdracht 5 deel 2 checked
chant= (((first_name) + '!' + ' ') *(len(first_name))).strip()
print(chant)


#opdracht 6 
good_chant= ' '!=chant[-1]
print(good_chant)


