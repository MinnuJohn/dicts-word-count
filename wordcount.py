"""Count words in file."""


# put your code here.
def word_count(filename):
    """Function to print each word in the 
    file with number of times it appear"""
    
    word_cnt = {} #null dictionary
    file = open(filename) #to open file
    for line in file:
        line = line.rstrip()
        words = line.split(" ")
        for word in words:
            word_cnt[word] = word_cnt.get(word,0)+1
    for word,cnt in word_cnt.items():
        print(word,cnt)
        

