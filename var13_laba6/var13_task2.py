def extract_and_convert_to_number(text):
    number_str = ""
    for char in text:
        if char.isdigit() or char == ".":
            number_str += char
        elif number_str:
            break
    if number_str:
        return float(number_str)
    else:
        return "Число не найдено"

input_text = input("Введите текст: ")
number = extract_and_convert_to_number(input_text)
print(f"Извлеченное число: {number}")