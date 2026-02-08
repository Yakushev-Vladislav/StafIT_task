import pytest

from reports import average, report_method

DATA = {
    "United States": [300, 100],
    "China": [50, 50],
    "Japan": [100],
}


def test_average():
    results = average(DATA)

    assert set(results.keys()) == set(DATA.keys())
    assert results["United States"] == 200
    assert results["China"] == 50
    assert results["Japan"] == 100


def test_report_method_success():
    method = report_method("average")
    assert method is average


def test_report_method_failure():
    with pytest.raises(ValueError):
        report_method("sum")
