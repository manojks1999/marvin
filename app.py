# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import request
from flask import Flask
from controllers.frequenctAnalysis import searchWikiTopic, wikiTopicAnalysis, getHistory
# Flask constructor takes the name of 
# current module (__name__) as argument.

app = Flask(__name__)
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.


@app.route('/', methods = ['GET'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'Hello Marvin'

# POST API to get topics of wikipedia
@app.route('/search_wikipedia_topics', methods = ['POST'])
def search_wikipedia_topics():
    return searchWikiTopic(request)

# POST API to get word frequency
@app.route('/word_frequency_analysis', methods = ['POST'])
def word_frequency_analysis():
    return wikiTopicAnalysis(request)


# Get API to get history
@app.route('/history', methods = ['GET'])
def get_history():
    return getHistory(request)


# main driver function
if __name__ == '__main__':
	# run() method of Flask class runs the application 
	# on the local development server.
    app.run()
