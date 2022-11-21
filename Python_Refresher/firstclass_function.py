from operator import itemgetter

def divide(dividend,divisor):
    if divisor==0:
        raise ZeroDivisionError("The divisor cannot be zero")
    return dividend/divisor

def calculate(*values,operator):
    return operator(*values)

result=calculate(20,4,operator=divide)
print(result)


def search(sequence,expected,finder):
    for elem in sequence:
        if finder(elem)==expected:
            return elem
    raise RuntimeError(f"could not find an element with {expected}")

friends=[
    {"name":"rolf smith",'age':'26'},
    {"name":"adam wolf",'age':'30'},
    {"name":"anne pun",'age':'27'}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends,"anne pun",get_friend_name))
print(search(friends,"anne pun",itemgetter("name")))
