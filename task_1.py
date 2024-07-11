# Дано число в диапазоне от 1_000_000 до 20_000_000. Получите список целочисленных делителей этого числа.
def divisor(n):
    """ Получаем отсортированый список целочисленных делителей числа n """

    result = []
    r = int(n ** 0.5)
    for i in range(1, r + 1):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return sorted(set(result))


if __name__ == '__main__':
    print(divisor(20_000_000))
