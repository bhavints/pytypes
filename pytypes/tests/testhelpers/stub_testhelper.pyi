'''
Created on 21.10.2016

@author: Stefan Richthofer
'''

from typing import Any, TypeVar, Generic, Generator, Iterable, Sequence, \
		Tuple, List, Callable, Dict, Mapping, Union
from numbers import Real

def testfunc1(a: int, b: Real) -> str: ...

class class1():
	def meth1(self, a: float, b: str) -> str: ...
	def meth2(self, d, c: str) -> int: ...

	@staticmethod
	def static_meth(d, c: str) -> int: ...

	@classmethod
	def class_meth(cls, a: str, b: int) -> float: ...

	class class1_inner():
		def inner_meth1(self, a: float, b: str) -> int: ...

		@staticmethod
		def inner_static_meth(d: float, c: str) -> int: ...


class class2(class1):
	def meth1b(self, a) -> str: ...

	def meth2b(self, b: class1) -> str: ...


def testfunc_class_in_list(a: List[class1]) -> int: ...



def testfunc_None_ret(a: int, b: Real) -> None: ...

def testfunc_None_ret_err(a: int, b: Real) -> None: ...

def testfunc_None_arg(a: int, b: None) -> int: ...

def testfunc_Dict_arg(a: int, b: Dict[str, Union[int, str]]) -> None: ...

def testfunc_Mapping_arg(a: int, b: Mapping[str, Union[int, str]]) -> None: ...

def testfunc_Dict_ret(a: str) -> Dict[str, Union[int, str]]: ...

def testfunc_Dict_ret_err(a: int) -> Dict[str, Union[int, str]]: ...

def testfunc_Seq_arg(a: Sequence[Tuple[int, str]]) -> int: ...

def testfunc_Seq_ret_List(a: int, b: str) -> Sequence[Union[int, str]]: ...

def testfunc_Seq_ret_Tuple(a: int, b: str) -> Sequence[Union[int, str]]: ...

def testfunc_Seq_ret_err(a: int, b: str) -> Sequence[Union[int, str]]: ...

def testfunc_Iter_arg(a: Iterable[int], b: str) -> List[int]: ...

def testfunc_Iter_str_arg(a: Iterable[str]) -> List[int]: ...

def testfunc_Iter_ret() -> Iterable[int]: ...

def testfunc_Iter_ret_err() -> Iterable[str]: ...

def testfunc_Callable_arg(a: Callable[[str, int], str], b: str) -> str: ...

def testfunc_Callable_call_err(a: Callable[[str, int], str], b: str) -> str: ...

def testfunc_Callable_ret(a: int, b: str) -> Callable[[str, int], str]: ...

def testfunc_Callable_ret_err() -> Callable[[str, int], str]: ...

def testfunc_Generator() -> Generator[int, Union[str, None], Any]: ...

def testfunc_Generator_arg(gen: Generator[int, Union[str, None], Any]) -> List[int]: ...

def testfunc_Generator_ret() -> Generator[int, Union[str, None], Any]: ...

T_1 = TypeVar('T_1')
class Custom_Generic(Generic[T_1]):
	
	def __init__(self, val: T_1) -> None: ...

	def v(self) -> T_1: ...


def testfunc_Generic_arg(x: Custom_Generic[str]) -> str: ...

def testfunc_Generic_ret(x: int) -> Custom_Generic[int]: ...

def testfunc_Generic_ret_err(x: int) -> Custom_Generic[int]: ...


class testClass_property(object):

	@property
	def testprop(self) -> int: ...

	@testprop.setter
	def testprop(self, value: int) -> None: ...

	@property
	def testprop2(self) -> str: ...

	@testprop2.setter
	def testprop2(self, value: str) -> None: ...

	@property
	def testprop3(self) -> Tuple[int, str]: ...

	@testprop3.setter
	def testprop3(self, value: Tuple[int, str]) -> None: ...


class testClass_property_class_check(object):
	@property
	def testprop(self) -> int: ...

	@testprop.setter
	def testprop(self, value: int) -> None: ...

	@property
	def testprop2(self) -> float: ...

	@testprop2.setter
	def testprop2(self, value: float) -> None: ...


def testfunc_varargs1(*argss: float) -> Tuple[int, float]: ...

def testfunc_varargs2(a: str, b: int, c: None,
		*varg: int) -> Tuple[int, str]: ...

def testfunc_varargs3(*args: int, **kwds: float) -> Tuple[str, float]: ...

