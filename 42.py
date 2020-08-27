def ReverseWords(words):
    if words==None or len(words)<2:
        return words
    endIndex=len(words)-1
    reversedWords=""
    while 0<=endIndex:
        reversedWords+=words[endIndex]
        endIndex-=1
    beginIndex=0
    #endIndex=0
    result=""
    for i in range(0,len(reversedWords)):
        if reversedWords[i]==' '  :
            result+=ReverseOneWord(reversedWords,beginIndex,i-1)
            result+=' '
            beginIndex=i+1
        elif i==len(reversedWords)-1:
            result+=ReverseOneWord(reversedWords,beginIndex,i)
            beginIndex=i+1
    return result


def ReverseOneWord(words,beginIndex,endIndex):
    res=""
    while endIndex>=beginIndex:
        res+=words[endIndex]
        endIndex-=1
    return res

a="I am a student."
print(ReverseWords(a))

