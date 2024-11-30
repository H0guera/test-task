from task3.solution import appearance


def test_appearance_ok(task_3_test_cases):
    for i, test in enumerate(task_3_test_cases):
        test_answer = test["answer"]
        assert (
            appearance(test["intervals"]) == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
