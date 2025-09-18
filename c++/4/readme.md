# Concepts

* Destructors & RAII (resource acquisition is initialization). This means that a resource is acquired in the object's constructor, and released in the destructor. 

* C++ uses a _constructor chain_ -- base constructors run first, then derived constructors. 

* touching in encapsulation as well in this one -- setters, getters, `private`, `public`, `protected`

## public, private, and protected inheritance

### How Access Modifiers on Inherited Classes Work:

*Public Inheritance:* When a class inherits publicly from a base class, the public members of the base class remain public in the derived class, and protected members remain protected. Private members of the base class are never directly accessible to the derived class, regardless of the inheritance type. This is the most common form of inheritance and represents an "is-a" relationship, where the derived class is a specialized version of the base class and exposes its public interface. 
```C++
    class Base {
    public:
        int public_member;
    protected:
        int protected_member;
    private:
        int private_member;
    };

    class Derived : public Base {
        // public_member is public
        // protected_member is protected
        // private_member is not accessible
    };
```
*Protected Inheritance:* With protected inheritance, public and protected members of the base class become protected members in the derived class. This means they are accessible within the derived class and its further derived classes, but not from outside the derived class. Private members remain inaccessible. This type of inheritance is used when you want the derived class to inherit the implementation but not expose the public interface of the base class to external users. 
```C++

    class Base {
    public:
        int public_member;
    protected:
        int protected_member;
    };

    class Derived : protected Base {
        // public_member is protected
        // protected_member is protected
    };
```

*Private Inheritance:* In private inheritance, public and protected members of the base class become private members in the derived class. They are only accessible within the derived class itself and are not exposed to any further derived classes or external code. Private inheritance is often used for implementation inheritance, where the derived class uses the base class's functionality internally without exposing its interface. 
```C++

    class Base {
    public:
        int public_member;
    protected:
        int protected_member;
    };

    class Derived : private Base {
        // public_member is private
        // protected_member is private
    };
```
## Notes on virtual constructors/deconstructors

* Constructors cannot be marked virtual.
* polymorphic destructors *should* be marked virtual. If they're not, then derived destructors won't be run if you delete a base object. 

```cpp
struct Base {
    virtual ~Base() { std::cout << "Base dtor\n"; }
};

struct Child : Base {
    ~Child() override { std::cout << "Child dtor\n"; }
};

Base* b = new Child();
delete b;
// Output:
// Child dtor
// Base dtor
```

the above will only run 

* Virtual dispatch doesn't work during construction. Only the base version of a method runs, because dynamic dispatch cannot occur, because the derived part of the object isn't built yet. 

### other random notes

* private members of a base class can't be directly accessed by derived classes. 
* `protected` members, however, can be. 
* to access private members of a base class, you must create setters/getters in the base class, and presumably not override those setters and getters in subclasses. 
* implementations of methods directly in a class definition are implicitly inline. 


## Make it, run it
```sh
kbuchmil@TAMARIND:~/git/snippets/c++/3$ g++ -g -Wall example.cpp -o example
kbuchmil@TAMARIND:~/git/snippets/c++/3$ ./example
Child
Child
Child
```