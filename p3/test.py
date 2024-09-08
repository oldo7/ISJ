def first_odd_or_even(word):
    pilot_alpha = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
        'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike',
        'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
        'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']

    pilot_alpha_list = []
     
    for letter in word.lower():
        if ord(letter) < 97 or ord(letter) > 122:
            continue
        pilot_alpha_list.append(pilot_alpha[ord(letter)-97])

    return pilot_alpha_list

print(first_odd_or_even("SmRa z"))