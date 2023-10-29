from jsonconfigparser.fields import FloatField
from jsonconfigparser.exceptions import field_errors
from jsonconfigparser.exceptions import validator_errors
import pytest


def test_number_field_value():
    field = FloatField()

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

    field.set_value(5)
    assert field.value() == 5

    field = FloatField(name="test", default=5)

    assert field.value() == 5

    with pytest.raises(field_errors.InvalidDefaultTypeError):
        field = FloatField(name="test", default="test")

    field = FloatField(name="test", nullable=True)

    assert field.value() is None


def test_number_field_comparison_validation():
    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", gt=5, lt=4)

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", ge=5, lt=4)

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", gt=5, le=4)

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", ge=5, le=4)

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", gt=5, lt=4)

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", gt=5, ge=4)

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", lt=5, le=4)

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", gt="a")

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", ge="a")

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", lt="a")

    with pytest.raises(validator_errors.InvalidArgumentError):
        field = FloatField(name="test", le="a")

    field = FloatField(name="test", gt=3, lt=4)

    with pytest.raises(field_errors.InvalidValueError):
        field.set_value(5)

    with pytest.raises(field_errors.InvalidDefaultError):
        field = FloatField(name="test", default=5, gt=3, lt=4)
