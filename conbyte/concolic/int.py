# Copyright: see copyright.txt

import logging
from conbyte.concolic import Concolic, MetaFinal
from conbyte.utils import ConcolicObject, py2smt, unwrap
from conbyte.solver import Solver

log = logging.getLogger("ct.con.int")

class ConcolicInt(int, Concolic, metaclass=MetaFinal):
    def __new__(cls, value, expr=None, engine=None):
        assert type(value) is int
        obj = super().__new__(cls, value)
        obj.engine = engine if engine is not None else Solver._expr_has_engines_and_equals_value(expr, value)
        obj.value = py2smt(value)
        obj.expr = expr if expr is not None and obj.engine is not None else obj.value
        log.debug(f"ConInt, value: {value}, expr: {obj.expr}")
        return obj

    def __abs__(self, /): # <slot wrapper '__abs__' of 'int' objects>
        """abs(self)"""
        log.debug("ConInt, __abs__ is called")
        value = super().__abs__()
        expr = ["abs", self]
        return ConcolicObject(value, expr)

    def __add__(self, value, /): # <slot wrapper '__add__' of 'int' objects>
        """Return self+value."""
        log.debug("ConInt, __add__ is called")
        return self._bin_op('__add__', value)

    def __and__(self, value, /): # <slot wrapper '__and__' of 'int' objects> TODO
        """Return self&value."""
        log.debug("ConInt, __and__ is called")
        return ConcolicObject(super().__and__(unwrap(value)))

    def __bool__(self, /): # <slot wrapper '__bool__' of 'int' objects>
        """self != 0"""
        log.debug("ConInt, __bool__ is called")
        return super().__bool__() # We cannot return concolic objects here due to something like "while 1:".

    def __ceil__(self, *args, **kwargs): # <method '__ceil__' of 'int' objects>
        """Ceiling of an Integral returns itself."""
        log.debug("ConInt, __ceil__ is called"); args = [unwrap(arg) for arg in args]; kwargs = {k: unwrap(v) for (k, v) in kwargs.items()}
        value = super().__ceil__(*args, **kwargs)
        return ConcolicObject(value, self)

    # __class__, <class 'type'>

    # __delattr__, <slot wrapper '__delattr__' of 'object' objects>

    # __dir__, <method '__dir__' of 'object' objects>

    def __divmod__(self, value, /): # <slot wrapper '__divmod__' of 'int' objects> TODO
        """Return divmod(self, value)."""
        log.debug("ConInt, __divmod__ is called")
        return ConcolicObject(super().__divmod__(unwrap(value)))

    def __eq__(self, value, /): # <slot wrapper '__eq__' of 'int' objects>
        """Return self==value."""
        log.debug("ConInt, __eq__ is called")
        return self._bin_op('__eq__', value)

    # def __float__(self, /): # <slot wrapper '__float__' of 'int' objects>
    #     """float(self)"""

    def __floor__(self, *args, **kwargs): # <method '__floor__' of 'int' objects>
        """Flooring an Integral returns itself."""
        log.debug("ConInt, __floor__ is called"); args = [unwrap(arg) for arg in args]; kwargs = {k: unwrap(v) for (k, v) in kwargs.items()}
        value = super().__floor__(*args, **kwargs)
        return ConcolicObject(value, self)

    def __floordiv__(self, value, /): # <slot wrapper '__floordiv__' of 'int' objects>
        """Return self//value."""
        log.debug("ConInt, __floordiv__ is called")
        return self._bin_op('__floordiv__', value)

    def __format__(self, format_spec, /): # <method '__format__' of 'int' objects> TODO
        """Default object formatter."""
        log.debug("ConInt, __format__ is called")
        return ConcolicObject(super().__format__(unwrap(format_spec)))

    def __ge__(self, value, /): # <slot wrapper '__ge__' of 'int' objects>
        """Return self>=value."""
        log.debug("ConInt, __ge__ is called")
        return self._bin_op('__ge__', value)

    # def __getattribute__(self, name, /): # <slot wrapper '__getattribute__' of 'int' objects>
    #     """Return getattr(self, name)."""

    # def __getnewargs__(self, /): # <method '__getnewargs__' of 'int' objects>

    def __gt__(self, value, /): # <slot wrapper '__gt__' of 'int' objects>
        """Return self>value."""
        log.debug("ConInt, __gt__ is called")
        return self._bin_op('__gt__', value)

    def __hash__(self, /): # <slot wrapper '__hash__' of 'int' objects> TODO
        """Return hash(self)."""
        log.debug("ConInt, __hash__ is called")
        return ConcolicObject(super().__hash__())

    def __index__(self, /): # <slot wrapper '__index__' of 'int' objects>
        """Return self converted to an integer, if self is suitable for use as an index into a list."""
        log.debug("ConInt, __index__ is called")
        return super().__index__() # must return the primitive value for the use of low-level C functions

    # __init__, <slot wrapper '__init__' of 'object' objects>

    # __init_subclass__, <built-in method __init_subclass__ of type object at 0x903260>

    # def __int__(self, /): # <slot wrapper '__int__' of 'int' objects>
    #     """int(self)"""

    def __invert__(self, /): # <slot wrapper '__invert__' of 'int' objects> TODO
        """~self"""
        log.debug("ConInt, __invert__ is called")
        return ConcolicObject(super().__invert__())

    def __le__(self, value, /): # <slot wrapper '__le__' of 'int' objects>
        """Return self<=value."""
        log.debug("ConInt, __le__ is called")
        return self._bin_op('__le__', value)

    def __lshift__(self, value, /): # <slot wrapper '__lshift__' of 'int' objects>
        """Return self<<value."""
        log.debug("ConInt, __lshift__ is called")
        return ConcolicObject(super().__lshift__(unwrap(value)))

    def __lt__(self, value, /): # <slot wrapper '__lt__' of 'int' objects>
        """Return self<value."""
        log.debug("ConInt, __lt__ is called")
        return self._bin_op('__lt__', value)

    def __mod__(self, value, /): # <slot wrapper '__mod__' of 'int' objects>
        """Return self%value."""
        log.debug("ConInt, __mod__ is called")
        return self._bin_op('__mod__', value)

    def __mul__(self, value, /): # <slot wrapper '__mul__' of 'int' objects>
        """Return self*value."""
        log.debug("ConInt, __mul__ is called")
        return self._bin_op('__mul__', value)

    def __ne__(self, value, /): # <slot wrapper '__ne__' of 'int' objects>
        """Return self!=value."""
        log.debug("ConInt, __ne__ is called")
        return self._bin_op('__ne__', value)

    def __neg__(self, /): # <slot wrapper '__neg__' of 'int' objects>
        """-self"""
        log.debug("ConInt, __neg__ is called")
        value = super().__neg__()
        expr = ["-", self]
        return ConcolicObject(value, expr)

    def __or__(self, value, /): # <slot wrapper '__or__' of 'int' objects> TODO
        """Return self|value."""
        log.debug("ConInt, __or__ is called")
        return ConcolicObject(super().__or__(unwrap(value)))

    def __pos__(self, /): # <slot wrapper '__pos__' of 'int' objects>
        """+self"""
        log.debug("ConInt, __pos__ is called")
        value = super().__pos__()
        return ConcolicObject(value, self)

    def __pow__(self, value, mod=None, /): # <slot wrapper '__pow__' of 'int' objects> TODO
        """Return pow(self, value, mod)."""
        log.debug("ConInt, __pow__ is called")
        return ConcolicObject(super().__pow__(unwrap(value), unwrap(mod)))

    def __radd__(self, value, /): # <slot wrapper '__radd__' of 'int' objects>
        """Return value+self."""
        log.debug("ConInt, __radd__ is called")
        return self._bin_op('__radd__', value)

    def __rand__(self, value, /): # <slot wrapper '__rand__' of 'int' objects> TODO
        """Return value&self."""
        log.debug("ConInt, __rand__ is called")
        return ConcolicObject(super().__rand__(unwrap(value)))

    def __rdivmod__(self, value, /): # <slot wrapper '__rdivmod__' of 'int' objects> TODO
        """Return divmod(value, self)."""
        log.debug("ConInt, __rdivmod__ is called")
        return ConcolicObject(super().__rdivmod__(unwrap(value)))

    # __reduce__, <method '__reduce__' of 'object' objects>

    # __reduce_ex__, <method '__reduce_ex__' of 'object' objects>

    # def __repr__(self, /): # <slot wrapper '__repr__' of 'int' objects>
    #     """Return repr(self)."""

    def __rfloordiv__(self, value, /): # <slot wrapper '__rfloordiv__' of 'int' objects>
        """Return value//self."""
        log.debug("ConInt, __rfloordiv__ is called")
        return self._bin_op('__rfloordiv__', value)

    def __rlshift__(self, value, /): # <slot wrapper '__rlshift__' of 'int' objects> TODO
        """Return value<<self."""
        log.debug("ConInt, __rlshift__ is called")
        return ConcolicObject(super().__rlshift__(unwrap(value)))

    def __rmod__(self, value, /): # <slot wrapper '__rmod__' of 'int' objects>
        """Return value%self."""
        log.debug("ConInt, __rmod__ is called")
        return self._bin_op('__rmod__', value)

    def __rmul__(self, value, /): # <slot wrapper '__rmul__' of 'int' objects>
        """Return value*self."""
        log.debug("ConInt, __rmul__ is called")
        return self._bin_op('__rmul__', value)

    def __ror__(self, value, /): # <slot wrapper '__ror__' of 'int' objects> TODO
        """Return value|self."""
        log.debug("ConInt, __ror__ is called")
        return ConcolicObject(super().__ror__(unwrap(value)))

    def __round__(self, *args, **kwargs): # <method '__round__' of 'int' objects>
        """Rounding an Integral returns itself.\nRounding with an ndigits argument also returns an integer."""
        log.debug("ConInt, __round__ is called"); args = [unwrap(arg) for arg in args]; kwargs = {k: unwrap(v) for (k, v) in kwargs.items()}
        value = super().__round__(*args, **kwargs)
        return ConcolicObject(value, self)

    def __rpow__(self, value, mod=None, /): # <slot wrapper '__rpow__' of 'int' objects> TODO
        """Return pow(value, self, mod)."""
        log.debug("ConInt, __rpow__ is called")
        return ConcolicObject(super().__rpow__(unwrap(value), unwrap(mod)))

    def __rrshift__(self, value, /): # <slot wrapper '__rrshift__' of 'int' objects> TODO
        """Return value>>self."""
        log.debug("ConInt, __rrshift__ is called")
        return ConcolicObject(super().__rrshift__(unwrap(value)))

    def __rshift__(self, value, /): # <slot wrapper '__rshift__' of 'int' objects>
        """Return self>>value."""
        log.debug("ConInt, __rshift__ is called")
        return ConcolicObject(super().__rshift__(unwrap(value)))

    def __rsub__(self, value, /): # <slot wrapper '__rsub__' of 'int' objects>
        """Return value-self."""
        log.debug("ConInt, __rsub__ is called")
        return self._bin_op('__rsub__', value)

    def __rtruediv__(self, value, /): # <slot wrapper '__rtruediv__' of 'int' objects>
        """Return value/self."""
        log.debug("ConInt, __rtruediv__ is called")
        return self._bin_op('__rtruediv__', value)

    def __rxor__(self, value, /): # <slot wrapper '__rxor__' of 'int' objects> TODO
        """Return value^self."""
        log.debug("ConInt, __rxor__ is called")
        return ConcolicObject(super().__rxor__(unwrap(value)))

    # __setattr__, <slot wrapper '__setattr__' of 'object' objects>

    # def __sizeof__(self, /): # <method '__sizeof__' of 'int' objects>
    #     """Returns size in memory, in bytes."""

    # __str__, <slot wrapper '__str__' of 'object' objects>

    def __sub__(self, value, /): # <slot wrapper '__sub__' of 'int' objects>
        """Return self-value."""
        log.debug("ConInt, __sub__ is called")
        return self._bin_op('__sub__', value)

    # __subclasshook__, <built-in method __subclasshook__ of type object at 0x903260>

    def __truediv__(self, value, /): # <slot wrapper '__truediv__' of 'int' objects>
        """Return self/value."""
        log.debug("ConInt, __truediv__ is called")
        return self._bin_op('__truediv__', value)

    def __trunc__(self, *args, **kwargs): # <method '__trunc__' of 'int' objects>
        """Truncating an Integral returns itself."""
        log.debug("ConInt, __trunc__ is called"); args = [unwrap(arg) for arg in args]; kwargs = {k: unwrap(v) for (k, v) in kwargs.items()}
        value = super().__trunc__(*args, **kwargs)
        return ConcolicObject(value, self)

    def __xor__(self, value, /): # <slot wrapper '__xor__' of 'int' objects> TODO
        """Return self^value."""
        log.debug("ConInt, __xor__ is called")
        return ConcolicObject(super().__xor__(unwrap(value)))

    def as_integer_ratio(self, /): # <method 'as_integer_ratio' of 'int' objects> TODO
        """Return integer ratio.\n\nReturn a pair of integers, whose ratio is exactly equal to the original int\nand with a positive denominator.\n\n>>> (10).as_integer_ratio()\n(10, 1)\n>>> (-10).as_integer_ratio()\n(-10, 1)\n>>> (0).as_integer_ratio()\n(0, 1)"""
        log.debug("ConInt, as_integer_ratio is called")
        return ConcolicObject(super().as_integer_ratio())

    def bit_length(self, /): # <method 'bit_length' of 'int' objects> TODO
        """Number of bits necessary to represent self in binary.\n\n>>> bin(37)\n'0b100101'\n>>> (37).bit_length()\n6"""
        log.debug("ConInt, bit_length is called")
        return ConcolicObject(super().bit_length())

    def conjugate(self, *args, **kwargs): # <method 'conjugate' of 'int' objects>
        """Returns self, the complex conjugate of any int."""
        log.debug("ConInt, conjugate is called"); args = [unwrap(arg) for arg in args]; kwargs = {k: unwrap(v) for (k, v) in kwargs.items()}
        value = super().conjugate(*args, **kwargs)
        return ConcolicObject(value, self)

    @property
    def denominator(self): # <attribute 'denominator' of 'int' objects>
        """the denominator of a rational number in lowest terms"""
        log.debug("ConInt, denominator is called")
        return ConcolicObject(super().denominator) # should always return 1

    # from_bytes, <built-in method from_bytes of type object at 0x903260> (@classmethod)

    @property
    def imag(self): # <attribute 'imag' of 'int' objects>
        """the imaginary part of a complex number"""
        log.debug("ConInt, imag is called")
        return ConcolicObject(super().imag) # should always return 0

    @property
    def numerator(self): # <attribute 'numerator' of 'int' objects>
        """the numerator of a rational number in lowest terms"""
        log.debug("ConInt, numerator is called")
        value = super().numerator
        return ConcolicObject(value, self)

    @property
    def real(self): # <attribute 'real' of 'int' objects>
        """the real part of a complex number"""
        log.debug("ConInt, real is called")
        value = super().real
        return ConcolicObject(value, self)

    def to_bytes(self, /, length, byteorder, *, signed=False): # <method 'to_bytes' of 'int' objects> TODO
        """Return an array of bytes representing an integer."""
        log.debug("ConInt, to_bytes is called")
        return ConcolicObject(super().to_bytes(unwrap(length), unwrap(byteorder), signed=unwrap(signed)))

    ################################################################
    # Other helper methods are implemented in the following section.
    ################################################################

    def __bool2__(self):
        log.debug("ConInt, __bool2__ is called")
        value = super().__bool__()
        expr = ["not", ["=", self, "0"]]
        return ConcolicObject(value, expr)

    def __float2__(self, /): # our version of "def __float__(self, /):"
        log.debug("ConInt, __float2__ is called")
        value = super().__float__()
        expr = ['to_real', self]
        return ConcolicObject(value, expr)

    def __int2__(self):
        log.debug("ConInt, __int2__ is called")
        return self

    def __str2__(self):
        log.debug("ConInt, __str2__ is called")
        value = super().__str__()
        expr = ['ite', ['<', self, '0'], ['str.++', py2smt('-'), ["int.to.str", ['-', self]]], ["int.to.str", self]]
        return ConcolicObject(value, expr)

    def _bin_op(self, op, other):
        if op == '__add__':
            value = super().__add__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that int + float -> float instead of int,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['+', self, other]
            return ConcolicObject(value, expr)
        if op == '__eq__':
            value = super().__eq__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that (int = float) will convert int to float,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['=', self, other]
            return ConcolicObject(value, expr)
        if op == '__floordiv__':
            value = super().__floordiv__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that int.__floordiv__(float) will be changed to float.__rfloordiv__(int) in Python!
                # TODO: Currently not support the case when "other" is a float.
                # TODO: Currently not support the case when "other" is negative.
            else:
                try: other = int(other)
                except: other = 1
                other = self.__class__(other)
            expr = ['div', self, other]
            return ConcolicObject(value, expr)
        if op == '__ge__':
            value = super().__ge__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that (int >= float) will convert int to float,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['>=', self, other]
            return ConcolicObject(value, expr)
        if op == '__gt__':
            value = super().__gt__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that (int > float) will convert int to float,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['>', self, other]
            return ConcolicObject(value, expr)
        if op == '__le__':
            value = super().__le__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that (int <= float) will convert int to float,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['<=', self, other]
            return ConcolicObject(value, expr)
        if op == '__lt__':
            value = super().__lt__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that (int < float) will convert int to float,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['<', self, other]
            return ConcolicObject(value, expr)
        if op == '__mod__':
            value = super().__mod__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that int.__mod__(float) will be changed to float.__rmod__(int) in Python!
                # TODO: Currently not support the case when "other" is a float.
                # TODO: Currently not support the case when "other" is negative.
            else:
                try: other = int(other)
                except: other = 1
                other = self.__class__(other)
            expr = ['mod', self, other]
            return ConcolicObject(value, expr)
        if op == '__mul__':
            value = super().__mul__(unwrap(other))
            if not isinstance(other, Concolic):
                try: other = int(other)
                except: other = 1
                other = ConcolicObject(other)
            expr = ['*', self, other]
            return ConcolicObject(value, expr)
        if op == '__ne__':
            value = super().__ne__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that (int != float) will convert int to float,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['not', ['=', self, other]]
            return ConcolicObject(value, expr)
        if op == '__radd__':
            value = super().__radd__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that float + int -> float instead of int,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['+', other, self]
            return ConcolicObject(value, expr)
        if op == '__rfloordiv__':
            value = super().__rfloordiv__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # TODO: Currently not support the case when "other" is a float.
                # TODO: Currently not support the case when "other" is negative.
            else:
                try: other = int(other)
                except: other = 1
                other = self.__class__(other)
            expr = ['div', other, self]
            return ConcolicObject(value, expr)
        if op == '__rmod__':
            value = super().__rmod__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # TODO: Currently not support the case when "other" is a float.
                # TODO: Currently not support the case when "other" is negative.
            else:
                try: other = int(other)
                except: other = 1
                other = self.__class__(other)
            expr = ['mod', other, self]
            return ConcolicObject(value, expr)
        if op == '__rmul__':
            value = super().__rmul__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that float * int -> float instead of int,
                # so we cannot convert float to int here!
                # TODO: Currently not support the case when "other" is a list.
                # TODO: Currently not support the case when "other" is a str.
            else:
                try: other = float(other)
                except: other = 1.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['*', other, self]
            return ConcolicObject(value, expr)
        if op == '__rsub__':
            value = super().__rsub__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that int - float -> float instead of int,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['-', other, self]
            return ConcolicObject(value, expr)
        if op == '__rtruediv__':
            value = super().__rtruediv__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that int / float -> float instead of int,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['/', other, self]
            return ConcolicObject(value, expr)
        if op == '__sub__':
            value = super().__sub__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that int - float -> float instead of int,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 0.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['-', self, other]
            return ConcolicObject(value, expr)
        if op == '__truediv__':
            value = super().__truediv__(unwrap(other))
            if isinstance(other, Concolic):
                if isinstance(other, bool): other = other.__int2__()
                # Please note that int / float -> float instead of int,
                # so we cannot convert float to int here!
            else:
                try: other = float(other)
                except: other = 1.0
                if other == (t:=int(other)): other = t
                other = ConcolicObject(other)
            expr = ['/', self, other]
            return ConcolicObject(value, expr)
        raise NotImplementedError