# prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
# new_list = [number ** 2 for number in prev_list if number < 0]
# print(new_list)

sentence = 'My name is Elshed'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)