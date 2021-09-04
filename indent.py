# x = 0
# while x < 10:
#     print(x)
#     x = x + 1

def get_summ(first_word, second_word, delimiter='&'):
    first_word = str(first_word)
    second_word = str(second_word)
    unite = f"{first_word} {delimiter} {second_word}"
    return unite

print(get_summ("Learn", "Python"))
print (get_summ("Learn", "Python").upper())