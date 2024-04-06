import random

def get_numbers_ticket(min, max, quantity):
    
    if min < 1 or max >= 1001 or quantity != 6:
        print("Параметри не коректні!")
        return None
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    return list(numbers)

lottery_numbers = get_numbers_ticket(1, 777, 6)
print("Ваші лотерейні числа:", lottery_numbers)
