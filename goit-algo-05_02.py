import re
from typing import Callable

def generator_numbers(text:str):
    numbers = re.findall("\d+[\.,]?\d+",text)# , та . означають "або" в цьому виразі, а ? позначає, що попередній символ (, в даному випадку) може відсутній або відомий один раз.        
    for number in numbers:         
        yield float(number)            

def sum_profit(text: str, func: Callable):
    total_income = sum(func(text))
    return total_income

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")



