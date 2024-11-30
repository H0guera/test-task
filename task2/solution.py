import csv
import logging

import requests
from bs4 import BeautifulSoup

URL = (
    "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:"
    "%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

logger = logging.getLogger("__name__")


def main(url: str, headers: dict[str, str]) -> None:
    letter = None
    letter_counter = 0
    result_rows = []

    try:
        while url:
            response = requests.get(url, headers=headers)
            if not response.status_code == 200:
                logger.error(
                    "Unexpected response from url:%s. Status code: %s."
                    % (url, response.status_code)
                )
                break

            soup = BeautifulSoup(response.text, "lxml")

            target_div = soup.find(id="mw-pages")
            divs_of_letters = target_div.find_all(class_="mw-category-group")

            if next_page := target_div.find(string="Следующая страница"):
                next_page_href = next_page.find_parent("a").get("href")
                url = "https://ru.wikipedia.org" + next_page_href
            else:
                url = None

            for div in divs_of_letters:
                current_letter = div.find("h3").string

                if letter != current_letter:
                    if letter:
                        result_rows.append((letter, letter_counter))
                        logger.warning(f"{letter},{letter_counter}")
                    letter = current_letter
                    letter_counter = 0
                letter_counter += len(div.find_all("a"))

            if not next_page:
                logger.warning(f"{letter},{letter_counter}")
                result_rows.append((letter, letter_counter))

    finally:
        logger.warning(
            "Process finished with rows from '%s' to '%s'"
            % (result_rows[0][0], result_rows[-1][0])
        )
        with open("beasts.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(result_rows)


if __name__ == "__main__":
    main(URL, HEADERS)