def testfunc_varargs4(**kwds: float) -> float: ...

def testfunc_varargs5(a1: int, a2: str, *vargss: float,
		**vkwds: int) -> List[int]: ...

def testfunc_varargs6(a1: int, a2: str, *vargss: float,
		b1: int, b2: str, **vkwds: int) -> List[int]: ...

def testfunc_varargs6b(a1, a2, *vargss, b1, b2, **vkwds):
	# type: (int, str, *float, int, str, **int) -> List[int]
	...

def testfunc_varargs_err(a1: int, a2: str, *vargss: float,
		**vkwds: int) -> List[int]: ...

class testclass_vararg():
	def testmeth_varargs1(self, *vargs: Tuple[str, int]) -> int: ...

	def testmeth_varargs2(self, q1: int, q2: str, *varargs: float,
			**varkw: int) -> List[int]: ...

	def testmeth_varargs3(self, q1: int, q2: str, *varargs: float,
			w1: float, w2: Tuple[int, str], **varkw: int) -> List[int]: ...

	def testmeth_varargs_ca3b(self, q1, q2, *varargs, w1, w2, **varkw):
		# type: (int, str, *float, float, Tuple[int, str], **int) -> List[int]
		...

	@staticmethod
	def testmeth_varargs_static1(*vargs_st: float) -> Tuple[int, float]: ...

	@staticmethod
	def testmeth_varargs_static2(q1_st: int, q2_st: str, *varargs_st: float,
			**varkw_st: int) -> List[int]: ...

	@classmethod
	def testmeth_varargs_class1(cls, *vargs_cls: Tuple[str, int]) -> int: ...

	@classmethod
	def testmeth_varargs_class2(cls, q1_cls: int, q2_cls: str,
			*varargs_cls: float, **varkw_cls: int) -> List[int]: ...

	@property
	def prop1(self) -> str: ...

	@prop1.setter
	def prop1(self, *vargs_prop: str) -> None: ...

def testfunc_varargs_ca1(*argss: float) -> Tuple[int, float]: ...

def testfunc_varargs_ca2(a: str, b: int, c: None,
		*varg: int) -> Tuple[int, str]: ...

def testfunc_varargs_ca3(*args: int, **kwds: float) -> Tuple[str, float]: ...

def testfunc_varargs_ca4(**kwds: float) -> float: ...

def testfunc_varargs_ca5(a1: int, a2: str, *vargss: float,
		**vkwds: int) -> List[int]: ...

def testfunc_varargs_ca6(a1: int, a2: str, *vargss: float,
		b1: int, b2: str, **vkwds: int) -> List[int]: ...

def testfunc_varargs_ca6b(a1, a2, *vargss, b1, b2, **vkwds):
	# type: (int, str, *float, int, str, **int) -> List[int]
	...

class testclass_vararg_ca():
	def testmeth_varargs_ca1(self, *vargs: Tuple[str, int]) -> int: ...

	def testmeth_varargs_ca2(self, q1: int, q2: str,
			*varargs: float, **varkw: int) -> List[int]: ...

	def testmeth_varargs_ca3(self, q1: int, q2: str, *varargs: float,
			w1: float, w2: Tuple[int, str], **varkw: int) -> List[int]: ...

	def testmeth_varargs_ca3b(self, q1, q2, *varargs, w1, w2, **varkw):
		# type: (int, str, *float, float, Tuple[int, str], **int) -> List[int]
		...

	@staticmethod
	def testmeth_varargs_static_ca1(*vargs_st: float) -> Tuple[int, float]: ...

	@staticmethod
	def testmeth_varargs_static_ca2(q1_st: int, q2_st: str,
			*varargs_st: float, **varkw_st: int) -> List[int]: ...

	@classmethod
	def testmeth_varargs_class_ca1(cls, *vargs_cls: Tuple[str, int]) -> int: ...

	@classmethod
	def testmeth_varargs_class_ca2(cls, q1_cls: int, q2_cls: str,
			*varargs_cls: float, **varkw_cls: int) -> List[int]: ...

	@property
	def prop_ca1(self) -> str: ...

	@prop_ca1.setter
	def prop_ca1(self, *vargs_prop: str) -> None: ...


def func_defaults_typecheck(a: str, b, c, d) -> str: ...
def func_defaults_checkargs(a: str, b, c, d) -> str: ...
def func_defaults_annotations(a: str, b, c) -> str: ...

def testfunc_annotations_from_stubfile_by_decorator(a: str, b: int) -> int: ...
