from jsonconfigparser.fields import StringField
from jsonconfigparser import exceptions
import pytest


def test_string_field_value():
    field = StringField()

    with pytest.raises(exceptions.NoValueError):
        val = field.value()

    with pytest.raises(exceptions.InvalidValueError):
        field.set_value(5)

    with pytest.raises(exceptions.InvalidValueError):
        field._value = 5
        val = field.value()

    field.set_value('test')
    assert field.value() == 'test'

    field = StringField(
        default='test'
    )

    assert field.value() == 'test'

    with pytest.raises(exceptions.InvalidDefaultType):
        field = StringField(
            default=5
        )

    field = StringField(
        nullable=True
    )

    assert field.value() is None


def test_string_field_length_validation():
    with pytest.raises(exceptions.InvalidParametersError):
        field = StringField(
            min_length=-1
        )

    with pytest.raises(exceptions.InvalidParametersError):
        field = StringField(
            max_length=0
        )

    with pytest.raises(exceptions.InvalidParametersError):
        field = StringField(
            min_length=5,
            max_length=4
        )

    field = StringField(
        min_length=3,
        max_length=5
    )

    with pytest.raises(exceptions.ValidationFailedError):
        field.set_value('aa')

    with pytest.raises(exceptions.DefaultValueValidationFailedError):
        field = StringField(
            default="aa",
            min_length=3,
            max_length=5
        )
