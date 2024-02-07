from controllers.frequenctAnalysis import search_wikipedia_topic
import pytest

#Correct response
def test_search_topic() -> None:
    response = search_wikipedia_topic('test')
    # Use pytest assertions to check if the response is a list
    assert isinstance(response, list)
    assert len(response) > 0


# Missing value Correct response
def test_search_topic_exception() -> None:
    with pytest.raises(TypeError) as exc_info:
        response = search_wikipedia_topic()
    # Use pytest assertions to check if the response is a list
    print(str(exc_info.value))
    assert str(exc_info.value) == "search_wikipedia_topic() missing 1 required positional argument: 'search_topic'"