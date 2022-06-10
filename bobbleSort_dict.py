elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

# print(elements[0].keys())
# print(elements[0]["transaction_amount"])

def sort_dict(elements,key):
    print(elements)
    size = len(elements)-1
    for i in range(size):
        for j in range(len(elements)-1):
            if elements[j][key] > elements[j+1][key]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp

    print(elements)


if __name__ == '__main__':
    sort_dict(elements,"name")