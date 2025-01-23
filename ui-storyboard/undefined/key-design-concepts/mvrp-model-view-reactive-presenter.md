# MVRP method (Model-View-Reactive Presenter)

\- Presenter, View are bound to an existing MVP pattern in a reactive way (using UniTask, R3).

\- Presenter is referred to as "Lifecycle" in this document.

\- Between the View/UI and the business logic (UseCase), Presenter mediates all behavior.

\- The Presenter (or Lifecycle) ultimately calls the UseCase, which in turn calls the Repository and Gateway to handle external communication/DB/caching, etc.


