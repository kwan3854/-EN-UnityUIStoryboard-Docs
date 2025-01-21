# Onion Architecture

* A more "practical" variant of the typical Clean Architecture for real-world projects.
* Layering the **Inner Layer** (Domain, UseCase) and **Outer Layer** (Repository, Gateway), so that the business logic (UseCase/Domain) is not dependent on external dependencies (Network, DB, etc.).
* &#x20;The connection between each layer is only through interfaces (except MVP), and all implementations are injected with **Dependency Injection (VContainer)**&#xB85C;.
