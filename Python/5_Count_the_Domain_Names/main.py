# 5 Kyu - Count the Domain Names

def count_domains(domains, min_hits=0):
    # Шаг 1: Создается словарь для хранения количества запросов для каждого домена.
    domain_count = {}
    for line in domains.split('\n'):
        domain, count = line.split()
        count = int(count)
        parts = domain.split('.')
        # Шаг 2: Удаляются поддомены, оставляя только основные домены. Для доменов вида .co.xx и .com.xx оставляется 3 уровня, остальные домены имеют 2 уровня.
        if len(parts) > 2 and (parts[-2] == 'co' or parts[-2] == 'com'):
            domain = '.'.join(parts[-3:])
        else:
            domain = '.'.join(parts[-2:])
        # Шаг 3: Количество запросов добавляется в словарь.
        domain_count[domain] = domain_count.get(domain, 0) + count
    # Шаг 4: Из словаря удаляются домены с количеством запросов ниже порога min_hits.
    domain_count = {k: v for k, v in domain_count.items() if v >= min_hits}
    # Шаг 5: Словарь сортируется по количеству запросов в убывающем порядке, а затем по алфавиту.
    sorted_domains = sorted(domain_count.items(), key=lambda x: (-x[1], x[0]))
    # Шаг 6: Форматируется строка вывода.
    output = ''
    for domain, count in sorted_domains:
        output += f'{domain} ({count})\n'
    return output.strip()