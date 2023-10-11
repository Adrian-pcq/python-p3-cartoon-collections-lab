def roll_call_dwarves(dwarves):
    i=1
    for dwarve in dwarves:
        print(f"{i}. {dwarve}")
        i+=1

def summon_captain_planet(list):
    return [word.title() + "!" for word in list]

def long_planeteer_calls(list):
    for word in list: 
        if len(word)>4:
            return True
    return False 

def find_the_cheese(list):
    for food in list:
        if food == "cheddar":
            return food
    return None 