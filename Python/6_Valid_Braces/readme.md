# Valid Braces

---

Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples

```
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
```

# Вот решение задачи на Python, которое проверяет, является ли порядок скобок в строке правильным:

---

Алгоритм решения следующий:

- Создаем словарь braces_dict, который будет содержать соответствия открывающихся и закрывающихся скобок.
  Создаем пустой список stack, который будет содержать открывающиеся скобки.
- Проходимся по каждому символу в строке. Если символ является открывающейся скобкой, добавляем его в стек. Если символ является закрывающейся скобкой, проверяем, соответствует ли он последней открывающейся скобке в стеке. Если да, то удаляем последнюю открывающуюся скобку из стека. Если нет, то порядок скобок неправильный, возвращаем False.
- Если стек не пустой после прохода по всей строке, то порядок скобок также неправильный, возвращаем False.
- Все скобки в строке соответствуют друг другу, возвращаем True.

Примеры использования функции:

```
>>> validBraces("(){}[]")
True
>>> validBraces("([{}])")
True
>>> validBraces("(}")
False
>>> validBraces("[(])")
False
>>> validBraces("[({})](]")
False
```

# Варианты:

```
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''
```

```
def validBraces(s, previous = ''):
  while s != previous: previous, s = s, s.replace('[]','').replace('{}','').replace('()','')
  return not s
```

```
def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0
```
