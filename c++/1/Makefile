# Makefile is just a set of rules:
# target:dependencies followed by a 'recipe' (commands)

# compiler & flags
CXX = g++
CXXFLAGS = -Wall -std=c++17

# target executable
TARGET = foo

# Object files
OBJS = foo.o main.o

# default rule
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)


# compile .cpp into .o
# these are called 'pattern rules'
%.o: %.cpp %.hpp
	$(CXX) $(CXXFLAGS) -c $<


# clean build artifacts

clean:
	rm -rf $(TARGET) $(OBJS)
