# Concepts

* Virtual functions & polymorphism
    *  A virtual function in C++ is a member function declared in a base class using the virtual keyword, which can be overridden by a derived class. Its primary purpose is to enable runtime polymorphism, allowing the correct function to be called based on the actual type of the object being pointed to or referenced, rather than the type of the pointer or reference itself.
    * the 'override' keyword is recommended, but not required. 
    * if a method is not marked as virtual in a superclass, then the function to call is determined at compile time based on the static type of the variable. NOT true polymorphism. 
    * if a method is marked as virtual, then its calls are resolved at runtime based on the dynamic type -- dynamic dispatch.
    TRUE polymorphism.

* Classes vs structs? not much difference
  * Structs intended to be used as bundles of fields, and members are public by default
  * classes are intended to emphasize 'this has behavior, not just data' and members are private by default

* Pro tips
  * avoid passing polymorphic objects by value. Use pointers or references. 

## make it, run it

```sh
kbuchmil@TAMARIND:~/git/snippets/c++/2$ g++ -g -Wall example.cpp -o example
kbuchmil@TAMARIND:~/git/snippets/c++/2$ ./example
Child
Base
Child_Two

Base2
Base2
Child2
Base2
```

