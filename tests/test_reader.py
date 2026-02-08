import pytest

from reader import read_csv_file

CSV_CONTENT = """country,year,gdp
United States,2023,300
United States,2022,100
China,2023,50
China,2022,50
Japan,2023,100
"""


def create_csv_file(tmp_path, content):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(content)
    return csv_file


def test_read_csv_file_success(tmp_path):
    file = create_csv_file(tmp_path, CSV_CONTENT)
    results = read_csv_file(file, group_by="country", report_parameter="gdp")

    assert results == {
        "United States": [300, 100],
        "China": [50, 50],
        "Japan": [100],
    }


def test_read_csv_file_invalid_parameter(tmp_path):
    file = create_csv_file(tmp_path, CSV_CONTENT)

    with pytest.raises(ValueError):
        read_csv_file(file, group_by="country", report_parameter="gdpp")


def test_read_csv_file_invalid_group_by(tmp_path):
    file = create_csv_file(tmp_path, CSV_CONTENT)

    with pytest.raises(ValueError):
        read_csv_file(file, group_by="countries", report_parameter="gdp")
