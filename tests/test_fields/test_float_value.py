from jsonconfigparser.fields import FloatField
from jsonconfigparser import exceptions
import pytest


def test_float_field_value():
    field = FloatField()

    with pytest.raises(exceptions.NoValueError):
        val = field.value()

    with pytest.raises(exceptions.InvalidValueError):
        field.set_value('aa')

    with pytest.raises(exceptions.InvalidValueError):
        field._value = 'aa'
        val = field.value()

    field.set_value(5)
    assert field.value() == 5.0
    assert isinstance(field.value(), float)

    field = FloatField(
        default=5
    )

    assert field.value() == 5.0
    assert isinstance(field.value(), float)

    with pytest.raises(exceptions.InvalidDefaultType):
        field = FloatField(
            default='test'
        )

    field = FloatField(
        nullable=True
    )

    assert field.value() is None
