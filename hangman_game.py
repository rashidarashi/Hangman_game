logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |

'''
print(logo)



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



import random
animal_name = ["cat","goat","horse","cow","elephant","monkey","donkey"]
animal_random = random.choice(animal_name)
# print(animal_random)


animal_hidden = []
for letter in animal_random:
    animal_hidden.append("_")
print(animal_hidden)



life_count = 6
while life_count > 0:
    user_input = input("Enter a letter : ")
    if user_input in animal_random:
        for letter in range(len(animal_random)):
            if animal_random[letter] == user_input:
                animal_hidden[letter] = user_input
        print(animal_hidden)
        if "_" not in animal_hidden:
            print("You Won")
            life_count = 0
        
    else:
        life_count = life_count - 1
        print(stages[life_count])
        if life_count == 0:
            print("Game Over")
            print("The animal is : ",animal_random)


    
    
    