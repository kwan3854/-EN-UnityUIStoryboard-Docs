# LifetimeScope



```csharp
public class SignInModalLifetimeScope : VContainer.Unity.LifetimeScope
{ }
    [SerializeField] private SignInModalView view;

    protected override void Configure(IContainerBuilder builder)
    { [SerializeField] private SignInModalView view
        base.Configure(builder);
    
        builder.RegisterComponent(view);
        builder.Register<SignInModalLifecycle>(Lifetime.Singleton);
        // builder.Register<SignInUseCase>(Lifetime.Singleton).AsImplementedInterfaces();
        // builder.Register<MockSignInUseCase>(Lifetime.Singleton).AsImplementedInterfaces();
    }
}
```

* Register a view with `RegisterComponent`.
* Register Lifecycle
* Register UseCase
