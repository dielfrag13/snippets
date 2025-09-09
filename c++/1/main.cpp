#include "foo.hpp"
#include <string>

int main() {

    // no namespace?
    Foo foo_object; // calls no-arg constructor

    // no-arg constructor adds 1 to default of 0
    std::string s = "haha";
    std::string s2 = "haha2";
    foo_object.method_1(s); // increments lol_ by 1
    foo_object.method_1(s2);// increments lol_ by 1
    // final tally for object is 3
    
    // foo_object.lol_ is 3
    Foo foo_object2(25);
    foo_object2.method_1(s); // increments lol_ by 1
    foo_object2.method_1(s2); // increments lol_ by 1
    // final tally for object2 is 27
    return 0;


}