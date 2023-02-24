Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

---

Код проверяет, можно ли построить треугольник с заданными сторонами a, b и c. Функция is_triangle возвращает True, если это возможно, и False, если нет.

Для того, чтобы треугольник мог быть построен, необходимо выполнение условия: сумма любых двух сторон должна быть больше третьей стороны. Функция сравнивает сумму a + b со значением c, a + c со значением b и b + c со значением a. Если это условие выполняется для всех сторон, функция возвращает True, иначе False.
