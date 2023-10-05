from gensim.summarization.summarizer import summarize

with open('C:/Users/rambo/Desktop/Document.txt', 'r') as file:
    text2 = file.read()
print("\n")
summ = summarize(text2, ratio=0.8)
print('\n')
print("Summary using Gensim")
print('\n')
print(summ)
print("\n")