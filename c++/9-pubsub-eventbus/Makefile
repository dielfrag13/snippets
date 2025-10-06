# compiler and flags
CXX = g++
CXXFLAGS = -Wall -std=c++17

# target exe
TARGET = pubsub_bus

# object files
OBJS = EventBus.o main.o

# default rule
$(TARGET):$(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp %.hpp
	$(CXX) $(CXXFLAGS) -c $<

clean:
	rm -rf $(TARGET) $(OBJS)