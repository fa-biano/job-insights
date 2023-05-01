from src.pre_built.counter import count_ocurrences


def test_counter():
    file = 'data/jobs.csv'
    count_word1 = 'Finance'
    count_word2 = 'FinAncE'
    count_word3 = 'FINANCE'

    assert count_ocurrences(file, count_word1) == 512
    assert count_ocurrences(file, count_word2) == 512
    assert count_ocurrences(file, count_word3) == 512
