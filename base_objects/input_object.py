   
# class InputObj:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self._value)

#     def __eq__(self, other):
#         if isinstance(other, InputObj):
#             return self._value == other._value
#         return False

#     @property
#     def value(self):
#         return self._value

#     @value.setter
#     def value(self, v):
#         self._value = self.validate(v)

#     def validate(self, v):
#         return v
