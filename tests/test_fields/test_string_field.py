from jsonconfigparser.fields import StringField
from jsonconfigparser.exceptions import field_errors
from jsonconfigparser.exceptions import validator_errors
import pytest


def test_string_field_value():
    field = StringField()

    with pytest.raises(field_errors.NoNameError):
        val = field.value()

    field.name = "test"

    with pytest.raises(field_errors.NoValueError):
        val = field.value()

    with pytest.raises(field_errors.InvalidValueTypeError):
        field.set_value(5)

    with pytest.raises(field_errors.InvalidValueTypeError):
        field._value = 5
        val = field.value()

    field.set_value("test")
    assert field.value() == "test"

    field = StringField(name="test", default="test")

    assert field.value() == "test"

    with pytest.raises(field_errors.InvalidDefaultTypeError):
        field = StringField(name="test", default=5)

    field = StringField(name="test", nullable=True)

    assert field.value() is None


def test_string_field_length_validation():
    with pytest.raises(validator_errors.InvalidArgumentError):
        field = StringField(name="test", min_length=-1)

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = StringField(name="test", max_length=0)

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = StringField(name="test", min_length=5, max_length=4)

    field = StringField(name="test", min_length=3, max_length=5)

    with pytest.raises(field_errors.InvalidValueError):
        field.set_value("aa")

    with pytest.raises(field_errors.InvalidDefaultError):
        field = StringField(name="test", default="aa", min_length=3, max_length=5)
