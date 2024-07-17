from multiprocessing import Process


def create_file_index(i):
    with open(f'file_{i}', 'w') as f:
        f.write(str(i))


#запуск в несколько потоков
def my_processes(n):
    processes = []
    for i in range(1, n + 1):
        process = Process(target=create_file_index, args=(i,))
        processes.append(process)
    #ожидаем завершение всех потоков
    for process_item in processes:
        process_item.start()

if __name__ == '__main__':
    my_processes(10)