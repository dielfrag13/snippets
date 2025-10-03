#include <iostream>

// for std::function
#include <functional>

// just a function
void free_function(int x) {
    std::cout << "free_function: " << x << "\n";
}

// struct thing with lambda capturing 'this'
struct incrementer {
    int counter = 0;
    void run() {
        auto f = [this]() {counter++;};
        f();
        std::cout << "incrementer counter: " << counter << "\n";
    }

};


struct Vec2 {
    int x, y;
    Vec2 operator+(const Vec2 &other) const {
        return {x + other.x, y + other.y};
    }
};


// struct demonstrating functor, operator () overloading, initialization lists
struct Multiplier {
    int factor;
    int additional;
    // constructor -- introducing "initializer lists" -- the other way of initializing members of a struct/class!

    Multiplier(int f) : factor(f), additional(0) {}
    Multiplier(int f, int additional)
     : factor(f), 
       additional(additional) 
    {}

    // overload the () operator to enable functor-ness
    int operator()(int x) const {
        return (x * factor) + additional;
    }

    
};

// equivalent to this lambda:

int main(void) {

    // function pointers
    std::function<void(int)> func;
    func = free_function; 
    func(10);

    // lambda basic syntax
    func = [](int x){std::cout << "lambda: " << x << std::endl; }; // store lambda
    func(20);


    // demonstration of capture by value and capture by reference
    int x = 420;
    int y = 69;
    // x is copied for the scope of the lambda, but y is referenced
    auto func2 = [x, &y]() {std::cout << "captures lambda x and y: " << x << ", " << y << "\n";};
    func2();
    std::cout << "adding 1 to outer scope copy, which shall change?\n";
    x++;
    y++;
    func2();

    // demonstration of using 'this' -- see incrementer
    incrementer inc;
    inc.run();
    inc.run();
    std::cout << "inc counter: " << inc.counter << "\n";
    

    // demonstrating vec2 addition overloading
    Vec2 a{1,2}, b{3,4};
    Vec2 c = a + b;
    std::cout << "Vec2 a{1,2} + b{3,4}: " << c.x << ", " << c.y << "\n";

    Multiplier tripler(3);
    Multiplier quadrupler(4);
    Multiplier doubler_with_one_additional(2, 1);
    std::cout << "tripler ran with 5: " << tripler(5) << "\n";
    std::cout << "quadrupler ran with 10: " << quadrupler(10) << "\n";
    std::cout << "doubler with one additonal ran with 8: " << doubler_with_one_additional(8) << "\n";

    return 0;
}