# Virtual Function

A virtual function is a member function which is declared within a base class and is re-defined(Overriden) by a derived class. When you refer to a derived class object using a pointer or a reference to the base class, you can call a virtual function for that object and execute the derived class’s version of the function.

 - Virtual functions ensure that the correct function is called for an object, regardless of the type of reference (or pointer) used for function call.
 - They are mainly used to achieve **Runtime polymorphism**
 - The resolving of function call is done at Run-time.
 - Virtual functions can **NOT** be static and also can **NOT** be a friend function of another class.
 - Virtual functions should be accessed using pointer or reference of base class type to achieve run time polymorphism.
 - The prototype of virtual functions should be same in base as well as derived class.
 - They are always defined in base class and overridden in derived class. It is not mandatory for derived class to override (or re-define the virtual function), in that case base class version of function is used.
 - A class may have **virtual destructor** but it can **NOT** have a virtual constructor.

# Late Binding & Early Binding

Late binding (Runtime) is done in accordance with the content of pointer (i.e. location pointed to by pointer) and Early binding (Compile time) is done according to the type of pointer.

# Working of virtual functions (concept of VTABLE and VPTR)

 - If object of that class is created then a **virtual pointer(VPTR)** is inserted as a data member of the class to point to **VTABLE** of that class.
 - Irrespective of object is created or not, a static array of function pointer called **VTABLE** where each cell contains the address of each virtual function contained in that class.

![](https://media.geeksforgeeks.org/wp-content/uploads/VirtualFunctionInC.png)

# References

1. [Virtual Function in C++](https://www.geeksforgeeks.org/virtual-function-cpp/)