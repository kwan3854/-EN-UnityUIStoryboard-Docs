# Write mockup code

In fact, we've already written some sort of mockup code.

It's called, [gateway.md](../ui/gateway.md "mention") code, but for the sake of simplicity, I didn't write any code to connect to the actual server, I simply wrote code that delays a few seconds and returns a value.

In this way, we choose the layer we want to mock based on what we intend to mock, write a mock class that implements the same interface as the part that will be the actual implementation, and inject the mock class into the DI container to use it.


