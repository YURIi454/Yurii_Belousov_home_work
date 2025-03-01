import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


def test_decorators() -> None:
    """Тестирование декоратора."""

    @log(filename="log_test")
    def one(r: int, e: int) -> float:
        return r / e

    assert one(44, 22) == 2

    with pytest.raises(ZeroDivisionError):
        one(15, 0)


def test_caps_decorators(capsys: CaptureFixture[str]) -> None:
    """Тестирования декоратора."""

    @log()
    def two(a: int, s: int) -> float:
        return a / s

    two(9, 3)
    check_out = capsys.readouterr()
    assert check_out.out == "работа функции two >>> 3.0\n\n"

    with pytest.raises(ZeroDivisionError):
        two(8, 0)
