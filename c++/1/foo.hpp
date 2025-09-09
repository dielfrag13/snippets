#include <iostream>
class Foo {

private:
    int lol_; 

public:
    // declare the constructor (no parameters)
    // no return type -- not even void
    Foo();
    
    // Constructor overloading -- this one takes one int
    // the term here is 'delegation'. 
    Foo(int x); 



    int public_var1;


    // usual method
    void method_1(std::string);


    // declare the destructor
    ~Foo();



}; // classes end in semicolon?

