# Напишите скрипт который создаст параллельно 10 файлов с именем `file_ {index} .txt' и записывает их номер внутрь
# файла.

import threading


def create_file_thread():
    """Создание n файлов и запись вних индекс с помощью потоков"""

    def create_file_index(i):
        with open(f'file_{i}', 'w') as f:
            f.write(str(i))

    thread1 = threading.Thread(target=create_file_index, args=(1,))
    thread2 = threading.Thread(target=create_file_index, args=(2,))
    thread3 = threading.Thread(target=create_file_index, args=(3,))
    thread4 = threading.Thread(target=create_file_index, args=(4,))
    thread5 = threading.Thread(target=create_file_index, args=(5,))
    thread6 = threading.Thread(target=create_file_index, args=(6,))
    thread7 = threading.Thread(target=create_file_index, args=(7,))
    thread8 = threading.Thread(target=create_file_index, args=(8,))
    thread9 = threading.Thread(target=create_file_index, args=(9,))
    thread10 = threading.Thread(target=create_file_index, args=(10,))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()


if __name__ == '__main__':
    create_file_thread()
