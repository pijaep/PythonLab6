ru_dict = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'yo',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'sch',
    'ъ': '',
    'ы': 'y',
    'ь': '',
    'э': 'e',
    'ю': 'yu',
    'я': 'ya'
}


def transliterate(text):
    result = ''

    for char in text:

        if char.lower() in ru_dict:

            if char.isupper():
                result += ru_dict[char.lower()].upper()
            else:
                result += ru_dict[char.lower()]

        else:
            result += char

    return result

russian_text = input('Введите текст:',)
english_text = transliterate(russian_text)
print('Измененный текст:',english_text)