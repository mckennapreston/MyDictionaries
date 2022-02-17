
def main():
    infile = open('AI.txt', 'r')

    import re
    string = open("AI.txt").read()
    NewString = re.sub('[^a-zA-z0-9\n.]', ' ',string)

    open("AI.txt", "w").write(NewString)

    WordFrequency = {}

    for line in infile:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        line = line.rstrip
        
    
    for word in words:
        if word in WordFrequency:
            WordFrequency[word] = WordFrequency[word] + 1
        else:
            WordFrequency[word] = 1
    WordFrequency[word]

    print(WordFrequency)

main()