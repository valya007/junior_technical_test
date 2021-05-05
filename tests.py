import pytest
import webapp

def test_nouns_transform1():
    sentence = "This is the test for the task."
    response = ["test", "task"]
    assert webapp.nouns_transform(sentence) == response

def test_nouns_transform2():
    sentence = "I'd like to go to the cinema"
    response_correct = ["cinema"]
    response_incorrect = ["I"]
    assert webapp.nouns_transform(sentence) == response_correct
    assert webapp.nouns_transform(sentence) != response_incorrect

def test_render_template1():
    input_dict = {"test_variable":""}
    return_data = webapp.render_template('test pages/test.html', input_dict)
    assert return_data == "<title></title>"

def test_render_template2():
    input_dict = {"test_variable":"dog,cat,elephant"}
    return_data = webapp.render_template('test pages/test.html', input_dict)
    assert return_data == "<title>dog,cat,elephant</title>"

def test_main():
    environ = {"QUERY_STRING":"", "PATH_INFO":"/abc"}
    def start_response(status,headers):
        expected_status = "200 OK"
        assert int(headers[1][1]) == 128 #error page size
        assert status == expected_status
    return_data = webapp.main(environ, start_response)