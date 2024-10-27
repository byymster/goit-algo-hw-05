import timeit


# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    skip = {c: m for c in text} | skip

    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += skip.get(text[i], m)

    return -1


# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    lps = [0] * m
    j = 0

    # Попереднє обчислення таблиці lps
    compute_lps_array(pattern, m, lps)

    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern, prime=101):
    m, n = len(pattern), len(text)
    hpattern = 0
    htext = 0
    h = 1

    for i in range(m - 1):
        h = (h * 256) % prime

    for i in range(m):
        hpattern = (256 * hpattern + ord(pattern[i])) % prime
        htext = (256 * htext + ord(text[i])) % prime

    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            htext = (256 * (htext - ord(text[i]) * h) + ord(text[i + m])) % prime
            if htext < 0:
                htext += prime

    return -1


# Читання файлів
def read_file(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as file:
        return file.read()


# Функція для вимірювання часу
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=1)



# Основний блок для порівняння
if __name__ == "__main__":
    text1 = read_file('article1.txt', encoding='windows-1251')
    text2 = read_file('article2.txt', encoding='utf-8')

    pattern_exist = "кількість"
    pattern_non_exist = "non_existing_substring_here"

    algorithms = {
        "Boyer-Moore": boyer_moore,
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp
    }

    for text, text_name in [(text1, "Стаття 1"), (text2, "Стаття 2")]:
        print(f"\nТест для {text_name}:")
        for pattern, pattern_name in [(pattern_exist, "існуючий підрядок"), (pattern_non_exist, "вигаданий підрядок")]:
            print(f"\nПошук для {pattern_name}:")
            for alg_name, alg_func in algorithms.items():
                time_taken = measure_time(alg_func, text, pattern)
                print(f"{alg_name}: {time_taken:.6f} сек")
