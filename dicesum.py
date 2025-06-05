import random
 
def roll_dice():
    return random.randint(1,6), random.randint(1,6)
 
def check_roll(dice1, dice2):
    sum_dices = dice1 + dice2
    if sum_dices <= 6:
        return f"La suma de tus dados es {sum_dices}. Lamentable"
    elif sum_dices > 6 and sum_dices < 10:
        return f"La suma de tus dados es {sum_dices}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {sum_dices}. Parece una jugada ganadora"
    
    
num1,num2=roll_dice()
result=check_roll(num1,num2)
print(result)