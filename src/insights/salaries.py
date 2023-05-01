from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    source_list = read(path)
    salaries = set()

    for salary in source_list:
        if salary['max_salary'].isnumeric():
            salaries.add(int(salary['max_salary']))

    return max(salaries)


def get_min_salary(path: str) -> int:
    source_list = read(path)
    salaries = set()

    for salary in source_list:
        if salary['min_salary'].isnumeric():
            salaries.add(int(salary['min_salary']))

    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])
        match_salary = int(salary)

        if max_salary < min_salary:
            raise ValueError('min_salary is greater than max_salary')
    except Exception:
        raise ValueError('Invalid Numbers')

    return match_salary <= max_salary and match_salary >= min_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass

    return filtered_jobs
