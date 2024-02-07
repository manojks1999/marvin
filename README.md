# Marvin

## Installation

Get a pull of repository

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install -r requirements.txt
```
Execute below command to start the server
```bash
flask run
```
## API Documentation
### Getting frequency of words [POST]
Endpoint: 

```default user_id: 700```
```
http://localhost:5000/word_frequency_analysis
```
or

```Optional```
```
http://localhost:5000/word_frequency_analysis?user_id=500
```

Input Parameters (json body):
```
topic_name(String)
```
```
frequency_rank(Integer)
```

Example:
```
{
    "topic_name": "Earth",
    "frequency_rank": "5"
}
```
Response:

```Status Code: 200```
```
{
    "data": [
        {
            "frequency": Integer,
            "word": String
        }
    ],
    "success": Boolean
}
```
```Status Code: 400```
```
{
    "message": String,
    "success": Boolean
}
```
### History of search results

Input Parameters (Type query params):
```
user_id [Optional] default user_id is 700 if not passed
```
Endpoint
```
http://localhost:5000/history
````
or 
```
http://localhost:5000/history?user_id=500
````

Response:
```
{
    "data": [
        {
            "search": [
                {
                    "frequency": 387,
                    "word": "the"
                },
                {
                    "frequency": 348,
                    "word": "of"
                },
                {
                    "frequency": 190,
                    "word": "and"
                },
                {
                    "frequency": 185,
                    "word": "a"
                },
                {
                    "frequency": 174,
                    "word": "to"
                }
            ],
            "time": "2024-02-07 04:46:20"
        }
    ],
    "success": true
}
```

### If any of topic not found use below url [POST]
```
http://localhost:5000/search_wikipedia_topics
```
Parameter:
```
{
    "topic_name": "Earth"
}
```
Response:
```
{
    "data": [
        "Earth",
        "Google Earth",
        "Moon",
        "Flat Earth",
        "Earth Day",
        "Earth–Moon–Earth communication",
        "Not of This Earth",
        "The Earth Is ...",
        "Near-Earth object",
        "Salt of the earth"
    ],
    "success": true
}
```

### Unit Testing
```bash
pytest
```

