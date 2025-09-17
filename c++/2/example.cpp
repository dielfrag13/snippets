// goal is to demonstrate virtual functions and polymorphism
#include "iostream"

// difference between a struct and a class? Not much, actually
// Only difference is the default access level:
//  * in a struct, members and base classes are public by default
//    * use structs to group plain data objects or just bundles of fields
//  * in a class, members and base classes are private by default
//    * use classes when you want to emphasize "this has behavior, not just data"

struct ExampleBase { int x; };

struct Derived : ExampleBase {};   // default is public inheritance
// Equivalent to: struct Derived : public Base {};

class Derived2 : ExampleBase {};   // default is private inheritance
// Equivalent to: class Derived2 : private Base {};


// marking the method as 'virtual' means the method can be overridden 
struct Base { virtual void speak() {std::cout << "Base\n"; }};
// can only override virtual functions. trying to override non-virtual function yields error that looks like this:
/*
example.cpp:25:28: error: ‘void Child::speak()’ marked ‘override’, but does not override
   25 | struct Child : Base { void speak() override {std::cout << "Child\n"; }};
*/
struct Child : Base { void speak() override {std::cout << "Child\n"; }};
struct Child_Two : Base {void speak() {std::cout << "Child_Two\n";}};

// unlike the above true overriding, this technique 'hides' the method and requires explicit indication
// if you want to call the superclass variant of the method
struct Base2 {void speak() {std::cout << "Base2\n"; }};
struct Child2 : Base2 { void speak() {std::cout << "Child2\n"; }};

int main(void) {
    Base *b = new Child();
    Base *bb = new Base();
    Base *bbb = new Child_Two();
    b->speak();             // outputs 'Child' as speak() is overridden
    bb->speak();            // outputs 'Base' as this is the default implementation
    bbb->speak();           // outputs 'Child_Two'-- speak() is overridden still cuz the 'override' keyword is not required
                            // but don't exclude it cuz it shoots you in the foot in a variety of ways if you mess up
    std::cout << std::endl;

    Base2 *b2 = new Child2();
    Base2 *bb2 = new Base2();
    Child2 *c2 = new Child2();
    b2->speak();            // outputs 'Base2' as the method referenced is based on the type of the variable now
    bb2->speak();           // outputs 'Base2' for the same reason
    c2->speak();            // outputs 'Child2' as now the type of the variable is child, so it refers to child implementation
    c2->Base2::speak();     // outputs 'Base2' now as we explicitly refer to the base2 version

    return 1;
}

