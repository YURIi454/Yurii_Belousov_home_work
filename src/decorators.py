from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор логирует работу функции, ее результаты и возникшие ошибки.
    filename задан - логи записываются в указанный файл.
    filename не задан - логи выводятся в консоль.
    В логи записываются:
    Имя функции и результат выполнения при успешной операции.
    Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке."""

    def decorator_log(function: Any) -> Any:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            try:
                function(*args, **kwargs)
                write_to_log = f"работа функции {function.__name__} >>> {function(*args, **kwargs)}\n"
                if not filename:
                    print(write_to_log)
                else:
                    with open(filename, mode="a", encoding="utf-8") as file:
                        file.write("#" * 3 + "\n" + write_to_log)

                return function(*args, **kwargs)

            except Exception as error:
                write_to_log = f"{function.__name__} ошибка {type(error).__name__} аргументы {args} {kwargs}"
                if not filename:
                    print(write_to_log)
                else:
                    with open(filename, mode="a", encoding="utf-8") as file:
                        file.write("#" * 3 + "\n" + write_to_log + "\n")
                raise error

        return wrapper

    return decorator_log
