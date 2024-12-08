vowel = 'aeiou'
consonant = 'bcdfghjklmnpqrstvwxyz'

word = input('Vvedite clovo: ').lower()

vowel_count = 0
consonant_count = 0

for char in word:
    if char in vowel:
        vowel_count += 1
    elif char in consonant:
        consonant_count += 1
    elif (word != vowel) and (word != consonant):
        print('false')

print(f'kolichestvo glasnyh: {vowel_count}',f'kolichestco soglasnyh: {consonant_count}')