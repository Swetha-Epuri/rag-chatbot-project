from unittest.mock import MagicMock
from evaluation.answer_evaluator import AnswerEvaluator


def test_parse_valid_json():

    evaluator = AnswerEvaluator.__new__(AnswerEvaluator)

    response = """
    {
        "score": 0.9,
        "reason": "Good answer"
    }
    """

    result =  evaluator._parse_response(response)

    assert result["score"] == 0.9

    assert result["reason"] == "Good answer"

def test_parse_json_with_extra_text():

    evaluator = AnswerEvaluator.__new__(AnswerEvaluator)

    response = """
    Here is the result:
    
    {
        "score": 0.8,
        "reason": "Mostly correct"
    }
    """
    
    result =  evaluator._parse_response(response)
    
    assert result["score"] == 0.8

def test_parse_invalid_json():

    evaluator = AnswerEvaluator.__new__(AnswerEvaluator)
    
    response = ("This is not valid JSON")

    result =  evaluator._parse_response(response)
        
    assert result["score"] == 0.0


    
