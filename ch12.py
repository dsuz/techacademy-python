
class Human:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age
        self.gender = gender
    def __repr__(self):
        return repr((self.name, self.age, self.gender))

people = [
    Human('BAKARHYTHM', 42, 'male'),
    Human('Hironari Yamazaki', 41, 'male'),
    Human('Arthur Kuroda', 56, 'male'),
    Human('Yuko Fueki', 38, 'female'),
    Human('Diamond Yukai', 55, 'male'),
]

people.sort(key=lambda person:person.age, reverse=True) # 年齢の高い順にソートする
print(people)
