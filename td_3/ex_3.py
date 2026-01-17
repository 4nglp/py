sales = {
    "yahya":0,
    "oussama":41,
    "abdessamad":20,
}

def total_sales(dic):
    return sum(dic.values())
print(total_sales(sales))

def top_seller(dic):
    return max(dic, key = dic.get)
print(top_seller(sales))

