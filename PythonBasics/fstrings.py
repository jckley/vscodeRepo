# %%
# lesson https://www.youtube.com/watch?v=nghuHvKLhJA
# single or double quotes can be used, but it is preferred to use "" if u use '' in variables
from datetime import datetime

name = "Juan"
data = [2, 4, 6, 8]
print(f"Mi Nombre es {name}")

# %%
# also f strings support applying methods to variables
sentence = f"My name is {name.upper()}"
print(sentence)

# %%
dict1 = {"name": "Jenn", "age": 23}
sentence1 = f"My name is {dict1['name']} and I am {dict1['age']} years old"
print(sentence1)

# %%
# calculation
for n in range(1, 5):
    # el : despues de la variable indica un formato adicional
    sentence2 = f"The value is {n*2:05}"
    print(sentence2)
    print(f"The value is == {n*2:05}")
# %%
#  f string formatting 1

# '2016-07-26 03:57'
date1 = "{:%Y-%m-%d %H:%M}".format(datetime(2016, 7, 26, 3, 57))
print(date1)

birthday = datetime(1990, 1, 3)
sentence3 = f"Jenn has a birthday on {birthday:%B %d, %Y}"
print(sentence3)

# %%
#  f string formatting 2
str1 = "{:*<15}".format("Algun texto")  # Algun texto****
print(str1)
str2 = "{:.10}".format("Python Tutorial")  # cortar en diez ch
print(str2)
# %%
#  f string formatting 2
