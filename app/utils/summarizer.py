import nltk
import heapq

# Once downloaded, you cant comment these lines
nltk.download('stopwords')
nltk.download('punkt')

def token(text):
    word_list = nltk.word_tokenize(text)
    return word_list

def sent_token(text):
    sent_list = nltk.sent_tokenize(text)
    return sent_list

def remove_stopwords(word_list):
    stopwords = set(nltk.corpus.stopwords.words('english'))
    filtered_words = []

    for word in word_list:
        if word not in stopwords:
            filtered_words.append(word)

    return filtered_words

def word_freq(filtered_words):
    word_frequency = {}

    for word in filtered_words:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1

    return word_frequency


def max_freq(word_frequency):
    max_freq = max(word_frequency.values())

    for word in word_frequency.keys():
        word_frequency[word] = (word_frequency[word]/max_freq)

    return word_frequency


def sentence_scores(sent_list, word_frequency):
    sent_scores = {}

    for sentence in sent_list:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequency.keys():
                if len(sentence.split(' ')) < 30:
                    if sentence not in sent_scores.keys():
                        sent_scores[sentence] = word_frequency[word]
                    else:
                        sent_scores[sentence] += word_frequency[word]

    return sent_scores


def get_summary(sent_scores):
    summary = heapq.nlargest(7, sent_scores, key=sent_scores.get)

    return summary
