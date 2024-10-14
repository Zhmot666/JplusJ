# Объединение одинаковых записей

import json


def merge_duplicate_objects(data):
    """
    Объединяет объекты с одинаковым значением 'ils' в списке данных.

    Args:
        data (list): Список объектов JSON.

    Returns:
        tuple: Кортеж из обработанного списка объектов, количества объединений и списка объединенных 'ils'.
    """
    merged_data = {}
    merge_count = 0
    merged_ils = []  # Список для хранения объединенных 'ils'
    for item in data:
        ils = item['ils']
        if ils in merged_data:
            merged_data[ils]['r31'].extend(item['r31'])
            merged_data[ils]['r32'].extend(item['r32'])
            merge_count += 1
            merged_ils.append(ils)  # Добавляем 'ils' в список объединенных
        else:
            merged_data[ils] = item
    return list(merged_data.values()), merge_count, merged_ils


def process_json_file(file_path, output_path):
    """
    Обрабатывает JSON файл, объединяет дубликаты и записывает результат.

    Args:
        file_path (str): Путь к входному JSON файлу.
        output_path (str): Путь к выходному JSON файлу.
    """
    with open(file_path, 'r', encoding='cp1251') as infile:
        data = json.load(infile)

    merged_data, merge_count, merged_ils = merge_duplicate_objects(data['data'])
    data['data'] = merged_data

    with open(output_path, 'w', encoding='cp1251') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)

    print(f"Количество объединений: {merge_count}")
    print(f"Объединенные 'ils': {', '.join(merged_ils)}")  # Выводим список объединенных 'ils'


# Замените 'endfile.json' и 'merged_file.json' на реальные пути к файлам
process_json_file('endfile.json', 'merged_file.json')
