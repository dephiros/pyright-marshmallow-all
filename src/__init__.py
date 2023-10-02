import marshmallow
from marshmallow.fields import Field

def test():
    TestSchema().dump({})
    raise marshmallow.ValidationError("This is a test")
test()

class TestSchema(marshmallow.Schema):
    pass

class PinCode(Field):
    """Field that serializes to a string of numbers and deserializes
    to a list of numbers.
    """

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return "".join(str(d) for d in value)

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return [int(c) for c in value]
        except ValueError as error:
            raise marshmallow.ValidationError("Pin codes must contain only digits.") from error
