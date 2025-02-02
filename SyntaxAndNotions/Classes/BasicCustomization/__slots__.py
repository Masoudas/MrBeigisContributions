"""
__slots__ allow us to explicitly declare data members (like properties) and deny the creation of __dict__ and 
__weakref__ (unless explicitly declared in __slots__ or available in a parent.)

The space saved over using __dict__ can be significant. Attribute lookup speed can be significantly improved as 
well.

	-	object.__slots__
This class variable can be assigned a string, iterable, or sequence of strings with variable names used by 
instances. __slots__ reserves space for the declared variables and prevents the automatic creation of __dict__ and 
__weakref__ for each instance.

	-	Notes on using __slots__
When inheriting from a class without __slots__, the __dict__ and __weakref__ attribute of the instances will always 
be accessible.

Without a __dict__ variable, instances cannot be assigned new variables not listed in the __slots__ definition. 
Attempts to assign to an unlisted variable name raises AttributeError. If dynamic assignment of new variables is 
desired, then add '__dict__' to the sequence of strings in the __slots__ declaration.

Without a __weakref__ variable for each instance, classes defining __slots__ do not support weak references to its 
instances. If weak reference support is needed, then add '__weakref__' to the sequence of strings in the __slots__ 
declaration.

__slots__ are implemented at the class level by creating descriptors (Implementing Descriptors) for each variable 
name. As a result, class attributes cannot be used to set default values for instance variables defined by 
__slots__; otherwise, the class attribute would overwrite the descriptor assignment.

The action of a __slots__ declaration is not limited to the class where it is defined. __slots__ declared in parents 
are available in child classes. However, child subclasses will get a __dict__ and __weakref__ unless they also 
define __slots__ (which should only contain names of any additional slots).

If a class defines a slot also defined in a base class, the instance variable defined by the base class slot is 
inaccessible (except by retrieving its descriptor directly from the base class). This renders the meaning of the 
program undefined. In the future, a check may be added to prevent this.

Nonempty __slots__ does not work for classes derived from “variable-length” built-in types such as int, bytes and 
tuple.

Any non-string iterable may be assigned to __slots__. Mappings may also be used; however, in the future, special 
meaning may be assigned to the values corresponding to each key.

__class__ assignment works only if both classes have the same __slots__.

Multiple inheritance with multiple slotted parent classes can be used, but only one parent is allowed to have 
attributes created by slots (the other bases must have empty slot layouts) - violations raise TypeError.

If an iterator is used for __slots__ then a descriptor is created for each of the iterator’s values. However, 
the __slots__ attribute will be an empty iterator.
"""