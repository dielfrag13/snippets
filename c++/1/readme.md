# concepts

* Basic class syntax between headers, implementation
* Basic compiltion demonstration
* Constructors, methods, destructors
* Constructor delegation: when one constructor for a class calls another with a different number of parameters

## building
build with a 'make' call.

```sh
make
```
and clean with:
```sh
make clean
```

Output as written:

```sh
kbuchmil@TAMARIND:~/git/snippets/c++/1$ ./foo
setting lol_ to 0...
Hello from no-arg constructor!
but added one lol
method 1: haha
method 1: haha2
setting lol_ to 25...
method 1: haha
method 1: haha2
destruction. lol_ count: 27
destruction. lol_ count: 3
```