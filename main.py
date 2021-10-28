from random import randint

dictionary_file_name = "dictionary.txt"  # our file
dictionary_handler = open(dictionary_file_name, "r")  # open file for reading


def count_lines(file_handler):
    """
    given file handler returns the number of lines
    :param file_handler: file handler
    :return: total number of lines
    """
    file_handler.seek(0)  # puts the cursor at the beginning
    line_counter = 0
    for _line in file_handler:  # prepend underscore to unused variables (they stop to be grey)
        line_counter += 1
    return line_counter


def get_word_at_line(file_handler, line_number):
    """
    Given file handler and index, returns word at that line
    :param file_handler: file handler (must be open)
    :param line_number: an index from 0 to the last line of the file (N-1),
                        where N is the number of lines of the file
    :return: whole line at index n
    """
    # make sure the cursor is at the beginning of the file
    # Note: .seek() cannot be used to go to a certain line
    file_handler.seek(0)

    # the following for loop is used to skip `line_number` lines
    for _i in range(line_number):
        file_handler.readline()

    # now we need to read the content at line `line_number`
    word_at_line = file_handler.readline().strip()
    return word_at_line


def choose_random_word(file_handler):
    """
    choose random word from a file
    :param file_handler: file handler
    :return: random word
    """
    # Note: Requires to import random
    total_lines = count_lines(file_handler)
    random_word_index = randint(0, total_lines - 1)  # gives index of a random word
    random_word = get_word_at_line(file_handler, random_word_index)
    return random_word


def letter_from_user():
    """
    letter from user
    :return: letter
    """
    letter = input("please give a letter : ")
    return letter


def semi_unknown_word(word, set_of_correct_letters):
    """
    combination of correct letters from user and underscores
    :param word: word
    :param set_of_correct_letters: set of correct letters
    :return: combination of correct letters and underscores
    """
    # string builder pattern
    unknown_word = ""
    for let in word:
        if let in set_of_correct_letters:
            unknown_word += let
        else:
            unknown_word += "_"
    return unknown_word


def hangman_image(errors):
    image = [""" 
     |¬¬¬¬¬
     |  
     |    
     |    
     |   
     |""",
             """
       |¬¬¬¬@
       |  
       |    
       |    
       |   
       |""",
             """
       |¬¬¬¬@
       |  --|--
       |    
       |    
       |   
       | """,
             """
       |¬¬¬¬@
       |  --|--
       |    |
       |    
       |   
       |""",
             """
       |¬¬¬¬@
       |  --|--
       |    |
       |    |
       |   
       |""",
             """
       |¬¬¬¬@
       |  --|--
       |    |
       |    |
       |   / \\
       |"""]
    return image[errors]


def run_hangman():
    correct_letters = set()  # stores correct letters from user
    wrong_letters = set()  # stores wrong letters from user
    secret_word = choose_random_word(dictionary_handler)
    print(semi_unknown_word(secret_word, correct_letters))

    found_word = ""
    max_errors = 5
    #                                   with this we don't count the same error twice
    #                                   and we don't need the variable "number_of_errors"
    while found_word != secret_word and len(wrong_letters) < max_errors:
        current_letter = letter_from_user()

        if current_letter in secret_word:
            correct_letters.add(current_letter)
        else:
            # number_of_errors += 1 # it counts as mistake even if we have done the same mistake before
            wrong_letters.add(current_letter)
            print("sorry the '{}' letter is wrong!".format(current_letter))

        found_word = semi_unknown_word(secret_word, correct_letters)
        print("correct letters : {}".format(correct_letters))
        print("wrong letters {}".format(wrong_letters))
        print(hangman_image(len(wrong_letters)), end=" ")
        print(found_word)

    if found_word == secret_word:
        print("congratulations")
    else:
        print("You are a completely incompetent the word was {} duh!".format(secret_word))


keep_running = True
while keep_running:
    run_hangman()
    answer = input("play again? ").lower().strip()
    yes_answers = ["yes", "y"]
    keep_running = (answer in yes_answers)
