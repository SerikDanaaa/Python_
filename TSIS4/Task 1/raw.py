import re

given_filename = "../raw.txt"
input_file = open(given_filename, mode='r', encoding='utf_8')
myfile = input_file.read()

items_cnt = re.findall(r"\d+\.\n", myfile)
item_names = re.findall(r"(.*\n)\d+\,\d+ x", myfile)
cout_cnt = re.findall(r"\d+\,\d+ ", myfile)
item_price = re.findall(r"(?<=\d x ).*.", myfile)
item_total_price = re.findall(r"(.+\,\d+\n)Стоимость", myfile)

print("1. Name of the company:", *re.findall(r"(?<=Филиал ).*.", myfile), end = '\n')

print("2. BIN number:", *re.findall(r"(?<=БИН ).*.", myfile), end = '\n')

print("  For each item:")
for i in range(len(items_cnt)):
    print("    1. Title ----", item_names[i], end = '')
    print("    2. Cout ----", cout_cnt[i])
    print("    3. Unit price ----", item_price[i])
    print("    4. Total price ----", item_total_price[i])

print("4. Date ----", *re.findall(r"(?<=Время: ).*.", myfile), end = '\n\n')

print("5. Address ----", *re.findall(r"(.+\n)Оператор", myfile), end = '')