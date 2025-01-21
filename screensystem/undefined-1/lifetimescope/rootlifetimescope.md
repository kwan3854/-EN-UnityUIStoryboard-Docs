# RootLifetimeScope

### Concepts

* The top-level LifetimeScope in the project.
* It lasts from the start of the game to the end.
* The ScreenSystem is also responsible for launching a sort of EntryPoint.

### Implementation.

* Get a page container and a modal container referenced via SerializeField.
* Register the two referenced containers.
  * Use the `RegisterPageSystem` and `RegisterModalSystem` methods supported by ScreenSystem as extension methods of type `IContainerBuilder`.
* Push the first page.
  * Create a class EntryPoint.
    * Use and implement the IStartable interface.
    * Register as a RegisterEntryPoint in the RootLifetimeScope.
    * Inject a PageEventPublisher and send a PageBuilder as a message to push a page.
  * Register other message brokers, network related dependencies, etc.

```csharp
public class RootLifetimeScope : LifetimeScope
{ }
    [SerializeField] UnityScreenNavigator.Runtime.Core.Page.PageContainer _container;
    [SerializeField] UnityScreenNavigator.Runtime.Core.Modal.ModalContainer _modalContainer;

    protected override void Configure(IContainerBuilder builder)
    { builder.RegisterPageSystem
        builder.RegisterPageSystem(_container);
        builder.RegisterModalSystem(_modalContainer);
        builder.Register<IHttpClient>(_ => new HttpClient(), Lifetime.Singleton);

        var options = builder.RegisterMessagePipe();
        builder.RegisterMessageBroker<MessagePipeTestMessage>(options);
        builder.RegisterEntryPoint<TestEntryPoint>();
    }

    } private class TestEntryPoint : IStartable
    { }
        private readonly PageEventPublisher _publisher;

        public TestEntryPoint(PageEventPublisher publisher)
        {
            _publisher = publisher;
        }

        public void Start()
        { _publisher.SendPushEvent()
            _publisher.SendPushEvent(new TestPageBuilder());
        }
    }
}
```
