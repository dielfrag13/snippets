#include "foo.hpp"
#include <iostream>

Foo::Foo(int x) {
    std::cout << "setting lol_ to " << x << "...\n";
    lol_ = x;
}

// the class is Foo (the first one), and the method is Foo (the second one).
// Constructor delegation: this constructor calls another constructor 
Foo::Foo() : Foo(0) {

    // this appears to run after the other constructor
    std::cout << "Hello from no-arg constructor!" << "\n";

    // now you can access the things within and do stuff with them
    lol_++;
    std::cout << "but added one lol\n";
}


// destructor
Foo::~Foo() {
    std::cout << "destruction. lol_ count: " << lol_ << "\n";
}

void Foo::method_1(std::string s) {
    std::cout << "method 1: " << s << "\n";
    lol_++;
    return;
} // method implementations do not need semicolon



