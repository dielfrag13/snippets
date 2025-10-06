# concepts

* Pub/Sub Event Bus model
* `using` keyword
* various supporting std namespace data types and functions
* touches on iterators


# 10,000 foot overview of pub/sub event bus model

You have the concepts of Events. Events have a type (represented by string), and associated data (think 'log' and a log message, or 'priceUpdate' and a dollar amount). 

You have an EventBus. The EventBus has a `handlers` dictionary/unordered_map element that contains a mapping of types (log, priceUpdate, etc) each to a vector of things that care -- the subscribers.

```
EventBus 
 | 
 |-- 'log' -> [list of things that care about log messages]
 |-- 'priceUpdateSpy' -> [list of things that care about SPY price updates]
 |-- 'priceUpdateBTC' -> [list of things that care about BTC price updates]
 ...
 |
```

The things that care -- the handlers -- is a collection of supplied functions that are called upon the receival of a message. Each are called with that event message. 

The bus 'publishes' the event by calling every handler's handle function with that event. 
The bus has helper functions to enable subscriptions -- i.e. getting your handler into the list of things that'll be called when the bus identifies a message of the type you care about. 


## using

It is advised to be cautious with `using` because it can lead to name collisions and ambiguity, especially in large projects. But it provides some conveniences.

You can define a namespace, and then you don't have to prefix elements (like std::string) with the prefix:

### namespace utilization
```cpp
#include <iostream>

namespace MyNamespace {
    void greet() {
        std::cout << "Hello from MyNamespace!" << std::endl;
    }
}

int main() {
    using namespace MyNamespace; // Bring MyNamespace members into scope
    greet(); // Call greet() without MyNamespace:: prefix
    return 0;
}
```

### using declaration (for specific members)

```cpp
#include <iostream>
#include <string>

int main() {
    using std::cout; // Bring only std::cout into scope
    using std::string; // Bring only std::string into scope

    string message = "Specific members imported!";
    cout << message << std::endl;
    return 0;
}
```

### type aliases -- replacing `typedef`:
```cpp
// Using typedef (older style)
typedef std::vector<int> IntVector;

// Using using (modern C++)
using IntVector = std::vector<int>;

// With templates
template <typename T>
using MySmartPointer = std::unique_ptr<T>;

int main() {
    IntVector myVec;
    myVec.push_back(10);

    MySmartPointer<double> ptr = std::make_unique<double>(3.14);
    return 0;
}
```

### inheriting base class members
```cpp
class Base {
public:
    void print(int x) { /* ... */ }
    void print(double d) { /* ... */ }
};

class Derived : public Base {
public:
    using Base::print; // Bring all overloaded print functions from Base
    void print(std::string s) { /* ... */ }
};
```

## Iterators
A generalization of pointers that allow a c++ program to work with different data structures in a uniform manner. They are pointers, so you use arrow syntax to dereference them and get their contents. 

Also, don't forget that you don't use arrow with references becuase references behave like the objects they refer to. 

Think of iterators as a lightweight object that points *into* a container (like a pointer, but container-aware). You can:
* move it forward (e.g. ++it)
* dereference it to get th eelement it points to (e.g. *it)
* compare it to another iterator (e.g. `it == container.end()`)

Different containers expose different iterator operations (random-access for `vector`, bidirectional for `list`, etc) but the common pattern is:

```cpp
for (auto it = c.begin(); it != c.end(); ++it) {
    /* use *it */
}
```
Or you can use c++ range-for loops that hide the iterator:
```cpp
for (auto& elem : c) { /* use elem */ }
```
You typically use the c++ range-for loop when you just need to read or write elements. You use explicit iterators when you need:
* the position (e.g. to call erase(vit))
* to iterate over a sub-range
* to interleave iteration with container-modifying operations that require iterators

# std::thing glossary

## std::vector
* basically just dynamically sized arrays (python list equivalent)

### std::emplace_back
Constructs the object directly in allocated space at the end of the vector (instead of constructing it somewhere then copying it)

### std::find 
Takes a key and tries to locate the element with which the key matches. If successful the function returns an iterator pointing to the sought after element. If unsuccessful it returns the past-the-end ( end() ) iterator.

## std::move
Used to indicate an object `t` may be 'moved from', i.e. allowing the efficient transfer of resources from `t` to another object. 

## std::any
A type in c++17 and above that can be, well, any. Its type is deduced based on the first thing assigned to it. 

### std::any_cast
A function used to safely extract the value stored within a `std::any` object. It ensures that the type you are attempting to extract matches the exact type stored in the `std::any` object. Google's AI illustrates:

```cpp
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any a;

    // Store an int
    a = 10;
    try {
        int i = std::any_cast<int>(a); // Extract by value
        std::cout << "Stored int: " << i << std::endl;
    } catch (const std::bad_any_cast& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    // Attempt to cast to a different type (will throw)
    try {
        std::string s = std::any_cast<std::string>(a);
    } catch (const std::bad_any_cast& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    // Store a string
    a = std::string("hello");
    if (std::string* s_ptr = std::any_cast<std::string>(&a)) { // Extract by pointer
        *s_ptr += " world";
        std::cout << "Modified string: " << *s_ptr << std::endl;
    } else {
        std::cout << "Failed to get string pointer." << std::endl;
    }

    return 0;
}
```
## Are you asking "well what differentiates `std::any` and `auto`"?
Auto is a keyword used for deduction at compile time. When you declarte a variable with auto, the compiler infers its type based on the initializer. It cannot change during runtime. It does not require runtime type checking, as it cannot change and the compiler will always be able to deduce when something would or might go wrong. 

`std::any` is a type-erased container that can hold a value of any copyable type. It allows storing objects of different types in the same `std::any` object, and the type can change at runtime. It requires the use of `std::any_cast` to do runtime type checking safety, which can throw exceptions if casts are invalid. 

```cpp
    std::any a;
    a = 10; // a now holds an int
    a = std::string("hello"); // a now holds a std::string
    // int val = std::any_cast<int>(a); // Throws bad_any_cast exception
    std::string str_val = std::any_cast<std::string>(a); // OK
```




# make it, run it

```bash
kbuchmil@TAMARIND:~/git/snippets/c++/9-pubsub-eventbus$ make
g++ -Wall -std=c++17 -c EventBus.cpp
g++ -Wall -std=c++17   -c -o main.o main.cpp
main.cpp: In function ‘int main()’:
main.cpp:34:10: warning: unused variable ‘subscriber_1’ [-Wunused-variable]
   34 |     auto subscriber_1 = bus.subscribe("tick", [&](const Event& ev) {
      |          ^~~~~~~~~~~~
g++ -Wall -std=c++17 -o pubsub_bus EventBus.o main.o
kbuchmil@TAMARIND:~/git/snippets/c++/9-pubsub-eventbus$ ./pubsub_bus
[log] starting...
[tick #1] BTC=96
[tick #2] SPY=98
[tick #3] SPY=94
[ALERT] SPY under 95: 94
[tick #4] BTC=125000
[log] unsubscribed the alerter.
[tick #5] SPY=105
[tick #6] SPY=65
[log] ending.
```