# Write your solution here
def dict_of_numbers() -> dict:
    spelled_numbers = {
        'ones': ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
        'tens': ["", ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'],
                    'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    }
    numbers = {}
    for number in range(0, 100):
        
        if number < 10:
            numbers[number] = spelled_numbers['ones'][number]
        else:
            tens, ones = map(int, str(number))
            if tens == 1:
                numbers[number] = spelled_numbers['tens'][tens][ones]
            else:
                if ones == 0:
                    numbers[number] = spelled_numbers['tens'][tens]
                else:
                    numbers[number] = f"{spelled_numbers['tens'][tens]}-{spelled_numbers['ones'][ones]}"
    return numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    
    for number in numbers.values():
        print(number)