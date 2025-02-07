# The power of mockup code

### When do I use mockup code?

For small, simple, low-complexity projects, the usefulness of injectable architectures may not be apparent by writing mockup code. But as you grow in size, complexity increases, and more people work together, the true value of these structures becomes apparent.

With mockup code, you can do the following

- Prototyping
- Independent testing

### Assumptions

Let's assume the following situation You have a project that is already somewhat functional. You want to test the direction of your plans for an additional feature. This feature requires communication with the server, but you don't want to waste any resources by working on the server, since you're just checking the direction of your plans. At the same time, you don't want to force fully hard-coded code into a project that's already working well, even if it's prototyping.

#### We have already designed a well-separated structure.

- We've separated the domain logic part from the external logic based on an onion architecture
- Loosely connected to each other by interfaces.
- Dependencies are managed through DI containers.

So, on the client side, you can simply replace the layers where data comes from the server with mockup classes, implement the logic considering only the domain logic, and then later on, when the plan is finalized and you have real data coming from the server, you can implement the actual layers to connect with the server and replace them.

This approach can also facilitate debugging and testing of complex and deep UIs.

Let's say you're developing a screen that requires you to sequentially enter a total of 10 depths, starting with the login screen. How terrible would it be if the data required for the behavior of that screen had dependencies from the previous screens, and you had to test all 10 screens in sequence each time before you could proceed?

This is where mocking comes in, allowing us to break out the dependencies and test only the screen we are developing by running it individually.


