from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = 'tests/mocks/brazilians_jobs.csv'
    job_list = read_brazilian_file(path)

    for job in job_list:
        assert 'title' in job
        assert 'salary' in job
        assert 'type' in job
