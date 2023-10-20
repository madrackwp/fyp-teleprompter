class ReadText():
    def __init__(self):
        self.readstring = ""
    
    def format(self):
        return f'<p style="color: rgb(213, 225, 163);">{self.readstring}<\p>'
    
    def addWord(self, newWord):
        self.readstring = self.readstring + " " + newWord

    def removeWord(self):
        words = self.readstring.split()
        if len(words) == 0:
            return None
        wordToRemove = words[-1]
        self.readstring = self.readstring[:len(self.readstring)-len(wordToRemove)-1]
        return wordToRemove
    
    def removeSentence(self):
        sentences = self.readstring.split(".")
        print(sentences)
        if len(sentences) == 1 and sentences[0] == "":
            return None
        else:
            sentenceToRemove = sentences[-2]
            # print("FROM READ. TRYING TO REMOVE: " + sentenceToRemove)
            self.readstring = self.readstring[:len(self.readstring)-len(sentenceToRemove)-1]
            return sentenceToRemove

    def addSentence(self, sentenceToAdd):
        self.readstring = self.readstring + " " + sentenceToAdd + "."

    def getRead(self):
        return self.readstring

class UnreadText():
    def __init__(self, unreadString):
        self.unreadstring = unreadString
    def format(self):
        return f'<p style="color: rgb(50, 50, 50)">{self.unreadstring}<\p>'
    
    def removeWord(self):
        if len(self.unreadstring) == 0:
            return None
        words = self.unreadstring.split()
        if len(words) == 0:
            return None
        firstWord = words[0]
        # print("FIRST WORD IS: " + firstWord)
        length = len(firstWord)
        if len(self.unreadstring) > length:
            self.unreadstring = self.unreadstring[length+1 :]
        else:
            self.unreadstring = self.unreadstring[length:]
        return firstWord
    
    def removeSentence(self):
        if len(self.unreadstring) == 0:
            return None
        sentences = self.unreadstring.split(".")
        
        firstSentence = sentences[0]
        words = firstSentence.split()
        if len(words) <= 4: #Meaning the sentence has less than 4 words left
            length = len(firstSentence)
            if len(self.unreadstring) > length:
                self.unreadstring = self.unreadstring[length+1 :]
            else:
                self.unreadstring = self.unreadstring[length:]
            return firstSentence
        else:
            return None
        
    def removeSentenceManual(self):
        if len(self.unreadstring) == 0:
            return None
        sentences = self.unreadstring.split(".")
        if len(sentences) == 0:
            return None
        firstSentence = sentences[0]
        length = len(firstSentence)
        if len(self.unreadstring) > length:
            self.unreadstring = self.unreadstring[length+1 :]
        else:
            self.unreadstring = self.unreadstring[length:]
        return firstSentence

        
        

    def addWord(self, wordToAdd):
        self.unreadstring = wordToAdd + " " + self.unreadstring
    
    def addSentence(self, sentenceToAdd):
        # print("HERE I AM!")
        self.unreadstring = sentenceToAdd + ". " + self.unreadstring
        # print(self.unreadstring)
    
    def getUnread(self):
        return self.unreadstring