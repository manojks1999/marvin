from services.frequencyAnalysis import search_wikipedia_topic, get_frequecy_by_topic, get_history
from flask import jsonify, request
class InvalidInput(Exception):
    pass

#Controller of search topic response returns all the possible topics available in wikipedia
def searchWikiTopic(request):
    try:
        data = request.get_json()
        topic_name = data.get('topic_name')
        if topic_name == '':
            raise InvalidInput(f'Topic name cannot be empty.')
        result = search_wikipedia_topic(topic_name)
        return jsonify(
            success = True, 
            data = result,
        ), 200
    except Exception as input_error:
        print(f"Error in controller of getting topic name: {input_error}")
        return jsonify(
            success = False, 
            message = 'Invalid input'
            ), 400
    except Exception as error:
        print(f"Error in controller of getting topic name: {error}")
        return jsonify(
            success = False, 
            message = 'Unalbe to process the request'
            ), 500


def wikiTopicAnalysis(request):
    try:
        data = request.get_json()
        topic_name = data.get('topic_name')
        rank = data.get('frequency_rank')
        user_id = request.args.get('user_id')
        if topic_name == '' or rank is None or type(rank) != int:
            raise InvalidInput(f'Topic name cannot be empty.')
        user_id = '700' if user_id is None else user_id
        result = get_frequecy_by_topic(topic_name, rank, user_id)
        return jsonify(
            success = True, 
            data = result,
        ), 200
    except InvalidInput as input_error:
        print(f"Error in controller of search frequency topic name: {input_error}")
        return jsonify(
            success = False, 
            message = 'Invalid input'
            ), 400
    except Exception as error:
        print(f"Error in controller of getting frequency of topic name: {error}")
        return jsonify(
            success = False, 
            message = 'Unalbe to process the request'
            ), 500


def getHistory(request):
    try:
        user_id = request.args.get('user_id')
        user_id = '700' if user_id is None else user_id
        result = get_history(user_id)
        return jsonify(
            success = True, 
            data = result,
        ), 200
    except Exception as input_error:
        print(f"Error in controller of get history: {input_error}")
        return jsonify(
            success = False, 
            message = 'Invalid input'
            ), 400
    except Exception as error:
        print(f"Error in controller of get history: {error}")
        return jsonify(
            success = False, 
            message = 'Unalbe to process the request'
            ), 500