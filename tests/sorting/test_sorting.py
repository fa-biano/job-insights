import pytest
from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {'min_salary': 100, 'max_salary': 1000, 'date_posted': '2023-01-21'},
        {'min_salary': 300, 'max_salary': 3000, 'date_posted': '2022-12-25'},
        {'min_salary': 200, 'max_salary': 2000, 'date_posted': '2023-04-20'},
    ]

    sorted_by_max = [
        {'min_salary': 300, 'max_salary': 3000, 'date_posted': '2022-12-25'},
        {'min_salary': 200, 'max_salary': 2000, 'date_posted': '2023-04-20'},
        {'min_salary': 100, 'max_salary': 1000, 'date_posted': '2023-01-21'},
    ]

    sorted_by_min = [
        {'min_salary': 100, 'max_salary': 1000, 'date_posted': '2023-01-21'},
        {'min_salary': 200, 'max_salary': 2000, 'date_posted': '2023-04-20'},
        {'min_salary': 300, 'max_salary': 3000, 'date_posted': '2022-12-25'},
    ]
    sorted_by_date = [
        {'min_salary': 200, 'max_salary': 2000, 'date_posted': '2023-04-20'},
        {'min_salary': 100, 'max_salary': 1000, 'date_posted': '2023-01-21'},
        {'min_salary': 300, 'max_salary': 3000, 'date_posted': '2022-12-25'},
    ]

    sort_by(jobs, 'max_salary')
    assert jobs == sorted_by_max

    sort_by(jobs, 'min_salary')
    assert jobs == sorted_by_min

    sort_by(jobs, 'date_posted')
    assert jobs == sorted_by_date

    with pytest.raises(ValueError):
        sort_by(jobs, 'invalid')
