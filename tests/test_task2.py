import csv
import requests

from task2.solution import main, HEADERS, URL


def test_response_ok():
    response = requests.get(URL, HEADERS)

    assert response.status_code == 200


def test_script_ok():
    russian_a = "А"

    main(URL, HEADERS)

    with open("beasts.csv", newline="") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

        assert rows[0][0] == russian_a
        assert rows[-1][0] == "Z"
