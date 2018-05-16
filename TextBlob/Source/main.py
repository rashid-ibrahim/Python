
from textblob import TextBlob
from textblob import Word

class blobBuilder:
    def __init__(self):
        self.blob = None
        self.sentences = []
        

    def setBlob(self, val):
        self.blob = TextBlob(val)
        self.sentences = self.setSentences()
        

    def getBlob(self):
        return self.blob

    def setSentences(self):
        print(self.blob)
        print(self.blob.sentences)
        self.sentences = self.blob.sentences

    def getSentences(self):
        '''#Get ALL sentences
        print(blob.sentences)
        print('\n')'''
        print('getSentences method')
        print(self.sentences)
        return self.sentences

    def getSentenceWords(self, sent):
        '''#Looping the words.
        for words in sentences[0].words:
            print(words)'''
        return sent.words

    def getSentenceNounPhrases(self, sent):
        ''' #This is slow running.
            for np in sent0.noun_phrases:
                print(np)'''
        return sent.noun_phrases

    
    

def main():
    raw = "Analytics Vidhya is a great platform to learn data science. \n It helps community through blogs, hackathons, discussions, etc."
    bb = blobBuilder()
    bb.setBlob(raw)
    print(bb.getBlob())
    sentences = bb.getSentences()
    print('Sentences:')
    print(sentences)
    print('\n')

    #The sentences by index.
    for i in range(0, len(sentences)):
        print(sentences[i])
    print('\n')

    for i in sentences:
        x = bb.getSentenceWords(i)
        for j in x:
            print(x)
        print('\n')
    print('\n')

    for i in sentences:
        x = bb.getSentenceNounPhrases(i)
        for np in x:
            print(np)
        print('\n')
    print('\n')

    #Tags for parts/types of speech each word is. Full list of types at https://www.clips.uantwerpen.be/pages/mbsp-tags
    for i in sentences:
        for word, tag in i.tags:
            print(word, tag)
        print('\n')
    print('\n')

    for i in sentences:
        print(i.words)
        print(i.words[1])
        print(i.words[1].singularize())
        print('\n')

    for i in sentences:
        for word,pos in i.tags:
            if pos == 'NN':
                print(word.pluralize())

    w = Word('running')
    #This will print 'run'.
    print(w.lemmatize('v'))



if __name__ == '__main__':
    main()
    


