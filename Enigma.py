"""
Noel Desmarais
CS 021D
Final Project: A program that codes a sentence using the method from the WWII German encrypter 'Enigma'
"""

import time


# get input from user
def main():
    print("\n\t-----Welcome to Enigma-----\n")
    plugboard = input("Enter the plugboard settings (Format: WX YZ): ")
    ringSettings = input("Enter the ring setting (3 letters): ")
    plaintext = input("Enter the sentence to encode or decode: ")
    # encode it and then print the results
    outcome = encode(plaintext, ringSettings, plugboard)
    print("\nResult:  " + outcome)
    time.sleep(1)
    # ask to convert to morse code
    answer = input("\nWould you like to convert into Morse Code?\n")
    morse(answer, outcome)


def morse(answer, outcome):
    # Morse Code Dictionary
    morse_dict = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..', }
    # if the user wants to convert it to morse code
    answer = answer.upper()
    if answer == 'Y' or answer == 'YES':
        message = []
        for i in range(0, len(outcome)):  # replace each letter with its corresponding code
            message.append(morse_dict[outcome[i]])
        message = ''.join(message)
        print(message)


# rotating the rotors to the correct starting place
def start_rotors(stop, rotorlist):
    i = rotorlist[0]
    # rotate the lists until they are at the specified location
    while i != stop:
        rotorlist.append(rotorlist.pop(0))
        i = rotorlist[0]
    return rotorlist


def list_plugs(plugset):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    plugset = plugset.upper()
    # check to see if all the plugs are in the alphabet
    plugs = True
    for i in range(0, len(plugset)):
        if plugset[i] not in alphabet:
            plugs = False
    if plugs:
        # make into a list
        plugset = plugset.split()
        # double and reverse the pairs so that they are encoded both ways
        plugset += [x[::-1] for x in plugset]
        return plugset, plugs
    else:
        return plugset, plugs


def sub(plugboard, plaintext, plugs):
    plaintext = plaintext.upper()
    # if we are not bypassing the plugboard then use it
    if plugs:
        plain_edit = []
        for i in range(0, len(plaintext)):
            plain_edit.append(plaintext[i])

        # for each pair, separate the first and second character
        for pair in range(0, len(plugboard)):
            char = plugboard[pair][0]
            switch = plugboard[pair][1]
            # switch each character in the plaintext that matches 'char' with 'switch
            for i in range(0, len(plaintext)):
                if plaintext[i] == char:
                    plain_edit[i] = switch
        plain_edit = ''.join(plain_edit)
    # if we are bypassing then just send the code through as is
    else:
        plain_edit = plaintext

    return plain_edit


def reflector(reflect_dict, rotors1):
    # reflect each input to its corresponding letter
    reflect = reflect_dict[rotors1]
    return reflect


def encode(plaintext, ringSettings, plugboard):
    # alphabet
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Rotor 3 Substitution
    rotor3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z',
              'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
    rotor3Notch = "V"

    # Rotor 2 Substitution
    rotor2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W',
              'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
    rotor2Notch = "E"

    # Rotor 1 Substitution
    rotor1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O',
              'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
    rotor1Notch = "Q"

    # Reflector
    reflect_dict = {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L',
                    'H': 'D', 'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K',
                    'O': 'M', 'P': 'I', 'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W',
                    'W': 'V', 'X': 'J', 'Y': 'A', 'Z': 'T'}

    ringSettings = ringSettings.upper()

    try:
        rotor1_start = ringSettings[0]
        rotor2_start = ringSettings[1]
        rotor3_start = ringSettings[2]
    except:
        ringSettings = "AAA"
        rotor1_start = ringSettings[0]
        rotor2_start = ringSettings[1]
        rotor3_start = ringSettings[2]

    # start each rotor at the correct position
    rotor1 = start_rotors(rotor1_start, rotor1)
    rotor2 = start_rotors(rotor2_start, rotor2)
    rotor3 = start_rotors(rotor3_start, rotor3)

    plugset = list_plugs(plugboard)
    if plugset[1]:
        plaintext = sub(plugset[0], plaintext, plugset[1])
    # alert the user to their mistake
    elif not plugset[1]:
        print("\nPlugboard settings invalid.")
        time.sleep(1)
        print("Bypassing")
        time.sleep(1)
        plaintext = sub(plugset[0], plaintext, plugset[1])

    rotors_output = []
    for i in range(0, len(plaintext)):
        # dont try to encode the spaces or other characters
        if plaintext[i] in alpha:
            # rotate the rotors before each letter goes through
            rotor3.append(rotor3.pop(0))
            if rotor3[0] == rotor3Notch:
                rotor3.append(rotor3.pop(0))
            if rotor2[0] == rotor2Notch:
                rotor2.append(rotor2.pop(0))
            if rotor1[0] == rotor1Notch:
                rotor1.append(rotor1.pop(0))
                rotor2.append(rotor2.pop(0))
            # send each letter through the rotors
            place = alpha.index(plaintext[i])
            rotors3value = rotor3[place]
            place = alpha.index(rotors3value)
            rotors2value = rotor2[place]
            place = alpha.index(rotors2value)
            rotors1value = rotor1[place]

            # reflect the letter to change it and then put it back through the rotors
            reflected = reflector(reflect_dict, rotors1value)
            place = rotor1.index(reflected)
            rotors1 = alpha[place]
            place = rotor2.index(rotors1)
            rotors2 = alpha[place]
            place = rotor3.index(rotors2)
            rotors3 = alpha[place]
            rotors_output.append(rotors3)
    rotors_output = ''.join(rotors_output)
    # only put the code back through the plugs if it is not being bypassed
    if plugset[1]:
        rotors_output = sub(plugset[0], rotors_output, plugset[1])

    return rotors_output


main()