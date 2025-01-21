# Model, View, Presenter (Lifecycle) set

## Development Units

* 1 Model, 1 Presenter, 1 View per Page/Modal is the default unit.
* Depending on the complexity, you can configure multiple Models or Views, but it is recommended to "merge" them into a single Model, single View in the end.

## About using the interface

{% hint style="success" %}
See [mvp.md](mvp.md "mention") for more information.
{% endhint %}

* The MVP is intended to be a straightforward implementation without using interfaces.
* However, only in limited cases where we find a repetitive use more than 2-3 times throughout the project, we will discuss and extract it into an interface.

## The actual logic is

* Presenter must perform logic via UseCase, which in turn handles external communication (servers, DB, etc.) via Repository.
* Repository in turn is responsible for the actual communication via Gateway.
* Developers don't need to worry about communication conventions, protocols, etc. at the UseCase level.
* Gateway is developed according to the actual communication protocol API, etc.
* Repository is developed last, as an intermediary between UseCase and Gateway.
