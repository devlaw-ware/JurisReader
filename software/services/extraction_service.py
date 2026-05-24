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

def extract_process_number(text): #funçao para extrair o número do processo judicial do texto 

    process_number = re.findall( #procura padrões no texto que correspondam ao formato do número do processo judicial
        r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}',
        text\
    )
    
    return list(set(process_number))
