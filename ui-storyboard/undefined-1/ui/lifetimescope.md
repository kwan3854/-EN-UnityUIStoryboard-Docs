# LifetimeScope

```csharp
public class SignInModalLifetimeScope : VContainer.Unity.LifetimeScope
{
    [SerializeField] private SignInModalView view;

    protected override void Configure(IContainerBuilder builder)
    {
        base.Configure(builder);
    
        builder.RegisterComponent(view);
        builder.Register<SignInModalLifecycle>(Lifetime.Singleton);
        // builder.Register<SignInUseCase>(Lifetime.Singleton).AsImplementedInterfaces();
        builder.Register<MockSignInUseCase>(Lifetime.Singleton).AsImplementedInterfaces();
    }
}
```

- `RegisterComponent` as a view
- Lifecycle enrollment
- UseCase Registration


