import random


def distance_levin_wiki(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)  # Keep current and previous row, not entire matrix
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

def distance_levin_rec(a, b):
    def recursive(i, j):
        if i == 0 or j == 0:
            # если одна из строк пустая, то расстояние до другой строки - ее длина
            # т.е. n вставок
            return max(i, j)
        elif a[i - 1] == b[j - 1]:
            # если оба последних символов одинаковые, то съедаем их оба, не меняя расстояние
            return recursive(i - 1, j - 1)
        else:
            # иначе выбираем минимальный вариант из трех
            return 1 + min(
                recursive(i, j - 1),  # удаление
                recursive(i - 1, j),   # вставка
                recursive(i - 1, j - 1)  # замена
            )
    return recursive(len(a), len(b))

def generate_string(len_s):
    s = ''

    for i in range(0, int(len_s)):
        s += str(
            chr(
                random.randint(
                    ord('A'),
                    ord('z')
                )
            )
        )
    
    return s
