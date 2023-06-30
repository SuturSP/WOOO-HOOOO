import math
import pickle
import os



class Calculator:
    def __init__(self, corpus_dir, idf_file):
        self.corpus_dir = corpus_dir
        self.idf_file = idf_file
        self.idf_values = {}
        if os.path.exists(self.idf_file):
            with open(self.idf_file, 'rb') as f:
                self.idf_values = pickle.load(f)
        else:
            self.calculate_idf()
            with open(self.idf_file, 'wb') as f:
                pickle.dump(self.idf_values, f)

    def imblind(self):
        directory = self.corpus_dir
        files = os.listdir(directory)
        for a in range(1, 1 + len(files)):
            with open(self.corpus_dir + "\\Text" + str(a) + ".txt", 'r') as t:
                text = t.readline().lower()
            text = text.replace(".", "")
            text = text.replace(",", "")
            text = text.replace("!", "")
            text = text.replace("?", "")
            text = text.replace('"', '')
            with open(self.corpus_dir + "\\Text" + str(a) + ".txt", 'w') as t:
                t.flush()
                t.write(text)

    def calculate_idf(self):
        n_total_documents = 0
        word_document_count = {}
        for filename in os.listdir(self.corpus_dir):
            n_total_documents += 1
            document_words = set()
            with open(os.path.join(self.corpus_dir, filename), 'r') as f:
                for line in f:
                    words = line.strip().split()
                    document_words.update(words)
            for word in document_words:
                word_document_count[word] = word_document_count.get(word, 0) + 1
        for word, count in word_document_count.items():
            self.idf_values[word] = math.log(n_total_documents / count)

    def calculate_tf(self, text):
        tf_idf_values = []
        document_words = text.strip().split()
        word_count = len(document_words)
        word_frequency = {}
        for word in document_words:
            word_frequency[word] = word_frequency.get(word, 0) + 1
        for word, frequency in word_frequency.items():
            tf = frequency / word_count
            idf = self.idf_values.get(word, 0)
            tf_idf = tf * idf
            tf_idf_values.append((word, tf_idf))
        return tf_idf_values

calculator = Calculator(corpus_dir='C:\\Users\\79137\\PycharmProjects\\WOOO-HOOOO\\corpus', idf_file='idf_values.pickle')

calculator.imblind()

with open("C:\\Users\\79137\\PycharmProjects\\WOOO-HOOOO\\corpus\\Text2.txt", 'r') as t:
    txt = t.readline()

tf_idf_values = calculator.calculate_tf(txt)
print(tf_idf_values)
