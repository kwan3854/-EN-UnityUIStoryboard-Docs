# Dependencies

### ScreenSystem has <mark style="color:red;">dependencies on the following libraries.

* VContainer
  * DI Framework to manage dependencies of classes and objects.
* UnityScreenNavigator
  * Performs screen transitions by splitting and switching screens into pages and modules.
* UniTask
  * OSS for easy handling of tasks, widely used for communication, screen transitions, etc.

### <mark style="color:green;">Recommended</mark> for use with the following libraries.

* UniRx
  * Mainly used to notify Presenter of events in the View and to implement MVP (MVRP).
* MessagePipe
  * A messaging library, used when you want to deliver updates to other screens that exist at the same time.
