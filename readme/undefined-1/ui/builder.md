# Builder

### Concepts

- BuilderBase is a feature of the ScreenSystem that works with DI Containers to create screens and generate Pages and Modals.
- The elements to be used in the next screen can be defined and passed as Parameters.
- For example, a UI where tapping an item in your inventory takes you to the item detail page,
  - You can pass the ID of the selected item as a parameter to the next screen.

### Example code in the Sign In Modal

```csharp
public class SignInModalBuilder : ModalBuilderBase<SignInModalLifecycle, SignInModalView>
{
    public SignInModalBuilder(bool playAnimation) : base(playAnimation)
    {
    }
}
```

### If you want to pass parameters to the screen call, you can use the

- ModalBuilderBase and PageBuilderBase come in two versions, one with parameters and one without.

```csharp
namespace ScreenSystem.Modal
{
    public abstract class ModalBuilderBase<TModal, TModalView, TParameter> : ModalBuilderBase<TModal, TModalView>
        where TModal : IModal
        where TModalView : ModalViewBase
    {
        public ModalBuilderBase(TParameter parameter, bool playAnimation = true, string overridePrefabName = null);
​
        protected override void SetUpParameter(LifetimeScope lifetimeScope);
​
        public async UniTask<IModal> Build(ModalContainer modalContainer, LifetimeScope parent, CancellationToken cancellationToken);
    }
​
    public abstract class ModalBuilderBase<TModal, TModalView> : IModalBuilder
        where TModal : IModal
        where TModalView : ModalViewBase
    {
        public ModalBuilderBase(bool playAnimation = true, string overridePrefabName = null);
    }
}
```

If you use a parameterized BuilderBase, the LifetimeScope for that screen will also be parameterized by the `LifetimeScopeWithParameter<T>` This way, when the screen is created on the Builder side, it will automatically pass the parameters to the LifetimeScope.


