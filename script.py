import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Tuple
import logging

EUROMILHOES_URL = "https://www.euromillones.com/pt/resultados/euromilhoes"

logging.basicConfig(level=logging.INFO)

def get_draw_results() -> Dict[str, List[int]]:
    try:
        response = requests.get(EUROMILHOES_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error fetching draw results: {e}")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        draw_date = soup.find('span', class_='main-date-draw').text.strip()
        numbers = [int(ball.text.strip()) for ball in soup.select('span.numbers span.ball-txt')]
        stars = [int(star.text.strip()) for star in soup.select('span.stars span.ball-txt')]
    except AttributeError as e:
        logging.error(f"Error parsing draw results: {e}")
        return {}

    return {
        "date": draw_date,
        "numbers": numbers,
        "stars": stars
    }

def my_personal_keys() -> Dict[str, Dict[str, List[int]]]:
    return {
        'key1': {'number': [10, 15, 22, 33, 45], 'stars': [2, 7]},
        'key2': {'number': [11, 17, 19, 21, 29], 'stars': [3, 9]},
        'key3': {'number': [3, 7, 8, 17, 25], 'stars': [7, 12]},
        'key4': {'number': [13, 21, 23, 30, 43], 'stars': [4, 10]},
        'key5': {'number': [7, 11, 15, 37, 44], 'stars': [7, 11]},
        'key6': {'number': [1, 9, 11, 20, 41], 'stars': [1, 6]},
        'key6': {'number': [9, 14, 18, 21, 30], 'stars': [7, 11]},
    }

def check_results(results: Dict[str, List[int]], personal_keys: Dict[str, Dict[str, List[int]]]) -> Dict[str, Dict[str, int]]:
    output = {}
    for i in range(1, 7):
        key_name = f'key{i}'
        personal_key = personal_keys[key_name]
        matching_numbers = set(results['numbers']) & set(personal_key['number'])
        matching_stars = set(results['stars']) & set(personal_key['stars'])
        output[f'chave_{i}'] = {
            'number': len(matching_numbers),
            'stars': len(matching_stars)
        }
    return output

def check_award(results: Dict[str, Dict[str, int]]) -> str:
    prize_table = {
        (5, 2): "1º Prémio",
        (5, 1): "2º Prémio",
        (5, 0): "3º Prémio",
        (4, 2): "4º Prémio",
        (4, 1): "5º Prémio",
        (3, 2): "6º Prémio",
        (4, 0): "7º Prémio",
        (2, 2): "8º Prémio",
        (3, 1): "9º Prémio",
        (3, 0): "10º Prémio",
        (1, 2): "11º Prémio",
        (2, 1): "12º Prémio",
        (2, 0): "13º Prémio"
    }

    awarded_prizes = []
    for key, result in results.items():
        match_tuple = (result['number'], result['stars'])
        if match_tuple in prize_table:
            key_formatted = key.replace('_', ' ').capitalize()
            prize_text = f"{prize_table[match_tuple]} | {key_formatted} -> {result['number']} números e {result['stars']} estrelas"
            awarded_prizes.append(prize_text)

    if awarded_prizes:
        return "🔵 PRÉMIOS \n" + "\n".join([f"=> {prize}" for prize in awarded_prizes])
    else:
        return "Sem nenhum prémio 😭\n\n"

def format_my_keys(my_keys: Dict[str, Dict[str, List[int]]]) -> str:
    message = "🔵 As nossas chaves:\n"
    for key, values in my_keys.items():
        numbers = " ".join(map(str, values['number']))
        stars = " ".join(map(str, values['stars']))
        message += f"{numbers} + {stars}\n"
    return message

def formatted_response(awards: str, draw_info: Dict[str, List[int]], personal_keys: Dict[str, Dict[str, List[int]]]) -> str:
    draw_numbers = " ".join(map(str, draw_info['numbers']))
    draw_stars = " ".join(map(str, draw_info['stars']))
    message = f"🔵 Resultados do sorteio de {draw_info['date']}\n\n"
    message += f"Números: {draw_numbers}\nEstrelas: {draw_stars}\n\n"
    message += format_my_keys(personal_keys)
    message += f"\n{awards}\n"
    return message

def get_euromilhoes_results_message() -> str:
    draw_info = get_draw_results()
    if not draw_info:
        return "Erro ao obter os resultados do sorteio."

    personal_keys = my_personal_keys()
    keys_results = check_results(draw_info, personal_keys)
    awards = check_award(keys_results)
    result_message = formatted_response(awards, draw_info, personal_keys)
    
    return result_message
