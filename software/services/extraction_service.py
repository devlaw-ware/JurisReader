import re


def extract_dates(text):

    dates = re.findall(
        r'\d{2}/\d{2}/\d{4}',
        text
    )

    return list(dict.fromkeys(dates))


def extract_values(text):

    values = re.findall(
        r'R\$\s?[\d\.,]+',
        text
    )

    return list(dict.fromkeys(values))


def extract_process_number(text):

    process_number = re.findall(
        r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}',
        text
    )

    return list(dict.fromkeys(process_number))

def extract_parties(text):

    parties = []

    lines = text.split('\n')

    for line in lines:

        if 'REQUERENTE' in line.upper():
            parties.append(line.strip())

        elif 'REQUERIDO' in line.upper():
            parties.append(line.strip())

        elif 'AUTOR' in line.upper():
            parties.append(line.strip())

        elif 'RÉU' in line.upper():
            parties.append(line.strip())

    return list(dict.fromkeys(parties))