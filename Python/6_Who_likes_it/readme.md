## Who likes it?

---

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

```
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
```

Note: For 4 or more names, the number in "and 2 others" simply increases.

### Функция на языке Python, которая принимает массив имен людей, которым нравится определенный объект, и возвращает соответствующую строку

---

Функция начинается с проверки длины массива names. Если массив пустой, функция возвращает "no one likes this". Если в массиве только один элемент, функция возвращает имя этого человека с "likes this". Если в массиве два элемента, функция возвращает два имени, разделенные "and", с "like this". Если в массиве три элемента, функция возвращает три имени, разделенные запятой и "and", с "like this". И наконец, если в массиве четыре или более элементов, функция возвращает первые два имени, разделенные запятой и "and", за которыми следует количество оставшихся элементов с "others like this".

_Вот пример использования:_

```
print(likes([]))  # Вывод: "no one likes this"
print(likes(["Peter"]))  # Вывод: "Peter likes this"
print(likes(["Jacob", "Alex"]))  # Вывод: "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"]))  # Вывод: "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"]))  # Вывод: "Alex, Jacob and 2 others like this"
```

В первом примере массив пустой, поэтому возвращается "no one likes this". Во втором примере в массиве только одно имя, поэтому возвращается имя этого человека с "likes this". В третьем примере в массиве два имени, поэтому возвращается два имени, разделенные "and", с "like this". В четвертом примере в массиве три имени, поэтому возвращаются три имени, разделенные запятой и "and", с "like this". В пятом примере в массиве четыре имена, поэтому возвращаются первые два имени, разделенные запятой и "and", за которыми следует количество оставшихся элементов (2) с "others like this".
