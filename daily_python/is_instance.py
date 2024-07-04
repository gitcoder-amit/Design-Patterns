'''To flatten a JSON object to a depth of 2, you can use a script in Python. This involves iterating through the nested JSON structure and restructuring it so that all keys at levels deeper than 2 are brought up to the second level, concatenating the nested keys.

'''

print(isinstance({4:5}, dict))  # True
print(isinstance([1,2], list))  # True
print(isinstance('str', str))  #True
print(isinstance(9, int))   # True
print(isinstance({4:5}, list))  # False


import json

def flatten_json(y, depth=2, prefix=''):
    out = {}

    def flatten(x, name='', current_depth=1):
        if isinstance(x, dict):
            # if current_depth < depth:
            for a in x:
                flatten(x[a], f'{name}{a}_', current_depth + 1)
            # else:
                # out[name[:-1]] = x
        # elif isinstance(x, list):
        #     if current_depth < depth:
        #         for i, a in enumerate(x):
        #             flatten(a, f'{name}{i}_', current_depth + 1)
        #     else:
        #         out[name[:-1]] = x
        else:
            out[name[:-1]] = x

    flatten(y, prefix)
    return out

# Example usage:
json_data = {
    "name": "John",
    "address": {
        "city": "New York",
        "zip": {
            "code": "10001",
            "extra": "1234"
        }
    },
    "contact": {
        "phone": "123456789",
        "email": "john@example.com"
    }
}

flattened_json = flatten_json(json_data, depth=4)
print(json.dumps(flattened_json, indent=4))

# output

# {
#     "name": "John",
#     "address_city": "New York",
#     "address_zip_code": "10001",
#     "address_zip_extra": "1234",
#     "contact_phone": "123456789",
#     "contact_email": "john@example.com"
# }

def flatten(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

nested_list = [1, [2, [3, [4, 5]], 6], 7, [8, [9, 10]]]
flattened_list = flatten(nested_list)
print(flattened_list)
