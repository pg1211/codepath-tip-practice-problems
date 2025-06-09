def final_value_after_operations(operations):
    tigger = 1
    for op in operations:
        if op == "bouncy" or op == "flouncy":
            tigger += 1
        if op == "trouncy" or op == "pouncy":
            tigger -= 1

    return tigger


# example usage
operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)

# problem 3


# we want to remove t, i, gg, er
def tiggerfy(word):
    lower_word = word.lower()

    lower_word.replace("t", "")
    lower_word.replace("i", "")
    lower_word.replace("gg", "")
    lower_word.replace("er", "")

    if lower_word == word:
        return lower_word

    return word


print(tiggerfy("Eggplant"))


def tiggerfy_split(word):
    # set new_word to have contents of word
    new_word = word

    # loop through things that we want to remove
    for delimiter in ["t", "i", "gg", "er"]:
        arr = new_word.split(delimiter)
        new_word = "".join(arr)

    return new_word
