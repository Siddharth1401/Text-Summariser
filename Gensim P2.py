from gensim.summarization.summarizer import summarize

with open('C:/Users/rambo/Desktop/Document.txt', 'r') as file:
    text2 = file.read()

summ_word_count = summarize(text2, word_count=100)
print("\n")
print(summ_word_count)
print("\n")