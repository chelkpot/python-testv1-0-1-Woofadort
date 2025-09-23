# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    nums: map = map(int, input("Введите числа: ").split())
    squares: list = [str(x * x) for x in nums]

    print("Результат:", " ".join(squares))
    # Аннотация типов - не признак ИИ

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()