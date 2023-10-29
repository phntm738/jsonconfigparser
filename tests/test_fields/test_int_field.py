from jsonconfigparser.fields import IntField
from jsonconfigparser.exceptions import field_errors
import pytest


def test_int_field_value():
    field = IntField()

    with pytest.raises(field_errors.NoNameError):
        val = field.value()

    field.name = "test"

    with pytest.raises(field_errors.NoValueError):
        val = field.value()

    with pytest.raises(field_errors.InvalidValueTypeError):
        field.set_value("aa")

    with pytest.raises(field_errors.InvalidValueTypeError):
        field.set_value(1.1)

    with pytest.raises(field_errors.InvalidValueTypeError):
        field._value = "aa"
        val = field.value()

    with pytest.raises(field_errors.InvalidValueTypeError):
        field._value = 1.1
        val = field.value()

    field.set_value(5)
    assert field.value() == 5

    field = IntField(name="test", default=5)

    assert field.value() == 5

    with pytest.raises(field_errors.InvalidDefaultTypeError):
        field = IntField(name="test", default="test")

    with pytest.raises(field_errors.InvalidDefaultTypeError):
        field = IntField(name="test", default=1.1)

    field = IntField(name="test", nullable=True)

    assert field.value() is None
