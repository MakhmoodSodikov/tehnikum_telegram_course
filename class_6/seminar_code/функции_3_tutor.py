import database
our_data = database.data

def users_(user_number):
    l = []
    for key in our_data.keys():
        vals = our_data[key]
        l.append(vals[user_number])
    return l

def compound(n):
    users = []
    for i in range(n):
        users.append(users_(i))
    print(users)

compound(2)