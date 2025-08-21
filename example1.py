
def print_text(f: callable):
    def wrapper(*args, **kwargs):
        print("start")
        result = f(*args, **kwargs)
        print("stop")
        return result
    return wrapper

@print_text
def func(a: int) -> int:
    return a ** 2
@print_text
def func2() -> None:
    print("run")

print(func(4))
func2()

# Задание
# 1 запуск
func()
# 2 запуск
func()