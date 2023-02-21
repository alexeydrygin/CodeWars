## Count the smiley faces!

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

```
Example
countSmileys([':)', ';(', ';}', ':-D']); // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']); // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
```

Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

---

Функция count_smileys принимает на вход массив строк arr, содержащий смайлики, и возвращает количество смайликов в массиве, удовлетворяющих условиям задачи.

Функция проходит по каждому элементу массива arr и проверяет, является ли он смайликом. Для этого проверяется длина строки смайлика: если она равна 2, значит, смайлик без носа, и его глаза и рот проверяются отдельно; если длина равна 3, значит, смайлик с носом, и глаза, нос и рот проверяются отдельно. Если смайлик удовлетворяет условиям, то счетчик увеличивается.

На выходе функция возвращает количество удовлетворяющих смайликов. Если массив пустой, функция вернет 0.
