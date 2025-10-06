#pragma once
#include <any> // available for c++ std 17 and above
#include <string>

namespace eng {

struct Event {
    std::string type;
    std::any data;
};

} // namespace eng