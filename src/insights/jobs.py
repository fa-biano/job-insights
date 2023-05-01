from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    dict_file = list()
    with open(path, encoding="utf8") as csvfile:
        file_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in file_reader:
            dict_file.append(row)
    return dict_file


def get_unique_job_types(path: str) -> List[str]:
    job_list = read(path)
    job_type = set()

    for job in job_list:
        job_type.add(job['job_type'])

    return (job_type)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = list()

    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs

# get_unique_job_types("./data/jobs.csv")
