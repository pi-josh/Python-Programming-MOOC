# Write your solution here
from datetime import datetime

def is_it_valid(pic: str) -> bool:
    # check if length is valid
    if len(pic) != 11:
        return False
    
    # partition the pic
    date_of_birth = pic[:6]
    marker = pic[6]
    personal_id = pic[7:10]
    control_character = pic[10]
    
    # check if half of code is a valid date
    dd, mm, yy = int(date_of_birth[0:2]), int(date_of_birth[2:4]), date_of_birth[4:6]
    if marker == '+':
        year = int("18" + yy)
    elif marker == '-':
        year = int("19" + yy)
    elif marker == 'A':
        year = int("20" + yy)
    else:
        return False
    
    try:
        birth_date = datetime(year, mm, dd)
    except ValueError:
        return False
    
    # check if control character is valid
    control_characters = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    nine_digit_number = int(date_of_birth + personal_id)
    index = nine_digit_number % 31
    
    if control_characters[index] == control_character:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))