def ReverseWords(words):
    if words==None or len(words)<2:
        return words
    endIndex=len(words)-1
    reversedWords=ReverseAllWords(words)
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

def ReverseAllWords(words):
    endIndex=len(words)-1
    reversedWords=""
    while 0<=endIndex:
        reversedWords+=words[endIndex]
        endIndex-=1
    return reversedWords

def ReverseOneWord(words,beginIndex,endIndex):
    res=""
    while endIndex>=beginIndex:
        res+=words[endIndex]
        endIndex-=1
    return res

def LeftReverseWords(words,index):
    if words==None or len(words)<2:
        return words
    if index<0 or index>len(words)-1:
        return words
    reversedWords=ReverseAllWords(words)
    res=""
    res+=ReverseOneWord(reversedWords,0,len(words)-index-1)
    res+=ReverseOneWord(reversedWords,len(words)-index,len(words)-1)
    return res

a="I am a student."
print(ReverseWords(a))
b="abcdefg"
print(LeftReverseWords(b,2))

