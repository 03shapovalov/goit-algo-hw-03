import random

def get_numbers_ticket(min, max, quantity):
    
    if max - min + 1 < quantity:
        print("Параметри не коректні!")
        return None
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    return list(numbers)

lottery_numbers = get_numbers_ticket(1, 98, 12)
print("Ваші лотерейні числа:", lottery_numbers)

# надіюся це вже буде правильно ... надіюся)))