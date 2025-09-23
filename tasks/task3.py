# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    weight: str = input("Введите вес в кг: ").strip().replace(',', '.')
    height: str = input("Введите рост в метрах: ").strip().replace(',', '.')

    weight = float(weight)
    height = float(height)

    BMI = weight / (height**2)

    print(f"Индекс массы тела: {BMI}")
    # Аннотация типов - не признак ИИ
   

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()