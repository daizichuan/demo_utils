import json


def check_key_dict_list_value(json_data, key):
    '''根据key，从多层dict查看value'''
    if isinstance(json_data, list):
        for i in json_data:
            if key in str(i): return check_key_dict_list_value(i, key=key)
    elif isinstance(json_data, dict):
        for k, v in json_data.items():
            if k == key:
                return v
            if key in str(v):
                return check_key_dict_list_value(v, key=key)
    else:
        try:
            return check_key_dict_list_value(json.loads(json_data), key=key)
        except:
            return


if __name__ == '__main__':
    lis = []
    json_data1 = {'key1': {'key2': [{'key3': 93, 'key4': 14}, {'key3': 93, 'key4': 15}]}, 'key5': 'test'}
    print(type(check_key_dict_list_value(json_data1, 'key6')))
    # print(lis)
