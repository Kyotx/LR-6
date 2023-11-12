def count_vowel_starting_words(text):
    vowels = "аяуюоеёэиыАЯУЮОЕЁЭИЫ"
    words = text.split()
    count = 0
    for word in words:
        if word and word[0] in vowels:
            count += 1
    return count

input_text = input("Введите текст: ")
word_count = count_vowel_starting_words(input_text)
print(f"Количество слов, начинающихся с гласной: {word_count}")