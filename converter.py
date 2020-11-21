def input_number():
    global rome_number
    rome_number = str(input('Введите Римское число: ')).upper()

def convert_to_arabic(num):
    total_number = 0
    rome_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = num[::-1]
    last_char = 0
    for i in num:
        curent_char =  rome_dict[i]
        if curent_char >= last_char: total_number += curent_char
        else: total_number -= curent_char
        last_char = curent_char
    return total_number

if __name__ == "__main__":
    input_number()
    print(convert_to_arabic(rome_number))
    