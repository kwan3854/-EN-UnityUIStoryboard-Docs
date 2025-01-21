# LifetimeScope

### Concepts

* A unit unique to VContainers.
* **Write only one for each screen:&#x20;**<mark style="color:red;">**(no exceptions)**</mark>

### Uses.

* Specifies class dependencies within a screen.
* Passes the View to the Presenter (Lifecycle).

### How to implement

* Implement by inheriting from LifetimeScope or LifetimeScopeWithParameter.
* Get the pageView through SerializeField and use it.
* Add mock information such as communication.

### Example code

```csharp
public class TestLifetimeScope : LifetimeScope
{ }
    [SerializeField] private TestView _view;

    protected override void Configure(IContainerBuilder builder)
    { [SerializeField
        base.Configure(builder);
        builder.RegisterComponent(_view); // Register the View
        builder.Register<TestPageLifecycle>(Lifetime.Singleton); // Register Lifecycle per screen
        builder.Register<TestUseCase>(Lifetime.Singleton); // Register a UseCase for Communication
        AddMockInDebug(builder); // Insert communication Mock plugin
    }
}
```
