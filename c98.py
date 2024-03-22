def countWords():
    wordCount = 0
    fileName = input("please enter the file name")
    fileOpen = open(fileName,'r')
    for l in fileOpen:
        words=l.split()
        wordCount = wordCount+ len(words)

    print("no of words are" )
    print(wordCount)


countWords()