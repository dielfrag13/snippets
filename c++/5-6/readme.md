# concepts

* pointers, references, smart pointers, a scope trick (putting things in brackets within functions)


## references vs pointers

* Pointers (*) can be null. References (&) are always valid. 
* use these when passing around polymorphic types. Copying those by value is bad news bears. 

# smart pointers

* these require `#include <memory>`

### why smart pointers?
In C, you'd `malloc`/`free`. In C++, you'd `new`/`delete`. Both are error-prone:
* forgot to `delete` -> memory leak
* `delete` twice -> undefined behavior
* early return/exceptions -> leaks. 

Smart pointers solve each of these things by applying RAII (that is, Resource Acquisition Is Initialization): _owning memory is tied to the lifetime of an object_. 


## `std::unique_ptr`

* represents sole ownership of a resource.
* When the `unique_ptr` goes out of scope, it automatically `delete`s the resource. 
* It cannot be copied (i.e. ownership is unique). You can only *move* it. 
* created with the `make_unique` function: `std::make_unique<Type>()`

* Benefits:

* * no manual delete.
* * Expresses intent: "this object has exactly one owner."
* * lightweight. 


## `std::shared_ptr`

* represents shared ownership of a resource.
* reference-counted -- every copy increments the count; when the last one goes away, resource is deleted.
* heavier weight than `unique_ptr`


### quick aside on scope brackets

You can define an 'inner scope' in your methods/functions, and things defined in that inner scope go away after the scope ends. 
```cpp
#include <iostream>

struct Foo {
    Foo()  { std::cout << "Foo constructed\n"; }
    ~Foo() { std::cout << "Foo destroyed\n"; }
};

int main() {
    {
        Foo f;  // constructed here
        std::cout << "Inside inner scope\n";
    }          // inner scope ends → f is destroyed here

    std::cout << "Back in main scope\n";
}
```
would output:
```
Foo constructed
Inside inner scope
Foo destroyed
Back in main scope
```

## Make it, run it
```sh
kbuchmil@TAMARIND:~/git/snippets/c++/5-6$ g++ -g -Wall example.cpp -o example
kbuchmil@TAMARIND:~/git/snippets/c++/5-6$ ./example
0
1
2
Foo created
Bar created
use count = 2
Bar destroyed
Foo destroyed
```


