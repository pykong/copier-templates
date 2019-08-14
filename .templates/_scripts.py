# This is a temporary workaround till Poetry supports scripts, see
# https://github.com/sdispater/poetry/issues/241.
# https://medium.com/octopus-wealth/python-scripts-26e3d0bd5277
from subprocess import check_call


def format() -> None:
    check_call(["seed-isort-config"])
    check_call(["isort", "-y", "."])
    check_call(["black", "."])
    # check_call(["blacken-docs", "."])
    [% block format %][% endblock %]


def lint() -> None:
    check_call(["mypy", "."])
    check_call(["flake8", "."])
    [% block lint %][% endblock %]


def test() -> None:
    check_call(["pytest", "."])
    [% block test %][% endblock %]

