import requests, json

FILE_URL = 'https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt'
RANDOM_ORG_APIKEY = 'e8064aca-afb3-4bbd-9c54-058ae61802b2'


def roll_five_dices():
    payload = {
        'jsonrpc': '2.0',
        'method': 'generateIntegers',
        'params': {
            'apiKey': RANDOM_ORG_APIKEY,
            'n': 5,
            'min': 1,
            'max': 6,
            'replacement': True
        },
        'id': 1000
    }

    headers = {
        'content-type': 'application/json'
    }

    response = requests.post('https://api.random.org/json-rpc/1/invoke', headers=headers, data=json.dumps(payload))
    array_of_dices = response.json()['result']['random']['data']
    return ''.join(str(number) for number in array_of_dices)

def generate_words_dict():
    response  = requests.get(FILE_URL)
    numbers_words_array = response.text.strip().split('\n')
    words_dict = {}

    for line in numbers_words_array:
       splitted_line = line.split('\t')
       words_dict[splitted_line[0]] = splitted_line[1]

    return words_dict

chosen_word_list = []
words_dict = generate_words_dict()

for i in range(1,7):
    number = roll_five_dices()
    chosen_word_list.append(words_dict[number])

print(' '.join(chosen_word_list))
