import multiprocessing


def divisor_part(n, start, end):
    """Получаем список целочисленных делителей числа n в диапазоне от start до end"""
    result = []
    for i in range(start, end):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return result


def divisor(n, num_processes=4):
    """Получаем отсортированный список целочисленных делителей числа n с использованием многопроцессорности"""
    r = int(n ** 0.5) + 1
    chunk_size = r // num_processes
    pool = multiprocessing.Pool(processes=num_processes)

    tasks = []
    for i in range(1, r, chunk_size):
        start = i
        end = min(i + chunk_size, r)
        tasks.append((n, start, end))

    results = pool.starmap(divisor_part, tasks)

    # Объединяем и сортируем результаты
    flat_results = [item for sublist in results for item in sublist]
    return sorted(set(flat_results))


if __name__ == '__main__':
    print(divisor(20_000_000))