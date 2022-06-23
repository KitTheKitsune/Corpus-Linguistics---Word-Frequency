# ignore.py
# by Kendrick Smith

def getText():
    infile = open("harry.txt","r")
    allText = infile.read()
    return allText
def inspectWord(theWord,wList,fList):
    tempWord = theWord.rstrip("\"\'.,`;:-!?")
    tempWord = tempWord.lstrip("\"\'.,`;:-!")
    tempWord = tempWord.lower()
    if len(tempWord) < 4:
        
        if tempWord in wList:
            tIndex = wList.index(tempWord)
            fList[tIndex]+=1
        else:
            wList.append(tempWord)
            fList.append(1)
        
def printParallelLists(wList,fList):
    outfile = open("ignore.txt","w")
    for i in range(len(wList)):
        if fList[i] > 10:
            print(wList[i],fList[i], file=outfile)
def main():
    outfile = open("ignore.txt","w")
    wList = []
    fList = []
    myText = getText()
    myWords = myText.split(" ")
    for word in myWords:
        inspectWord(word,wList,fList)
        printParallelLists(wList,fList)           

main()
