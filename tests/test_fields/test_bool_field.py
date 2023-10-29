from jsonconfigparser.fields import BoolField
from jsonconfigparser.exceptions import field_errors
import pytest


def test_bool_field_value():
    field = BoolField()

    with pytest.raises(field_errors.NoNameError):
        val = field.value()

    field.name = "test"

    with pytest.raises(field_errors.NoValueError):
        val = field.value()

    with pytest.raises(field_errors.InvalidValueTypeError):
        field.set_value("aa")

    with pytest.raises(field_errors.InvalidValueTypeError):
        field._value = "aa"
        val = field.value()

    field.set_value(True)
    assert field.value() == True

    field = BoolField(name="test", default=True)

    assert field.value() == True

    with pytest.raises(field_errors.InvalidDefaultTypeError):
        field = BoolField(name="test", default="test")

    field = BoolField(name="test", nullable=True)

    assert field.value() is None
