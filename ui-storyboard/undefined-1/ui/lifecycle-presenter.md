# Lifecycle (presenter)

## Big concepts

### WillPushEnterAsync initializes the visible part of the view. 

- This is to avoid blank screens or incorrect indicators during animations that switch screens.
- By default, everything that should be displayed in the View is taken from the Model and associated with the View in Presenter.
- The data values in the Model are all reactive by default.

### DidPushEnter defines the interactive behavior of the view.

- DidPushEnter occurs after the end of all transition animations.
- The reason for registering all user action processing, such as button events, after all transition animations have ended is because:
  - Too many unexpected things happen if the user can provide input during the transition.
  - From the user's perspective, it doesn't matter if they can interact during the transition, such as clicking a button.
  - From the user's perspective, it's more concerning to see a blank or incomplete screen during the transition animation, which is fine because WillPushEnterAsync handles all of that. 

### Put the key value of the Asset into an attribute.

`AssetName` Put the asset key value in the attribute. I recommend that all Assets be managed as Addressable. A simple implementation is to put the prep in the Resources folder and give it a key value. For more information, see the official readme for the UnityScreenNavigator library.

## Finished Code

```csharp
[AssetName("MainUI/Modal/SignInModal.prefab")]
public class SignInModalLifecycle : LifecycleModalBase
{
    private string _currentId = string.Empty;
    private string _currentPassword = string.Empty;
    
    private readonly SignInModalView _view;
    private readonly ModalManager _modalManager;
    private readonly ISignInUseCase _signInUseCase;
    private readonly PageEventPublisher _pageEventPublisher;

    [Inject]
    public SignInModalLifecycle(SignInModalView view, ModalManager modalManager, ISignInUseCase signInUseCase, PageEventPublisher pageEventPublisher) : base(view)
    {
        _view = view;
        _modalManager = modalManager;
        _signInUseCase = signInUseCase;
        _pageEventPublisher = pageEventPublisher;
    }

    protected override UniTask WillPushEnterAsync(CancellationToken cancellationToken)
    {
        base.WillPushEnterAsync(cancellationToken);

        var model = new SignInModalModel();
        _view.SetView(model);
        return UniTask.CompletedTask;
    }

    public override void DidPushEnter()
    {
        base.DidPushEnter();
        
        var currentId = string.Empty;
        var currentPassword = string.Empty;
        
        // Disable the sign-in button
        _view.SetSignInButtonInteractable(false);
        
        // ID input event processing
        _view.OnIdInputFieldEditAsync
            .ForEachAwaitAsync(async id =>
            {
                currentId = id;
                UpdateButtonState(currentId, currentPassword);

                await UniTask.CompletedTask;
            }, ExitCancellationToken)
            .Forget();

        // Password input event processing
        _view.OnPasswordInputFieldEditAsync
            .ForEachAwaitAsync(async password =>
            {
                currentPassword = password;
                UpdateButtonState(currentId, currentPassword);
                
                await UniTask.CompletedTask;
            }, ExitCancellationToken)
            .Forget();
        
        _view.OnSignInButtonClickedAsync
            .ForEachAwaitAsync(async _ =>
            {
                await OnSignInButtonClicked();
            }, ExitCancellationToken)
            .Forget();
    }

    // If both id and password are not empty, enable the sign-in button
    private void UpdateButtonState(string id, string password)
    {
        bool isInteractable = !string.IsNullOrEmpty(id) && !string.IsNullOrEmpty(password);
        _view.SetSignInButtonInteractable(isInteractable);
    }

    // When the sign-in button is clicked, send a sign-in request
    private async UniTask OnSignInButtonClicked()
    {
        var logInInfo = _view.GetCurrentInput();
        var response = await _signInUseCase.SignIn(new ISignInUseCase.SignInRequestData(logInInfo.ID, logInInfo.Password));
            
        // If the sign-in is successful, close the modal
        if (response.IsSuccess)
        {
            _pageEventPublisher.SendPushEvent(new EntryPageBuilder(true, true));
            await _modalManager.Pop(true, ExitCancellationToken);
        }
    }
}
```


