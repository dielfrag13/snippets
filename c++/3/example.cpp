#include <iostream>

struct AbstractBase {
    virtual void speak() = 0; 
    void haha() {std::cout << "AbstractBase\n";}

};

struct Child : AbstractBase { 
    void speak() {
        std::cout << "Child\n"; 
    }
};

// Can't initialize a Child2 as it hasn't implemented the abstract method!
struct Child2 : AbstractBase {
    void haha() {
        std::cout << "Child2 haha\n";
    }
};

int main(void) {

    // creation using pointers
    Child *c = new Child();

    // setting up references
    Child c2;
    Child &c2_ref = c2;

    c->speak();         // syntax for raw pointer
    c2.speak();         // syntax for non-pointer
    c2_ref.speak();     // syntax for reference

    // Child2 *child2 = new Child2();     X -- error, looks like this:


    /*
    example.cpp: In function ‘int main()’:
example.cpp:34:33: error: invalid new-expression of abstract class type ‘Child2’
   34 |     Child2 *child2 = new Child2();
      |                                 ^
example.cpp:15:8: note:   because the following virtual functions are pure within ‘Child2’:
   15 | struct Child2 : AbstractBase {
      |        ^~~~~~
example.cpp:4:18: note:         ‘virtual void AbstractBase::speak()’
    4 |     virtual void speak() = 0;
      |                  ^~~~~
    
    */


    return 1;
}



