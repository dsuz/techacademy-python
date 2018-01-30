class Human:
    def __init__(self, age, name, gender):
        self._age = age
        self._name = name
        self._gender = gender
    # age, name, gender
    def _get_age(self):
        return self._age
    def _set_age(self, value):
        self._age = value

    age = property(_get_age, _set_age)
    
    def _get_name(self):
        return self._name
    def _set_name(self, value):
        self._name = value

    name = property(_get_name, _set_name)
        
    def _get_gender(self):
        return self._gender
    def _set_gender(self, value):
        self._gender = value
                
    gender = property(_get_gender, _set_gender)
    
l = [Human(25, "snpi", "male"), Human(30, "foo", "female"), Human(23, "bar", "male")]

result = sorted(l, key=lambda h: h.age, reverse=True)

# 以下不要
for h in result:
    print("{}, {}, {}".format(h.age, h.name, h.gender))
