## 5 Kyu - Rot13
---
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

---

Функция принимает строковое сообщение в качестве входных данных, выполняет итерацию по каждому символу в строке и применяет шифр ROT13 к каждому буквенному символу. Новая позиция каждой буквы в алфавите вычисляется путем добавления 13 к ее значению в ASCII-коде, при необходимости заменяя его на "a" или "А". Небуквенные символы добавляются к результирующей строке без изменений. Возвращается строка конечного результата.

Эта реализация обрабатывает как заглавные, так и строчные буквы и сохраняет любые специальные символы или цифры в исходной строке.