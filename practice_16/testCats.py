from cat import Cat

cat_male = Cat('сэм', "мальчик", 1)
print("Имя питомца: ", cat_male.name)
print("Пол питомца: ", cat_male.sex)

if cat_male.age % 10 == 1:
    print("Возраст питомца: ", cat_male.age, 'год')
elif cat_male.age % 10 in [2, 3, 4]:
    print("Возраст питомца: ", cat_male.age, 'годa')
else:
    print("Возраст питомца: ", cat_male.age, 'лет')

