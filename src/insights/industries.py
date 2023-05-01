from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industry_list = read(path)
    industry_types = set()

    for industry in industry_list:
        if industry['industry']:
            industry_types.add(industry['industry'])

    return industry_types


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_jobs = list()

    for job in jobs:
        if job['industry'] == industry:
            filtered_jobs.append(job)

    return filtered_jobs
