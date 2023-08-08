"""get_doi
This code is provided for convenience only
and comes with no support or warranty.

The purpose of this script is to demonstrate how to fetch DOIs
for a list of article titles using the CrossRef API.

Usage:
- Replace the contents of `example_input.csv` with your own.
- Run the script using `python get_doi.py`.
"""

import csv
import time
from pathlib import Path

import requests


def get_doi(title):
    """Fetch the DOI for a given title using the CrossRef API."""
    try:
        response = requests.get(
            f"https://api.crossref.org/works?query={title}", timeout=5
        )
        data = response.json()
        if data["message"]["total-results"] > 0:
            return data["message"]["items"][0]["DOI"]
    except requests.exceptions.Timeout:
        print(f"Timeout error fetching DOI for title '{title}'")
    except requests.exceptions.RequestException as error:
        print(f"Error fetching DOI for title '{title}': {error}")
    return None


def main():
    SCRIPT_DIR = Path(__file__).parent
    # Reading the CSV file
    # Replace with your own `citations_data.csv``
    with open(SCRIPT_DIR / "example_input.csv", "r", encoding="utf-8") as csvfile:
        entries = list(csv.DictReader(csvfile))

    # Fetching DOIs
    for entry in entries:
        title = entry["Title"]
        print(f"Fetching DOI for title: {title}")
        doi = get_doi(title)
        entry["DOI"] = doi
        print(f"DOI: {doi}")
        time.sleep(3)  # To avoid hitting the API rate limit

    # Writing back to a new CSV with DOIs
    # Replace with your own `citations_data_with_doi.csv``
    output_filename = "example_output.csv"
    with open(
        SCRIPT_DIR / output_filename, "w", newline="", encoding="utf-8"
    ) as csvfile:
        fieldnames = ["ID", "Title", "DOI"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)

    print(f"Process completed. DOIs saved to {output_filename}.")


if __name__ == "__main__":
    main()
