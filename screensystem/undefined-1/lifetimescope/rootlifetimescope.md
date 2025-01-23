# RootLifetimeScope

### Concepts

- The top-level LifetimeScope for a project.
- It lasts from the start of the game to the end.
- The ScreenSystem is also responsible for launching a kind of EntryPoint.

### Implementation policy

- Page containers and modal containers are referenced via SerializeField.
- Register the two referenced containers.
  - `IContainerBuilder` type as an extension method of the ScreenSystem-supported `RegisterPageSystem`and `RegisterModalSystem` methods supported by ScreenSystem.
- Push the first page.
  - Create an EntryPoint class.
    - Implement it using the IStartable interface.
    - Register as a RegisterEntryPoint in the RootLifetimeScope.
    - Inject a PageEventPublisher and send a PageBuilder as a message to push the page.
  - Register other message brokers, network-related dependencies, etc.

```csharp
public class RootLifetimeScope : LifetimeScope
{
    [SerializeField] UnityScreenNavigator.Runtime.Core.Page.PageContainer _container;
    [SerializeField] UnityScreenNavigator.Runtime.Core.Modal.ModalContainer _modalContainer;

    protected override void Configure(IContainerBuilder builder)
    {
        builder.RegisterPageSystem(_container);
        builder.RegisterModalSystem(_modalContainer);
        builder.Register<IHttpClient>(_ => new HttpClient(), Lifetime.Singleton);

        var options = builder.RegisterMessagePipe();
        builder.RegisterMessageBroker<MessagePipeTestMessage>(options);
        builder.RegisterEntryPoint<TestEntryPoint>();
    }

    private class TestEntryPoint : IStartable
    {
        private readonly PageEventPublisher _publisher;

        public TestEntryPoint(PageEventPublisher publisher)
        {
            _publisher = publisher;
        }

        public void Start()
        {
            _publisher.SendPushEvent(new TestPageBuilder());
        }
    }
}
```


