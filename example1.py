
def print_text(f: callable):
    counter = [1]
    def wrapper(*args, **kwargs):
        c = counter
        print(f"{c[0]} запуск")
        result = f(*args, **kwargs)
        c[0] += 1
        return result
    return wrapper

@print_text
def func(a: int) -> int:
    return a ** 2
@print_text
def func2() -> None:
    print("run")

# Задание
# 1 запуск
func(1)
# 2 запуск
func(1)

func2()
func2()
func2()