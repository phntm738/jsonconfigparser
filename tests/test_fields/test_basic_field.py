from jsonconfigparser.fields import BasicField
from jsonconfigparser import exceptions
import pytest


def test_basic_field_name():
    field = BasicField(
        name="test",
    )
    assert field.name == "test"
    field.name = "foo"
    assert field.name == "foo"

    field = BasicField()
    with pytest.raises(exceptions.InvalidNameError):
        field.name = 5


def test_basic_field_value():
    field = BasicField()

    with pytest.raises(exceptions.NoValueError):
        val = field.value()

    field.set_value(5)
    assert field.value() == 5

    field = BasicField(
        default=5
    )
    assert field.value() == 5

    field = BasicField(
        nullable=True
    )
    assert field.value() is None
