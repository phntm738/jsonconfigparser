from jsonconfigparser.fields import BaseField
from jsonconfigparser.exceptions import field_errors
import pytest


def test_basic_field_name():
    field = BaseField(
        name="test",
    )
    assert field.name == "test"
    field.name = "foo"
    assert field.name == "foo"

    field = BaseField()
    with pytest.raises(field_errors.InvalidNameTypeError):
        field.name = 5


def test_basic_field_value():
    field = BaseField()

    with pytest.raises(field_errors.NoNameError):
        val = field.value()

    field.name = "test"

    with pytest.raises(field_errors.NoValueError):
        val = field.value()

    field.set_value(5)
    assert field.value() == 5

    field = BaseField(name="test", default=5)
    assert field.value() == 5

    field = BaseField(name="test", nullable=True)
    assert field.value() is None
