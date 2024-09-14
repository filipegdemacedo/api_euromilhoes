import requests
from bs4 import BeautifulSoup

def get_draw_results():
    url = "https://www.euromillones.com/pt/resultados/euromilhoes"
    
    response = requests.get(url)
    html_content = response.text  # Make sure this is text, not bytes
    
    soup = BeautifulSoup(html_content, 'html.parser')

    draw_date = soup.find('span', class_='main-date-draw').text.strip()
    numbers = [int(ball.text.strip()) for ball in soup.select('span.numbers span.ball-txt')]
    stars = [int(star.text.strip()) for star in soup.select('span.stars span.ball-txt')]

    return {
        "date": draw_date,
        "numbers": numbers,
        "stars": stars
    }

def my_personal_keys():
    output = {
        'key1': {
            'number': [10, 15, 22, 33, 45],
            'stars': [2, 7]
        },
        'key2': {
            'number': [11, 17, 19, 21, 29],
            'stars': [3, 9]
        },
        'key3': {
            'number': [3, 7, 8, 17, 25],
            'stars': [7, 12]
        },
        'key4': {
            'number': [13, 21, 23, 30, 43],
            'stars': [4, 10]
        },
        'key5': {
            'number': [7, 11, 15, 37, 44],
            'stars': [7, 11]
        },
        'key6': {
            'number': [1, 9, 11, 20, 41],
            'stars': [1, 6]
        }
    }
    
    return output

def check_results(results, personal_keys):
    output = {}
    
    # Loop through each key
    for i in range(1, 7):
        key_name = f'key{i}'
        personal_key = personal_keys[key_name]
        
        # Count matching numbers
        matching_numbers = set(results['number']) & set(personal_key['number'])
        matching_stars = set(results['stars']) & set(personal_key['stars'])
        
        # Store the results for each key
        output[f'chave_{i}'] = {
            'number': len(matching_numbers),
            'stars': len(matching_stars)
        }
    
    return output

def check_award(results):
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
            awarded_prizes.append(prize_table[match_tuple])
            awarded_prizes_new = {
                'key': key,
                'result': prize_table[match_tuple]
            }
    
    if awarded_prizes:
        formatted_awards = "\n".join([f"=> {prize}" for prize in awarded_prizes])
        return f"\n🔵 PRÉMIOS \n\n{formatted_awards}\n\n"
    else:
        return "Sem nenhum prémio 😭\n\n"

def format_my_keys(my_keys):
    print("🔵 As nossas chaves:\n")
    
    for key, values in my_keys.items():
        numbers = " ".join(map(str, values['number']))
        stars = " ".join(map(str, values['stars']))
        print(f"{numbers} + {stars}")

def formatted_response(awards, get_draw_info, personal_keys, draw_numbers, draw_stars):
    print(f"🔵 Resultados do sorteio\n{get_draw_info['date']}\n")
    print(f"Números: {draw_numbers}\nEstrelas: {draw_stars}\n")
    format_my_keys(personal_keys)
    print(awards)

def get_euromilhoes_results():
    get_draw_info = get_draw_results()
    draw_numbers = get_draw_info['numbers']
    draw_stars = get_draw_info['stars']

    draw_results = {
        'number': draw_numbers,
        'stars': draw_stars
    }

    personal_keys = my_personal_keys()
    keys_results = check_results(draw_results, personal_keys)
    awards = check_award(keys_results)
    formatted_response(awards, get_draw_info, personal_keys, draw_numbers, draw_stars)

get_euromilhoes_results()