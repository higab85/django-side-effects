from side_effects.decorators import has_side_effects, is_side_effect_of
from side_effects.registry import _registry  # noqa: F401


@has_side_effects("foo")
def origin(message: str) -> str:
    print(f"origin: {message}")  # noqa: T001
    return f"Message received: {message}"


@is_side_effect_of("foo")
def no_docstring(message: str) -> None:
    print(f"side-effect.1: message={message}")  # noqa: T001


@is_side_effect_of("foo")
def one_line_docstring(message: str) -> None:
    """This is a one-line docstring."""
    print(f"side-effect.2: message={message}")  # noqa: T001


@is_side_effect_of("foo")
def multi_line_docstring(message: str, return_value: str) -> None:
    """
    This is a multi-line docstring.

    It has more information here.

    """
    print(  # noqa: T001
        f"Side-effect.3: message={message}, return_value={return_value}"
    )
