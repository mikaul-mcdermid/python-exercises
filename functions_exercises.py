def is_two(n):
    if n in (2, '2', 2.0):
        return True
    else:
        return False

def is_vowel(somestring):
    if type(somestring) == str:
        if len(somestring) == 1 and somestring.isalpha(): #checks for single character input and that it is alphabetical
            return somestring.lower() in 'aeiouy' #checks if string is in lowercase
        else:
            return False
    else:
        return False

def is_consonant(letter):
    if len(letter) == 1 and letter.isalpha():
        letter = letter.lower()
        return letter not in 'aeiouyAEIOUY'
    else:
        return False

def uppercase(word):
    if word and word[0].isalpha() and word[0].lower() not in 'aeiou':
        return word[0].upper() + word[1:]
    return word

def calc_tip(tip_percentage, bill_total):
    if 0 <= tip_percentage <= 1:
        tip_amount = tip_percentage * bill_total
        return round(tip_amount,2)
    else:
        return "Invalid tip percentage. Please enter a value between 0 and 1."


def apply_discount(price, discount_percentage):
    if 0 <= discount_percentage <= 100:
        discount = discount_percentage / 100
        discounted_price = price - (price * discount)
        return discounted_price
    else:
        return "Invalid tip percentage. Please enter a value between 0 and 100%."

def handle_commas(number_str):
    number_str = number_str.replace(',','')
    
    if number_str.replace(',','',1).isdigit():
        number = float(number_str)
        return number
    else: return "Invalid input. Please enter a number with or without commas."

def handle_commas(number_str):
    # Remove commas from the input string
    number_str = number_str.replace(',', '')

    # Check if the modified string can be converted to a number
    if number_str.replace('.', '', 1).isdigit():
        number = float(number_str)
        return number
    else:
        return "Invalid input. Please enter a number with or without commas."

def get_letter_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid score, please enter a value between 0 and 100 to receive your letter grade.'

def remove_vowels(input_string):
    vowels = "AEIOUaeiou"
    result_string = "".join(char for char in input_string if char not in vowels)
    return result_string

def normalize_name(input_string):
    # Remove whitespace, convert to lowercase, and replace spaces with underscores
    normalized = input_string.strip().lower().replace(" ", "_")

    # Remove characters that are not valid in a Python identifier
    normalized = ''.join(char for char in normalized if char.isidentifier())

    return normalized

def cumulative_sum(oldlist):
    newlist =[]
    #initialize a variable to store the cumulative sum
    c_sum = 0
    for num in oldlist:
        #add the current number to the cumulative sum
        c_sum += num
        print(f'cumulative: {c_sum}')
        #append the cumulative sum to the new list
        newlist.append(c_sum)
        print(f'newlist: {newlist}')