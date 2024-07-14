# Напишите скрипт который создаст параллельно 10 файлов с именем `file_ {index} .txt' и записывает их номер внутрь
# файла.

from multiprocessing import Process


def create_file_process():
    """Создание n файлов и запись вних индекс с помощью процессов"""

    def create_file_index(i):
        with open(f'file_{i}', 'w') as f:
            f.write(str(i))

    process1 = Process(target=create_file_index, args=(1,))
    process2 = Process(target=create_file_index, args=(2,))
    process3 = Process(target=create_file_index, args=(3,))
    process4 = Process(target=create_file_index, args=(4,))
    process5 = Process(target=create_file_index, args=(5,))
    process6 = Process(target=create_file_index, args=(6,))
    process7 = Process(target=create_file_index, args=(7,))
    process8 = Process(target=create_file_index, args=(8,))
    process9 = Process(target=create_file_index, args=(9,))
    process10 = Process(target=create_file_index, args=(10,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
    process9.start()
    process10.start()


if __name__ == '__main__':
    create_file_process()
