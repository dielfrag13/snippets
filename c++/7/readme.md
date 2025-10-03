# Concepts

* function pointers, lambdas and captures, functors, std::function, `auto`, `operator` and operator overloading .. and initializer lists. SO MANY CONCEPTS. 


# `std::function`
* this is a polymorphic wrapper for 'something callable.' 
* can hold:
  * regular function pointer
  * lambda
  * a functor (which is an object with `operator()`)
* syntax: `std::function<ReturnType(ArgumentTypes...)>`

# lambda
* anonymous (i.e. no name) inline functions.
* syntax: 
```cpp
[captures](params) -> return_type { body }
```

## captures? 
When you define a lambda inside a scope, it can 'capture' variables from that surrounding scope and use them inside the lambda body. The stuff inside the square brackets is the *capture list*. This is the special power of lambdas compared to normal functions -- they can 'close over' local varibles, which is why they're also sometimes called *closures*. 

## capture forms

### capture by value (`=` or `[x]`)
* makes a copy of the variable when the lambda is created. Later changes to the variable won't affect the lambda's instance of the variable. 

```cpp
int a = 10;
auto f = [a]() { std::cout << a << "\n"; }; // captured by value
a = 20;
f(); // prints 10
```

### capture by reference (& or [&x])
* captures the variable by reference. Later changes are visible inside the lambda.
```cpp
int a = 10;
auto f = [&a]() { std::cout << a << "\n"; }; // captured by reference
a = 20;
f(); // prints 20
```


### mix and match
You can do a mix of both:
```cpp
int x = 1, y = 2;
auto f = [x, &y]() { std::cout << x << ", " << y << "\n"; };
x = 10; y = 20;
f(); // prints "1, 20"
```

### Mutable capture
by default, lambdas capturing by value treat variables as `const`. If you want to modify the copy, mark the lambda `mutable`:
```cpp
int a = 10;
auto f = [a]() mutable { a++; std::cout << a << "\n"; };
f(); // prints 11 (but doesn’t change original 'a')
std::cout << a << "\n"; // prints 10
```

### `this`
You can capture `this` and get the current object so you can use members. It is basically a pass by reference.  
```cpp
struct Engine {
    int counter = 0;
    void run() {
        auto f = [this]() { counter++; };
        f();
        std::cout << counter << "\n"; // prints 1
    }
};
```

# functors and `operator`

## what is `operator`?

The special `operator` keyword allows you to do overloading of operators -- +, -, [], (), etc, for your own types.
To overload () is what makes an object callable like a function. That's why it's sometimes called the function-call operator. 

### Example: define a vector adding operator

```cpp
struct Vector {
  int x, y;
  Vector operator+(const Vector& other) const {
    return {x + other.x, y + other.y};
  }
}
```
Even though subtracting is mathmatically equivalent to adding, you must still explicitly overload '-' before subtracting. 
Also, let's talk about this line:
```cpp
  Vector operator+(const Vector& other) const {
```
The first `const` indicates the other side of the operator must be a const vector. It means "i promise not to modify `other` inside this function." Also passes by reference to avoid copying the whole `Vec2` object. 

The trailing `const` means "I promise not to modify the data members of `this` inside this function." It makes the function a *const member function*. Without the ocnst, you woulnd't be able to call `operator+` on a `const Vec2`. 

```cpp
const Vec2 a{1,2};
Vec2 b{3,4};
auto c = a + b;   // ✅ works because operator+ is const
```
If operator+ weren't `const`, this would fail, because `a` is const and you can't call non-const member functions on a const object. 

Use trailing const when your method does not modify the object. It's common for getter functions, and operators like `+`, `==`, `*`, etc. But don't use it if the function logically changes the object (think `push_back`, `set_name`, etc.)



## tieback to functors

Functors are just structs where the `()` operator is overloaded:
```cpp
struct Multiplier {
    int factor;

    Multiplier(int f) : factor(f) {}

    // overloading the (), enabling functor state
    int operator()(int x) const {
        return x * factor;
    }
};

Multiplier tripler(3);
std::cout << tripler(10); // prints 30
```
Unlike raw functions, functors can actually hold state. `tripler` remembers the multiplier factor -- 3. So it's almost like you can 'load' a function with a value at runtime. Very cool!

### initialization lists

Also, let's talk about this line:

```cpp
    Multiplier(int f) : factor(f) {}
```
This introduces 'initialization lists'. It is a constructor definition for `Multiplier`. The `: factor(f)` part is the *member initializer list*. It initializes the data member `factor` with the value of the parameter `f`. it is not a function call!

You could easily have done this too:
```cpp
struct Foo {
    int x;
    Foo(int val) { x = val; } // assigns x after it’s default-constructed
};
```
So why use initializer lists? For built-in types like `int` it doesn't matter much. But for class members like `std::string`, `std::vector`, etc, initializer lists are better because the construct the object once with the right value, instead of constructing a default object and then reassigning. Efficiency! 

Also, sometimes, you cannot do constructor body assignment, such as for const members:

```cpp
struct Foo {
    const int x;

    // ❌ ERROR: assignment not allowed for const
    //Foo(int val) {
    //    x = val;   // invalid
    //}

    // ✅ OK: initialized in member initializer list
    Foo(int val) : x(val) {}
};

```
or references:
```cpp
struct Bar {
    int& ref;

    // ❌ ERROR: reference must be initialized
    //Bar(int& r) {
    //    ref = r;   // invalid
    //}

    // ✅ OK
    Bar(int& r) : ref(r) {}
};
```
One more example, but this time, just demonstrate how to do it with more complex objects:
```cpp
struct Baz {
    std::string s;
    int i;

    // ❌ This constructs an empty string first, then assigns -- inefficient!
    Baz(const std::string& str, int i) {
        s = str;
        i = i;
    }

    // ✅ This constructs directly with the given value
    Baz(const std::string& str, int i) : s(str), i(i) {}
};
```





## Make it, run it
```bash
kbuchmil@TAMARIND:~/git/snippets/c++/7$ g++ -g -Wall example.cpp -o example
kbuchmil@TAMARIND:~/git/snippets/c++/7$ ./example
free_function: 10
lambda: 20
captures lambda x and y: 420, 69
adding 1 to outer scope copy, which shall change?
captures lambda x and y: 420, 70
incrementer counter: 1
incrementer counter: 2
inc counter: 2
Vec2 a{1,2} + b{3,4}: 4, 6
tripler ran with 5: 15
quadrupler ran with 10: 40
doubler with one additonal ran with 8: 17
```

