class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + "=" + self.meaning
    
wordslist = []
print("Welcome to flashcard app!")
while True:
    word = input("Enter word: ")
    meaning = input("Enter meaning: ")
    wordslist.append(flashcard(word,meaning))
    option = int(input("Ente 0 to continue, 1 to stop: "))
    if option:
        break

print("flashcards list: ")
for i in wordslist:
    print("*", i)