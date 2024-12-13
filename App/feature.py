from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def get_all_query(title, author, text):
    total = title + ' ' + author + ' '  + text
    total = remove_punctuation_stopwords_lemma(total)
    total = [total]
    return total

def remove_punctuation_stopwords_lemma(sentence):
    filter_sentence = ''
    lemmatizer = WordNetLemmatizer()
    stop_words = stopwords.words('english')

    sentence = re.sub(r'[^\w\s]','',sentence)
    words = nltk.word_tokenize(sentence) #tokenization

    words = [w for w in words if not w in stop_words] #removing stopwords
    for word in words:
        filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
    return filter_sentence
