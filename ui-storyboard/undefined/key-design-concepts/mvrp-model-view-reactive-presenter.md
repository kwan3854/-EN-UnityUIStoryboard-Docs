# MVRP method (Model-View-Reactive Presenter)

- Presenter, View are bound to the existing MVP pattern in a reactive way (using UniTask, R3).

- Presenter is referred to as "Lifecycle" in this document.

- Between the View/UI and the business logic (UseCase), Presenter mediates all behavior.

- Presenter (or Lifecycle) ultimately calls UseCase, which in turn calls Repository and Gateway to handle external communication/DB/caching, etc.
