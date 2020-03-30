import string
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer

stop_words = set(stopwords.words('english'))


def Clean(Data):
    lancaster = LancasterStemmer()
    i = 0
    for s in Data:
        s = s.lower()  # Lower case
        translator = str.maketrans("", "", string.punctuation)
        s = s.translate(translator)  # Remove Punctuation
        s = ''.join([i for i in s if not i.isdigit()])  # Remove numeric data
        x = s
        x = x.split()
        for v in range(len(x)):
            x[v] = lancaster.stem(x[v])
        x = " ".join(x)
        Data[i] = x
        i += 1
    return Data
