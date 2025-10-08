import pytest
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

def test_get_options_ratio():
    assert get_options_ratio(9, 10) == 0.9
    assert get_options_ratio(5, 20) == 0.25

    with pytest.raises(ValueError):
        get_options_ratio(1, 0)

def test_get_faculty_rating():
    assert get_faculty_rating(0.95) == "Excellent"
    assert get_faculty_rating(0.85) == "Very Good"
    assert get_faculty_rating(0.75) == "Good"
    assert get_faculty_rating(0.65) == "Needs Improvement"
    assert get_faculty_rating(0.5) == "Unacceptable"

    with pytest.raises(ValueError):
        get_faculty_rating(1.2)

    with pytest.raises(ValueError):
        get_faculty_rating(-0.1)
