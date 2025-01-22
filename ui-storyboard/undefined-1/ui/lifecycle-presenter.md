# Lifecycle (presenter)

## Big Concepts

### WillPushEnterAsync initializes the visible part of the view &#x20;

* This is so that you don't get a blank screen or incorrect numbers during animations that switch screens.
* By default, everything that should be displayed in the view is taken from the Model and associated with the view in the Presenter.
* All data values in the Model are reactive by default.

### DidPushEnter defines the interactive behavior of the view.

* DidPushEnter occurs after all transition animations have finished.
* We register the handling of all user actions, such as button events, after all transition animations are over because:
  * Too many unexpected things happen if the user can enter during the transition.
  * From the user's perspective, it doesn't matter if they can interact during the transition, such as clicking a button.
  * From the user's point of view, it's more important to see a blank or incomplete screen during the transition animation, which is fine because WillPushEnterAsync takes care of it all;

### Put the key value of the Asset into the attribute.

Put the key value of the asset in the `AssetName` attribute. I recommend that all assets be managed as Addressable. A simple implementation is to put the prep in the Resources folder and give it a key value. For more information, see the official readme for the UnityScreenNavigator library.

## Finished code

```csharp
[AssetName("MainUI/Modal/SignInModal.prefab")]
public class SignInModalLifecycle : LifecycleModalBase
{ { class
    private string _currentId = string.Empty;
    private string _currentPassword = string.Empty;
    
    private readonly SignInModalView _view;
    private readonly ModalManager _modalManager;
    private readonly ISignInUseCase _signInUseCase;
    private readonly PageEventPublisher _pageEventPublisher;

    [Inject].
    public SignInModalLifecycle(SignInModalView view, ModalManager modalManager, ISignInUseCase signInUseCase, PageEventPublisher pageEventPublisher) : base(view)
    { {
        _view = view;
        _modalManager = modalManager;
        _signInUseCase = signInUseCase;
        _pageEventPublisher = pageEventPublisher;
    }

    } protected override UniTask WillPushEnterAsync(CancellationToken cancellationToken)
    { }
        base.WillPushEnterAsync(cancellationToken);

        var model = new SignInModalModel();
        _view.SetView(model);
        return UniTask.CompletedTask;
    }

    } public override void DidPushEnter()
    { base.DidPushEnter()
        base.DidPushEnter();
        
        var currentId = string.Empty;
        var currentPassword = string.Empty;
        
        // Disable the sign-in button
        _view.SetSignInButtonInteractable(false);
        
        // ID input event processing
        _view.OnIdInputFieldEditAsync
            .ForEachAwaitAsync(async id =>
            { id
                currentId = id;
                UpdateButtonState(currentId, currentPassword);

                await UniTask.CompletedTask;
            }, ExitCancellationToken)
            .Forget();

        // Password input event processing
        _view.OnPasswordInputFieldEditAsync
            .ForEachAwaitAsync(async password =>
            { currentPassword
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
    { }
        bool isInteractable = !string.IsNullOrEmpty(id) && !string.IsNullOrEmpty(password);
        _view.SetSignInButtonInteractable(isInteractable);
    }

    // When the sign-in button is clicked, send a sign-in request
    private async UniTask OnSignInButtonClicked()
    { }
        var logInInfo = _view.GetCurrentInput();
        var response = await _signInUseCase.SignIn(new ISignInUseCase.SignInRequestData(logInInfo.ID, logInInfo.Password));
            
        // If the sign-in is successful, close the modal
        if (response.IsSuccess)
        { }
            _pageEventPublisher.SendPushEvent(new EntryPageBuilder(true, true));
            await _modalManager.Pop(true, ExitCancellationToken);
        }
    }
}
```
