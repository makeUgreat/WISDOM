import pickle
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'Korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

with open('james.p', 'wb') as file:
    pickle.dump(name,file)
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(scores,file)


with open('james.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
