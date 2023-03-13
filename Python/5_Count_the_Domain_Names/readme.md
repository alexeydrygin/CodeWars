## 5 Kyu - Count the Domain Names
---
Story
You have a list of domain names from a log file, indicating the number of times the computer accessed those sites. However, the list shows subdomains too, but you want to see only the main sites and the total number of accesses. For example 6.clients-channel.google.com and apis.google.com should be counted together as google.com.

Task
Complete the function that takes two arguments:

- domains is a list of domain names, showing the number of access requests to each domain, as you copied it from the logs
- and the optional min_hits which defines what is the minimum number of accesses in order to appear on the output list. If this is not given, consider it 0.
Return a string ready to be printed, showing the sites with the total number of accesses, in a decreasing order.

Output requirements:

- the output should show the sites with the total number of accesses in parentheses,
- sites should have only 2 levels (e.g. ebay.com), except for .co.xx and .com.xx type domains, which should have 3 levels (e.g. amazon.co.jp),
- the list should be sorted in decreasing order of access,
- if two sites have the same number of accesses, sort them alphabetically,
- entries should be separated by newlines (\n)
Example
```
domains_list = '''\
*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212
*.in-addr.arpa    384
*.l.google.com    317
1.client-channel.google.com    110
6.client-channel.google.com    45
a.root-servers.net    1059
apis.google.com    43
clients4.google.com    71
clients6.google.com    81
connect.facebook.net    68
edge-mqtt.facebook.com    56
graph.facebook.com    150
mail.google.com    128
mqtt-mini.facebook.com    47
ssl.google-analytics.com    398
star-mini.c10r.facebook.com    46
staticxx.facebook.com    48
www.facebook.com    178
www.google.com    162
www.google-analytics.com    127
www.googleapis.com    87'''

count_domains(domains_list, 500) = '''\
root-servers.net (1059)
google.com (957)
facebook.com (525)
google-analytics.com (525)'''
```

---
Функция count_domains принимает список доменных имен, указывающих количество запросов к каждому домену, и необязательный параметр min_hits, который определяет минимальное количество запросов, необходимое для появления в выходном списке.

Шаг 1: Создается словарь для хранения количества запросов для каждого домена.

Шаг 2: Удаляются поддомены, оставляя только основные домены. Для доменов вида .co.xx и .com.xx оставляется 3 уровня, остальные домены имеют 2 уровня.

Шаг 3: Количество запросов добавляется в словарь.

Шаг 4: Из словаря удаляются домены с количеством запросов ниже порога min_hits.

Шаг 5: Словарь сортируется по количеству запросов в убывающем порядке, а затем по алфавиту.

Шаг 6: Форматируется строка вывода.

В результате функция возвращает строку, готовую к печати, показывающую домены с общим количеством доступов в убывающем порядке, в соответствии с требованиями вывода.

---

## Комментарии к коду:


```python
def count_domains(domains, min_hits=0):
```
Это определение функции с двумя аргументами:

domains - строка с доменными именами и количеством доступов к ним
min_hits - минимальное количество доступов, необходимое для включения домена в список вывода. Значение по умолчанию 0.
```python
domain_count = {}
```
Создание пустого словаря для хранения количества доступов к каждому доменному имени.

```python
for line in domains.split('\n'):
    domain, count = line.split()
    count = int(count)
    parts = domain.split('.')
```
Разбиение строки на строки по разделителю новой строки и перебор строк в цикле. Каждая строка содержит доменное имя и количество доступов, разделенные пробелом. Затем строка разбивается на две переменные: domain - доменное имя, и count - количество доступов. Значение count преобразуется в целочисленное значение.

```python
    if len(parts) > 2 and (parts[-2] == 'co' or parts[-2] == 'com'):
        domain = '.'.join(parts[-3:])
    else:
        domain = '.'.join(parts[-2:])
```
Удаляются субдомены, чтобы получить основное доменное имя. Если доменное имя имеет более двух частей и предпоследняя часть является "co" или "com", то оставшиеся две части (т. е. основное доменное имя и последняя часть) объединяются с помощью точки. В противном случае оставляется только основное доменное имя.

```python
    domain_count[domain] = domain_count.get(domain, 0) + count
```
Для каждого доменного имени добавляется количество доступов в словарь domain_count. Если доменное имя уже присутствует в словаре, то количество доступов добавляется к текущему значению в словаре. Если доменное имя отсутствует в словаре, то добавляется новый элемент со значением, равным количеству доступов.

```python
domain_count = {k: v for k, v in domain_count.items() if v >= min_hits}
```
Удаляются домены, количество доступов к которым меньше, чем min_hits.

```python
sorted_domains = sorted(domain_count.items(), key=lambda x: (-x[1], x[0]))
```
Сортировка элементов словаря domain_count по убыванию количества доступов и по возрастанию лексикографического порядка доменных имен.

```python
output = ''
for domain, count in sorted_domains:
    output += f'{domain} ({count})\n'
```
Форматирование вывода списка отсортированных доменных имен и количества доступов.