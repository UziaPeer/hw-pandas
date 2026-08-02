import pytest
from analyze import support_in_one_party_elections, support_in_multi_party_elections, parties_with_different_relative_order
from testcases import parse_testcases

testcases = parse_testcases("testcases.txt")

def run_testcase(party:str):
    if party == "parties_with_different_relative_order":
         return f"{parties_with_different_relative_order()}"
    else:
         return f"{support_in_one_party_elections(party)} {support_in_multi_party_elections(party)}"

@pytest.mark.parametrize("testcase", testcases, ids=[testcase["name"] for testcase in testcases])
def test_cases(testcase):
    actual_output = run_testcase(testcase["input"])
    assert actual_output == testcase["output"], f"Expected {testcase['output']}, got {actual_output}"


def test_new_cases():
    assert support_in_one_party_elections("מחל") >= 0
    assert support_in_multi_party_elections("מחל") >= 0

    result = parties_with_different_relative_order()
    assert result is None or len(result) == 2
