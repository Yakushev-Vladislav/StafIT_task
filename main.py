import argparse
from collections import defaultdict

from tabulate import tabulate

from reader import read_csv_file
from reports import report_method


def argument_parser():
    """
    Create a command-line interface for reading .csv files.

    Allowed arguments:
        - `--files` -> List of .csv files;
        - `--report` -> Method and parameter in format: `method-parameter`.
    """
    parser = argparse.ArgumentParser(
        description="Generate reports from CSV data.",
        epilog="Example: python main.py --files file1.csv file2.csv "
        "--report average-gdp",
        allow_abbrev=False,
    )
    parser.add_argument(
        "--files", nargs="+", required=True, help="One or more .csv files"
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Method and parameter in format: 'method-parameter'.",
    )
    return parser.parse_args()


def print_report(results: dict, chosen_parameter: str):
    """
    Creates and outputs the report to stdout.
    """
    table = [[k, f"{v:.2f}"] for k, v in results.items()]

    print(
        tabulate(
            table,
            headers=["country", chosen_parameter],
            showindex="always",
            tablefmt="pretty",
        )
    )


def main():
    """
    Entry point of script.

    Parses command-line arguments, reads multiple CSV files, aggregates data
    grouped by a specified key, calculates the chosen report metric (e.g., `average`) for a
    specified parameter (e.g., `gdp`), and prints a formatted table with the results.

    Uses:
        - `argument_parser`: to parse input files and report type.
        - `read_csv_file`: to extract and group data from CSV.
        - `report_method`: to select calculation method (e.g., average).
        - `print_report`: to output result in a readable format.

    Expected CLI usage:
        python main.py --files file1.csv file2.csv --report average-gdp

    Returns:
        None. Outputs the report to stdout.
    """

    # Parse arguments
    args = argument_parser()
    try:
        chosen_method, chosen_parameter = args.report.split("-")
    except ValueError:
        parser = argparse.ArgumentParser()
        raise parser.error("Report must be in format 'method-parameter'")

    chosen_group_key = "country"  # Now is supported only country-key.

    # Read .csv files
    files_data = defaultdict(list)
    for file in args.files:
        temp_file_data = read_csv_file(
            file_path=file,
            group_by=chosen_group_key,
            report_parameter=chosen_parameter.lower(),
        )
        for key, parameter in temp_file_data.items():
            files_data[key].extend(parameter)

    # Formation results
    results = report_method(chosen_method)(files_data)

    # Print report
    print_report(results, chosen_parameter)


if __name__ == "__main__":
    main()
