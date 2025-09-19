#include <iostream>
#include <memory>       // for smart pointers

/*
 * 5: basic pointer and reference stuff
 */
void ref_increment(int &x) {
    x++;
}
void ptr_increment(int *x) {
    (*x)++;
}

/*
 * 6: smart pointer stuff
 */
struct Foo {
    Foo() { std::cout << "Foo created\n"; }
    ~Foo() { std::cout << "Foo destroyed\n"; }
};
struct Bar {
    Bar() { std::cout << "Bar created\n"; }
    ~Bar() { std::cout << "Bar destroyed\n"; }
};
int main(void) {

    // conventional way
    int x = 0;
    int &x_ref = x;
    int *x_ptr = &x;

    // 5: basic pointer/reference stuff
    std::cout << x << std::endl;    // prints 0
    ref_increment(x_ref);
    std::cout << x << std::endl;    // prints 1
    ptr_increment(x_ptr);
    std::cout << x << std::endl;    // prints 2

    // 6: smart pointers!
    std::unique_ptr<Foo> u1 = std::make_unique<Foo>();
    // std::unique_ptr<Foo> p2 = p1;    // compilation error: "use of deleted function"

    std::shared_ptr<Bar> s1 = std::make_shared<Bar>();

    // quick aside: putting these in brackets defines a new scope
    // essentially, when the bracket ends, the scope does too and variables within are deleted. 
    {
        std::shared_ptr<Bar> s2 = s1; // both share ownership
        std::cout << "use count = " << s1.use_count() << "\n"; // prints 2
    } // p2 destroyed, count back to 1
    // Bar destroyed when p1 also goes out of scope
    return 1;
}
