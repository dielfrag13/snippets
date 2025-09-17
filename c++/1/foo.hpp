#include <iostream>
class Foo {

private:
    int lol_; 

public:
    // declare the constructor (no parameters)
    // no return type -- not even void
    Foo();
    // Constructor overloading -- this one takes one int
    Foo(int x);   // the term here is 'delegation'. 

    void method_1(std::string);  // usual method

    // declare the destructor
    ~Foo();

}; // classes end in semicolon?

