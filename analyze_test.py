import pytest
import re
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
    expected = testcase["output"]
    if expected.startswith("/") and expected.endswith("/i"):
        assert re.fullmatch(expected[1:-2], actual_output, re.I)
    else:
        assert actual_output == expected, f"Expected {expected}, got {actual_output}"

def test_new_cases():
    assert support_in_one_party_elections("מחל") >= 0
    assert support_in_multi_party_elections("מחל") >= 0

    result = parties_with_different_relative_order()
    assert result is None or len(result) == 2
