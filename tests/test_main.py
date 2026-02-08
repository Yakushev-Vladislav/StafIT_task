import subprocess
import sys

from main import main

CSV_CONTENT = """country,year,gdp
United States,2023,300
United States,2022,100
China,2023,50
China,2022,50
Japan,2023,100
"""


def test_run_main(monkeypatch, tmp_path, capsys):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(CSV_CONTENT)

    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--files", str(csv_file), "--report", "average-gdp"],
    )

    main()

    captured = capsys.readouterr()
    assert "United States" in captured.out


def test_main_success(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(CSV_CONTENT)

    results = subprocess.run(
        [
            sys.executable,
            "main.py",
            "--files",
            str(csv_file),
            "--report",
            "average-gdp",
        ],
        capture_output=True,
        text=True,
    )

    assert results.returncode == 0
    assert "United States" in results.stdout
    assert "China" in results.stdout
    assert "Japan" in results.stdout
    assert "200.00" in results.stdout
    assert "50.00" in results.stdout
    assert "100.00" in results.stdout


def test_main_invalid_1(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(CSV_CONTENT)

    results = subprocess.run(
        [
            sys.executable,
            "main.py",
            "--files",
            str(csv_file),
            "--report",
            "average",  # Invalid format
        ],
        capture_output=True,
        text=True,
    )

    assert results.returncode == 2
    assert "format" in results.stderr.lower()


def test_main_invalid_2(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(CSV_CONTENT)

    results = subprocess.run(
        [
            sys.executable,
            "main.py",
            "--file",  # Invalid argument
            str(csv_file),
            "--report",
            "average-gdp",
        ],
        capture_output=True,
        text=True,
    )

    assert results.returncode == 2
    assert "usage:" in results.stderr.lower()
