# Model, View, Presenter (Lifecycle)

## Development Units

- The default unit is 1 Presenter, 1 View, and 1 ViewModel per Page/Modal.
- Depending on the complexity, you can configure multiple ViewModels or Views, but it is recommended that they are ultimately "merged" into a single View.
- In a real MVP, the Model role is played by a Repository, which may be shared and used in multiple places. (See Onion Architecture) 

## About using the interface

{% hint style="success" %}
For more information, see the [mvp.md](mvp.md "mention") Note
{% endhint %}

- MVPs are based on direct implementation without using interfaces.
- However, only in limited cases where we find repetitive usage more than 2-3 times throughout the project, we will discuss and extract it into an interface.

## The actual logic is

- Presenter must perform logic through UseCase, and UseCase handles external communication (servers, DBs, etc.) through Repository.
- Repository, in turn, is responsible for the actual communication via Gateway.
- At the UseCase level, you don't need to worry about communication conventions, protocols, etc.
- Gateway is developed according to the actual communication protocol API, etc.
- Repository is developed last, as an intermediary between UseCase and Gateway.


