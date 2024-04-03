import re

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

def normalize_phone(phone_number):
    normalized_number = re.sub(r'\D', '', phone_number)  
    if normalized_number.startswith('38'):  
        normalized_number = "+" + normalized_number 
    elif normalized_number.startswith('0'):
        normalized_number = "+38" + normalized_number
    return normalized_number

sanitized_numbers = [normalize_phone(num) for num in phone_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)