# Напишите скрипт который создаст параллельно 10 файлов с именем `file_ {index} .txt' и записывает их номер внутрь
# файла.

def create_file(n):
    """Создание n файлов и запись вних индекс"""
    for i in range(1, n+1):
        with open(f'file_{i}', 'w') as f:
            f.write(str(i))


if __name__ == '__main__':
    create_file(10)
