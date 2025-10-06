#include "Event.hpp"
#include "EventBus.hpp"
#include <any>
#include <chrono>
#include <iostream>
#include <string>

using namespace eng;


// demo data payloads for events. 
struct Tick { std::string symbol; double last; };
struct Log { std::string msg; };


int main(void) {

    EventBus bus;

    int tick_count = 0;
    const double alert_under = 95.0;

    // let's make some lambdas just to demonstrate things

    // this sub will just print some logs. Won't ever unsubscribe it. 
    bus.subscribe("log", [](const Event& ev) {
        const auto& log = std::any_cast<const Log&>(ev.data);
        std::cout << "[log] " << log.msg << "\n";

    });
    

    // this sub just increments the tick count
    auto subscriber_1 = bus.subscribe("tick", [&](const Event& ev) {
        const auto& t = std::any_cast<const Tick&>(ev.data);
        ++tick_count;
        std::cout << "[tick #" << tick_count << "] " << t.symbol << "=" << t.last << "\n";
    });

    // this sub actually alerts for things
    auto subscriber_2 = bus.subscribe("tick", [=](const Event& ev) {
        const auto& t = std::any_cast<const Tick&>(ev.data);
        if (t.last < alert_under) {
            std::cout << "[ALERT] " << t.symbol << " under " << alert_under << ": " << t.last << "\n";
        }

    });


    // let's publish some events
    bus.publish(Event{"log", Log{"starting..."}});
    bus.publish(Event{"tick", {Tick{"BTC", 96.0}}});
    bus.publish(Event{"tick", {Tick{"SPY", 98.0}}});
    bus.publish(Event{"tick", {Tick{"SPY", 94.0}}});
    bus.publish(Event{"tick", {Tick{"BTC", 125000.0}}});

    bus.unsubscribe("tick", subscriber_2);
    bus.publish(Event{"log", Log{"unsubscribed the alerter."}});
    bus.publish(Event{"tick", {Tick{"SPY", 105.0}}}); // notice how only subscriber_2 received this
    bus.publish(Event{"tick", {Tick{"SPY", 65.0}}}); // notice how only subscriber_2 received this
    bus.publish(Event{"log", Log{"ending."}});

    return 1;
}