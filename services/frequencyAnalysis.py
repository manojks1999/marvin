import wikipedia
from collections import Counter
import json
from database.db import add_history, get_db_history


# Excluding the following words from the analysis mainly includes special characters
except_word_config = [
    '#',
    '$',
    'a',
    'b',
    'c',
    '@',
    '*',
    ')'
]
# Search wikipedia topic
def search_wikipedia_topic(search_topic):
    try:
        return wikipedia.search(search_topic)
    except Exception as error:
        print(f"Error in getting topic name: {error}")
        raise error


def summary(topic):
    try:
        return wikipedia.page(topic).content
    except Exception as error:
        print(f"Error in getting topic by name: {error}")
        raise error


def frequencyAnalysis(sentence, n):
    try:
        sentence_list = sentence.split()
        sentence_dict = {}

        #Mapping every word in dictionary Time O(n) Space O(n)
        for word in sentence_list:
            if word not in except_word_config:
                if word in sentence_dict:
                    sentence_dict[word] += 1
                else:
                    sentence_dict[word] = 1
        # Sorting every word in dictionary Time O(nlogn)
        sorted_sentence = sorted(sentence_dict.items(), key = lambda item:item[1], reverse = True)

        counter = Counter(sentence_list)
        mostCommon = counter.most_common(n)
        list_of_dicts = [{'word': t[0], 'frequency': t[1]} for t in mostCommon]
        return list_of_dicts
    except Exception as error:
        print(f"Error in getting topic name: {error}")
        raise error

def add_to_db(user_id, data):
    try:
        add_history(user_id, data)
    except Exception as error:
        print(f"Error in adding history: {error}")
        raise error

def get_frequecy_by_topic(topic_name, top_rank, user_id = '700'):
    try:
        content = summary(topic_name)
        result  = frequencyAnalysis(content, top_rank)
        add_to_db(user_id, json.dumps(result))
        return result
    except Exception as error:
        print(f"Error in getting topic details: {error}")
        raise error

def get_history(user_id):
    try:
        result = get_db_history(user_id)
        res = [{'time': t[1], 'search': json.loads(t[0])} for t in result]
        return res
    except Exception as error:
        print(f"Error in getting history: {error}")
        raise error