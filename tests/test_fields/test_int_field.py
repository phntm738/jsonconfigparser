from jsonconfigparser.fields import IntField
from jsonconfigparser import exceptions
import pytest


def test_int_field_value():
    field = IntField()

    with pytest.raises(exceptions.NoValueError):
        val = field.value()

    with pytest.raises(exceptions.InvalidValueError):
        field.set_value('aa')

    with pytest.raises(exceptions.InvalidValueError):
        field.set_value(1.1)

    with pytest.raises(exceptions.InvalidValueError):
        field._value = 'aa'
        val = field.value()

    with pytest.raises(exceptions.InvalidValueError):
        field._value = 1.1
        val = field.value()

    field.set_value(5)
    assert field.value() == 5

    field = IntField(
        default=5
    )

    assert field.value() == 5

    with pytest.raises(exceptions.InvalidDefaultType):
        field = IntField(
            default='test'
        )

    with pytest.raises(exceptions.InvalidDefaultType):
        field = IntField(
            default=1.1
        )

    field = IntField(
        nullable=True
    )

    assert field.value() is None
