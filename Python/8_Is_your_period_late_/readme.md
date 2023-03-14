## 8 kyu - Is your period late?
[Ссылка на задачу](https://www.codewars.com/kata/578a8a01e9fd1549e50001f1 "Is your period late?")

In this kata, we will make a function to test whether a period is late.

Our function will take three parameters:

last - The Date object with the date of the last period

today - The Date object with the date of the check

cycleLength - Integer representing the length of the cycle in days


Return true if the number of days passed from last to today is greater than cycleLength. Otherwise, return false.

---
## Задание:

## 8 Kyu - ваш период поздно?
[SSSLKA na зadaчue] (https://www.codewars.com/kata/578a8a01e9fd1549e50001f1 "Ваш период поздно?")

В этой Kata мы сделаем функцию, чтобы проверить, опаздывает ли период.

Наша функция займет три параметра:

Последнее - объект даты с датой последнего периода

Сегодня - объект даты с датой чека

Cyclelength - целое число, представляющее длину цикла в дни


Вернуть True, если количество дней, прошедших с прошлого, до сегодняшнего дня, больше, чем Cyclelength.В противном случае вернуть ложь.

---

Мы определяем функцию period_is_late, которая принимает три аргумента: last - объект datetime.date с датой последней менструации, today - объект datetime.date с датой проверки, и cycle_length - целое число, представляющее длину цикла в днях.

Затем мы определяем константу one_day, которая представляет количество секунд в дне. Далее мы вычисляем количество дней между датами last и today, используя метод days объекта datetime.timedelta, полученного из разности дат. Наконец, мы возвращаем True, если количество дней, прошедших между датами, больше cycle_length, и False в противном случае.

Обратите внимание, что данный код также предполагает, что дата last предшествует дате today. Если это не так, функция может вернуть непредвиденный результат.