import re

def extract_dates(text):

    dates = re.findall(
        r'\d{2}/\d{2}/\d{4}',
        text
    )

    return dates


def extract_values(text):

    values = re.findall(
        r'R\$\s?[\d\.,]+',

        text
    )

    return values