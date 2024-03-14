class HashTable:
    # Ініціалізація хеш-таблиці з певним розміром
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Створення порожніх списків для кожної комірки

    # Функція хешування, що повертає хеш для ключа
    def hash_function(self, key):
        return hash(key) % self.size

    # Вставка пари ключ-значення в хеш-таблицю
    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        # Якщо комірка порожня, просто додаємо пару
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            # Якщо ключ вже існує, оновлюємо його значення
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # Якщо ключ новий, додаємо пару в список
            self.table[key_hash].append(key_value)
            return True

    # Отримання значення за ключем
    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]  # Повертаємо значення, якщо ключ знайдено
        return None  # Якщо ключ не знайдено, повертаємо None

    # Видалення пари ключ-значення за ключем
    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i in range(len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    self.table[key_hash].pop(i)  # Видаляємо пару, якщо ключ знайдено
                    return True
        return False  # Якщо ключ не знайдено, повертаємо False

# Тестуємо хеш-таблицю та новий метод delete:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))   # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30

H.delete("orange")      # Видаляємо "orange"
print(H.get("orange"))  # Тепер виведе: None, оскільки "orange" було видалено
