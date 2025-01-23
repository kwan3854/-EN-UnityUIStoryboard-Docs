# RootLifetimeScope

- Attach it to the top-level GameObject in the top-level scene of your project.
- Below is example code, the main purpose of the RootLifetimeScope is to register things that should have a lifetime throughout the game, and it is also responsible for triggering the EntryPoint that launches the first UI page.

```csharp
public class ProjectRootLifetimeScope : VContainer.Unity.LifetimeScope
{
    [SerializeField] private PageContainer pageContainer;
    [SerializeField] private ModalContainer modalContainer;

    protected override void Configure(IContainerBuilder builder)
    {
        // ScreenSystem
        builder.RegisterPageSystem(pageContainer);
        builder.RegisterModalSystem(modalContainer);
    
        // MessagePipe
        var options = builder.RegisterMessagePipe();
        builder.RegisterMessageBroker<MessagePipeOptions>(options);
        
        RegisterGateways(builder);
        RegisterRepositories(builder);
        RegisterUseCases(builder);
        
        builder.RegisterEntryPoint<SampleEntryPoint>();
    }

    private void RegisterUseCases(IContainerBuilder builder)
    {
        builder.Register<SignInUseCase>(Lifetime.Scoped).AsImplementedInterfaces();
    }

    private void RegisterRepositories(IContainerBuilder builder)
    {
        builder.Register<AccountRepository>(Lifetime.Scoped).AsImplementedInterfaces();
    }

    private void RegisterGateways(IContainerBuilder builder)
    {
        builder.Register<HttpClientGateway>(Lifetime.Singleton).AsImplementedInterfaces();
    }

    // ReSharper disable once ClassNeverInstantiated.Local
    private class SampleEntryPoint : IStartable
    {
        private readonly PageEventPublisher _pageEventPublisher;
    
        public SampleEntryPoint(PageEventPublisher pageEventPublisher)
        {
            _pageEventPublisher = pageEventPublisher;
        }

        public void Start()
        {
            _pageEventPublisher.SendPushEvent(new SignInPageBuilder(false, false));
        }
    }
}
```


