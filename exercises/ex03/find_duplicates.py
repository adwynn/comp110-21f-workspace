"""Finding duplicate letters in a word."""

__author__ = "730443412"

word = str(input("Enter a word: "))
index: int = 0
comparison: int = index + 1
dulp: bool = False
while index < len(word):
    comparison = index + 1
    while comparison < len(word):
        if word[index] == word[comparison]:
            comparison += 1
            dulp = True
        else:
            comparison += 1
    index += 1 
if dulp == True:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")

            
