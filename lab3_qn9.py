# lab3_qn9.py

def main():
    sentence = input("Enter a sentence: ")
    sentence_split = sentence.split()

    for word in range(0, len(sentence_split)):
        print(f"{sentence_split[word]} (length: {len(sentence_split[word])})")
    
main()
