import requests
from timeit import default_timer as timer

def download_file(url):
    try:
        response = requests.get(url, timeout=10) # Додаємо таймаут
        response.raise_for_status() # Краще використання для перевірки успішного відповіді
        return response.text
    except requests.RequestException as e:
        print(f"Помилка при завантаженні файлу: {e}")
        return None

def measure_algorithm_time(algorithm, text, pattern):
    start_time = timer()
    result = algorithm(text, pattern)
    end_time = timer()
    return (end_time - start_time, result)

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
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
    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == M:
            return i - j
    return -1

def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1, modulus)
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1, modulus)
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            current_slice_hash = current_slice_hash % modulus
    return -1

# Завантаження текстових файлів з Інтернету
url_article1 = f"https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ&export=download"
url_article2 = f"https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh&export=download"

article1_text = download_file(url_article1)
article2_text = download_file(url_article2)

# Патерни для пошуку
real_pattern = "пошук"
fake_pattern = "абракадабра"

# Вимірюємо час виконання для реального підрядка в обох текстах
kmp_time_article1_real = measure_algorithm_time(kmp_search, article1_text, real_pattern)
boyer_moore_time_article1_real = measure_algorithm_time(boyer_moore_search, article1_text, real_pattern)
rabin_karp_time_article1_real = measure_algorithm_time(rabin_karp_search, article1_text, real_pattern)

kmp_time_article2_real = measure_algorithm_time(kmp_search, article2_text, real_pattern)
boyer_moore_time_article2_real = measure_algorithm_time(boyer_moore_search, article2_text, real_pattern)
rabin_karp_time_article2_real = measure_algorithm_time(rabin_karp_search, article2_text, real_pattern)

# Вимірюємо час виконання для вигаданого підрядка в обох текстах
kmp_time_article1_fake = measure_algorithm_time(kmp_search, article1_text, fake_pattern)
boyer_moore_time_article1_fake = measure_algorithm_time(boyer_moore_search, article1_text, fake_pattern)
rabin_karp_time_article1_fake = measure_algorithm_time(rabin_karp_search, article1_text, fake_pattern)

kmp_time_article2_fake = measure_algorithm_time(kmp_search, article2_text, fake_pattern)
boyer_moore_time_article2_fake = measure_algorithm_time(boyer_moore_search, article2_text, fake_pattern)
rabin_karp_time_article2_fake = measure_algorithm_time(rabin_karp_search, article2_text, fake_pattern)

# Виводимо результати
print("Час виконання для реального підрядка в статті 1:")
print("KMP:", kmp_time_article1_real)
print("Boyer-Moore:", boyer_moore_time_article1_real)
print("Rabin-Karp:", rabin_karp_time_article1_real)
print()

print("Час виконання для реального підрядка в статті 2:")
print("KMP:", kmp_time_article2_real)
print("Boyer-Moore:", boyer_moore_time_article2_real)
print("Rabin-Karp:", rabin_karp_time_article2_real)
print()

print("Час виконання для вигаданого підрядка в статті 1:")
print("KMP:", kmp_time_article1_fake)
print("Boyer-Moore:", boyer_moore_time_article1_fake)
print("Rabin-Karp:", rabin_karp_time_article1_fake)
print()

print("Час виконання для вигаданого підрядка в статті 2:")
print("KMP:", kmp_time_article2_fake)
print("Boyer-Moore:", boyer_moore_time_article2_fake)
print("Rabin-Karp:", rabin_karp_time_article2_fake)
