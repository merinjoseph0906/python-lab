def merge(dict1, dict2):
    return (dict2.update(dict1))
dict1 = {1:'apple', 2: 'orange'}
dict2 = {3:'bread', 4:'jam'}
print(merge(dict1, dict2))
print(dict2)