import csv
from collections import defaultdict


def read_csv_file(
    file_path: str, group_by: str = "country", report_parameter: str = "gdp"
) -> dict[str, list[float]]:
    """
    Read csv file.

    Default parameters:
        - `group_by`: 'country'.
        - `report_parameter`: 'gdp'.

    Return dict in format:
        - {`group_by`: list of `report_parameters`}.
    """
    result_data = defaultdict(list)

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        # Validation columns
        if group_by not in reader.fieldnames:
            raise ValueError(
                f"Column '{group_by}' not found in the .csf file. "
                f"Available columns: {reader.fieldnames}"
            )
        if report_parameter not in reader.fieldnames:
            raise ValueError(
                f"Column '{report_parameter}' not found in the .csf file. "
                f"Available columns: {reader.fieldnames}"
            )
        # Formatting data
        for row in reader:
            key = row.get(group_by, "")
            value = float(row.get(report_parameter, "0"))
            result_data[key].append(value)

    return result_data
