# Onion Architecture

- Let's take a typical Clean Architecture and make it more ** more "practical" for real-world**for real-world projects.
- **Inner layers**(Domain, UseCase) and **outer layer**(Repository, Gateway), so that the business logic (UseCase/Domain) is not dependent on external dependencies (network, DB, etc.).
-  Connections between each layer are only made via interfaces (except for MVPs), and all implementations use the **Dependency Injection (VContainer)**for all implementations.


