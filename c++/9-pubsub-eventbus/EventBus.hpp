#pragma once
#include "Event.hpp"

#include <cstdint>
#include <functional>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

namespace eng {

class EventBus {
    public:
    
    using Handler = std::function<void(const Event&)>;
    using HandlerId = std::uint64_t;

    // Subscribe to a topic. Returns an id you can use to unsubscribe. 
    HandlerId subscribe(const std::string& topic, Handler handler);

    // Unsubscribe -- returns true if a handler was removed.
    bool unsubscribe(const std::string& topic, HandlerId id);

    // publish an event for all handlers of a topic.
    void publish(const Event& ev) const;


private:
    // dict of str -> [(HandlerId, Handler), ...]
    std::unordered_map<std::string,
        std::vector<std::pair<HandlerId, Handler>>> handlers_;
    
    // will hold the id of the 'next' subscription. We need that to uniquely identify each subscription. 
    // we change next_id_ by one in the cpp subscribe() method. 
    // this is the 'c++'-y way of assigning the variable to 1, at initialization. Good for vectors & non-trivial objects. 
    HandlerId next_id_{1};
};



}
