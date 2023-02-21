## Stop gninnipS My sdroW!

---

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

```
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
```

### Функция на языке Python, которая переворачивает все слова в заданной строке, имеющие пять или более букв

---

Функция начинается со сплита строки на слова с помощью метода split(). Затем она проходит по словам и проверяет, имеет ли каждое слово пять или более букв. Если да, то оно переворачивается с помощью среза [::-1] в Python. Наконец, функция объединяет измененные слова обратно в строку с помощью метода join() и возвращает результат.

Вот пример использования:

```
print(spin_words("Hey fellow warriors"))  # Вывод: "Hey wollef sroirraw"
print(spin_words("This is a test"))  # Вывод: "This is a test"
print(spin_words("This is another test"))  # Вывод: "This is rehtona test"
```

В первом примере слово "fellow" имеет пять или более букв, поэтому оно переворачивается в "wollef". Остальные слова остаются без изменений. Во втором примере все слова имеют менее пяти букв, поэтому возвращается исходная строка. В третьем примере слова "another" и "test" имеют пять или более букв, поэтому они переворачиваются в "rehtona" и "tset".
