from jsonconfigparser.fields import NumberField
from jsonconfigparser import exceptions
import pytest


def test_number_field_value():
    field = NumberField()

    with pytest.raises(exceptions.NoValueError):
        val = field.value()

    with pytest.raises(exceptions.InvalidValueError):
        field.set_value('aa')

    with pytest.raises(exceptions.InvalidValueError):
        field._value = 'aa'
        val = field.value()

    field.set_value(5)
    assert field.value() == 5

    field = NumberField(
        default=5
    )

    assert field.value() == 5

    with pytest.raises(exceptions.InvalidDefaultType):
        field = NumberField(
            default='test'
        )

    field = NumberField(
        nullable=True
    )

    assert field.value() is None


def test_number_field_comparison_validation():
    with pytest.raises(exceptions.InvalidParametersError):
        field = NumberField(
            gt=5,
            lt=4
        )

    with pytest.raises(exceptions.InvalidParametersError):
        field = NumberField(
            ge=5,
            lt=4
        )

    with pytest.raises(exceptions.InvalidParametersError):
        field = NumberField(
            gt=5,
            le=4
        )

    with pytest.raises(exceptions.InvalidParametersError):
        field = NumberField(
            ge=5,
            le=4
        )

    with pytest.raises(exceptions.InvalidParametersError):
        field = NumberField(
            gt=5,
            lt=4
        )

    with pytest.raises(exceptions.InvalidParametersError):
        field = NumberField(
            gt=5,
            ge=4
        )

    with pytest.raises(exceptions.InvalidParametersError):
        field = NumberField(
            lt=5,
            le=4
        )

    field = NumberField(
        gt=3,
        lt=4
    )

    with pytest.raises(exceptions.ValidationFailedError):
        field.set_value(5)

    with pytest.raises(exceptions.DefaultValueValidationFailedError):
        field = NumberField(
            default=5,
            gt=3,
            lt=4
        )
