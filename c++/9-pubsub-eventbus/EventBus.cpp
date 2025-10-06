#include "EventBus.hpp"

namespace eng {

EventBus::HandlerId EventBus::subscribe(const std::string& topic, Handler handler) {

    // get the id and increment the Bus's next id
    const HandlerId id = next_id_++;
    handlers_[topic].emplace_back(id, std::move(handler));   // emplace_back constructs the element directly in allocated memory
    return id;
}

bool EventBus::unsubscribe(const std::string& topic, HandlerId id) {

    // "it": iterator
    // so this gets a 'reference' to the found pair in the handler_ vector
    auto it = handlers_.find(topic);
    // if no handler was found, skip outta town
    if (it == handlers_.end()) return false;

    // so 'it' points to an individual entry in the unordered map now -- a key/value pair.
    // 'second' gets the value -- a vector. 
    auto& vec = it->second;

    // and what do we do with that now? remove the (single) element with the supplied HandlerId. 
    for (auto vit = vec.begin(); vit != vec.end(); ++vit) {
        // vit -- vector iterator
        if (vit->first == id) {
            vec.erase(vit);     // this invalidates vit, so we can't use it in the loop anymore anyway
            return true;        // so return
        }
    }
    // if no entry was found with the supplied id, return false. 
    return false;

}


void EventBus::publish(const Event& ev) const {

    // gotta identify all things to publish to 
    // remember this returns a key-value pair. 
    // only one list of handler id's and handlers per type.
    auto it = handlers_.find(ev.type);

    // means no subscribers were found
    if (it == handlers_.end()) return;

    // `it->second` gets the vector that we want to run through. 
    // `pair` refers to each individual element of that vector. 
    for (auto& pair : it->second) {
        pair.second(ev); // call the stored handler function, with the event as a parameter. 
    }


}

} // end namespace eng 