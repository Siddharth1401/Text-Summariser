from gensim.summarization.summarizer import summarize

with open('C:/Users/rambo/Desktop/Document.txt', 'r') as file:
    text2 = file.read()

summ_split = summarize(text2, split=True, ratio=0.1)
print("\n")
print(summ_split)    
print("\n")