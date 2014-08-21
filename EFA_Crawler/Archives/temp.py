import pickle

lastnamelist = pickle.load(open(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\18800_lastname.pkl', 'rb'))

temp = list()

for name in lastnamelist:
    name = name[0] + name[1:].lower()
    temp.append(name)

pickle.dump(temp, open(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\18800_lastname1.p', 'wb'))
with open('18800_lastname.txt', 'wb') as f:
    f.write('\n'.join(temp))