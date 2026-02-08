def average(data: dict[str, list[float]]) -> dict[str, float]:
    """
    Calculate average of `report_parameter`.

    Return dict with average `report_parameter` in format:
        - {`key`: average `report_parameter`}.
    """
    result = {}

    for key, value in data.items():
        result[key] = sum(value) / len(value)

    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))


REPORTS = {
    "average": average,
}


def report_method(method: str = "average"):
    """
    Formation of the calculation method for the report.
    """
    try:
        return REPORTS[method.lower()]
    except KeyError:
        raise ValueError(
            f"Method {method} is not supported."
            f" Use one of valid methods: {list(REPORTS.keys())}."
        )
