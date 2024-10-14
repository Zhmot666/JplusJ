import json

if __name__ == '__main__':
    new_dict = dict()

    with open('Kv3.json', encoding='cp1251') as kv4:
        all_data2 = json.load(kv4)
        all_employees2 = all_data2['data']
        for key, value in all_data2.items():
            if key != 'data':
                new_dict[key] = value

    with open('Kv2.json', encoding='cp1251') as kv3:
        all_data1 = json.load(kv3)
        all_employees1 = all_data1['data']

    for fl in all_data2.items():
        if key != 'data':
            new_dict[key] = value
    new_dict['data'] = list()

    for i in all_employees2:
        for j in all_employees1:
            if i['ils'] == j['ils'] and i['kzl'] != '03':
                temp_dict = dict()
                for key, value in i.items():
                    if key != 'r31' or key != 'r32':
                        temp_dict[key] = value
                    if key == 'r31' or key == 'r32':
                        temp_dict[key] = j[key]+i[key]
                new_dict['data'].append(temp_dict)
                break
        else:
            new_dict['data'].append(i)

    with open("out.txt", "w", encoding='cp1251') as outfile:
        json.dump(new_dict, outfile)
