#  Объединение двух файлов
import json


def merge_json_data(file1_path, file2_path, output_path):
    """
    Объединяет данные из двух JSON файлов по ключу 'ils'.

    Args:
        file1_path (str): Путь к первому JSON файлу (kv3.json).
        file2_path (str): Путь к второму JSON файлу (kv2.json).
        output_path (str): Путь к выходному JSON файлу.
    """

    with open(file1_path, 'r', encoding='cp1251') as f1, \
            open(file2_path, 'r', encoding='cp1251') as f2:

        data1 = json.load(f1)
        data2 = json.load(f2)

    # Создаем словарь для быстрого доступа к объектам из data2 по 'ils'
    data2_by_ils = {item['ils']: item for item in data2['data']}

    # Объединяем данные
    for item1 in data1['data']:
        ils = item1['ils']
        item2 = data2_by_ils.get(ils)
        if item2:
            item1['r31'].extend(item2.get('r31', []))
            item1['r32'].extend(item2.get('r32', []))

    # Записываем объединенные данные в выходной файл
    with open(output_path, 'w', encoding='cp1251') as outfile:
        json.dump(data1, outfile, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    merge_json_data('kv3.json', 'kv2.json', 'out.json')
