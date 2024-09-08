#!/usr/bin/env python3

# ukol za 2 body
def first_odd_or_even(numbers):
    """Returns 0 if there is the same number of even numbers and odd numbers
       in the input list of ints, or there are only odd or only even numbers.
       Returns the first odd number in the input list if the list has more even
       numbers.
       Returns the first even number in the input list if the list has more odd 
       numbers.

    >>> first_odd_or_even([2,4,2,3,6])
    3
    >>> first_odd_or_even([3,5,4])
    4
    >>> first_odd_or_even([2,4,3,5])
    0
    >>> first_odd_or_even([2,4])
    0
    >>> first_odd_or_even([3])
    0
    """

    odds = []
    evens = []


    for number in numbers:
        if number % 2 == 0:
            odds.append(number)
        else:
            evens.append(number)
    

    if len(odds) == len(evens) or len(odds) == 0 or len(evens) == 0:
        return 0
    elif len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]


# ukol za 3 body
def to_pilot_alpha(word):
    """Returns a list of pilot alpha codes corresponding to the input word

    >>> to_pilot_alpha('Smrz')
    ['Sierra', 'Mike', 'Romeo', 'Zulu']
    """

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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
