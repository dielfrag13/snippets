#include <iostream>

class Base {
    public:
    Base() {
        std::cout << "Base constructed\n";
    }

    void set_private_id(int id) {
        std::cout << "Base setting id to " << id << "!\n";
        private_id=id;
    }

    int get_private_id() {
        return private_id;
    }

    virtual ~Base() {
        std::cout << "base deconstructing id " << private_id << "!\n";
    }

    // private members can't be accessed in derived classes
    private:
    int private_id;
    // protected members can be 
    protected:
    int protected_id; 
};



// you specify the access of the inherited classes here too. default is private:
//class Derived : Base {
// is the same as:
//class Derived : private Base {

class Derived : public Base {
    public:
    Derived() {
        std::cout << "Derived constructed\n";
    }

    ~Derived() override {
        std::cout << "derived deconstructing id " << get_private_id() << "!\n";
    }
};

int main(void) {

    Derived d;
    Derived &d1 = d;
    d1.set_private_id(1); 
    Derived *d2 = new Derived();
    d2->set_private_id(2);
    delete d2;

    return 1;
}



