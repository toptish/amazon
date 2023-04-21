import json

def parse_item(item):
    pass


def read_txt(path: str) -> str:
    with open(path, 'r') as file:
        data = file.read()
    return data

def transform_similar(similar_field):
    similar_list = similar_field.split('  similar:')[1].split('  ')[1:]
    similar_transformed = '"similar":[' + ",".join(similar_list) + "]"
    return similar_transformed


def transform_field(field):
    pair = field.split(':')
    dict_format = f'"{pair[0].strip()}": "{pair[1].strip()}"'
    return dict_format

def item_to_dict(item: str) -> dict:
    # print(item)
    categories = item.split('categories: ')[1].split('  reviews:')[0].split('\n')[1:]
    reviews = item.split('  reviews:')[1].split('similar: ')[0].split('\n')[1:]

    item_list = item.split('\n')
    item_list_transformed = []
    for field in item_list:
        if '  similar:' in field:
            # print(field)
            field_transf = transform_similar(field)
        elif '  categories:' in field:
            field_transf = f'"categories": {categories}'
        elif ' reviews:' in field:
            field_transf = f'"reviews": {reviews}'
        elif '|' in field:
            continue
        elif 'cutomer' in field:
            continue
        else:
            field_transf = transform_field(field)
        item_list_transformed.append(field_transf)
    # item_list = [x.strip() for x in item_list]
    item_json_formatted = '{\n' + ',\n'.join(item_list_transformed) + '\n}'
    # item_json_formatted = '{\n' + item.replace('\n', ',\n') + '\n}'
    # item_json = json.loads(item_json_formatted)
    # print(ifor cycle next looptem_json)
    return ',\n'.join(item_list_transformed)
    # return item_json

    # return item_dict


if __name__ == '__main__':
    data = read_txt('data/temp.txt')
    # print(data)
    data = item_to_dict(data)

    print(data)