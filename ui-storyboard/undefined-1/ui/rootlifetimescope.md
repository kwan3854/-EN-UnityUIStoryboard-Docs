# RootLifetimeScope

* 프로젝트 최상단 씬에 최상단 게임오브젝트에 붙여둔다.
* 아래는 예시코드이며, RootLifetimeScope에는 게임 진행 내내 수명이 유지되어야 하는 것들을 등록하는게 주 목적이며, 첫 UI 페이지를 시작시키는 EntryPoint 를 발동시키는 역할도 함.

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
