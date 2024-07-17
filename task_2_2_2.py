# Напишите скрипт который создаст параллельно 10 файлов с именем `file_ {index} .txt' и записывает их номер внутрь
# файла.

import threading


def create_file_index(i):
    with open(f'file_{i}', 'w') as f:
        f.write(str(i))


#запуск в несколько потоков
def my_treads(n):
    threads = []
    for i in range(1, n + 1):
        thread = threading.Thread(target=create_file_index, args=(i,))
        thread.start()
        threads.append(thread)
    #ожидаем завершение всех потоков
    for thread_item in threads:
        thread_item.join()


if __name__ == '__main__':
    my_treads(10)
