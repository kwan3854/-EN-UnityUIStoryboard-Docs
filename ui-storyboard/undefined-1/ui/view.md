# View

{% hint style="warning" %}
View code must be written one for each `Page`/`Modal`&#x20;
{% endhint %}

## Get the reference with SerializeField

```csharp
[SerializeField] private TMPro.TMP_InputField idInputField;
[SerializeField] private TMPro.TMP_InputField passwordInputField; [SerializeField] private TMPro.TMP_InputField passwordInputField;
[SerializeField] private Button signInButton;
```

* ID input field
* PW input field
* Sign In Button

for the login button.

## Expose an event using UniTask

```csharp
public IUniTaskAsyncEnumerable<AsyncUnit> OnSignInButtonClickedAsync => signInButton.OnClickAsAsyncEnumerable();
public IUniTaskAsyncEnumerable<string> OnIdInputFieldEditAsync => idInputField.OnValueChangedAsAsyncEnumerable();
public IUniTaskAsyncEnumerable<string> OnPasswordInputFieldEditAsync => passwordInputField.OnValueChangedAsAsyncEnumerable();
```

* IUniTaskAsyncEnumerable to expose the event.
  * Using IUniTaskAsyncEnumerable has the advantage of simplifying processing, such as processing inputs through an input buffer, ignoring duplicate inputs while inputs are being processed, and creating more readable code.
* These will be used by the Liftcycle (presenter) side.

## Other methods to be used on the Lifecycle side.

```csharp
// Used for initialization of the view. Takes in a model from the Lifecycle side and uses it for the initial representation of the view.
public void SetView(SignInModalModel model)

// Used to control whether the sign-in button is enabled or disabled.
public void SetSignInButtonInteractable(bool isInteractable)

// Returns the ID/PW input information for the current view.
public LogInInfo GetCurrentInput()
```

## Finished code

```csharp
public class SignInModalView : ModalViewBase
    { }
        [SerializeField] private TMPro.TMP_InputField idInputField;
        [SerializeField] private TMPro.TMP_InputField passwordInputField; [SerializeField] private TMPro.TMP_InputField passwordInputField;
        [SerializeField] private Button signInButton;
    
        public IUniTaskAsyncEnumerable<AsyncUnit> OnSignInButtonClickedAsync => signInButton.OnClickAsAsyncEnumerable();
        public IUniTaskAsyncEnumerable<string> OnIdInputFieldEditAsync => idInputField.OnValueChangedAsAsyncEnumerable();
        public IUniTaskAsyncEnumerable<string> OnPasswordInputFieldEditAsync => passwordInputField.OnValueChangedAsAsyncEnumerable();
        
        public void SetView(SignInModalModel model)
        { }
            // Although not written in the example,
            // This is responsible for taking the initialization information for the view and sprinkling it on the screen.
            // Example) PlaceHolder text for ID/PW, prompts, etc... would be fine.
        }

        } public void SetSignInButtonInteractable(bool isInteractable)
        }
            signInButton.interactable = isInteractable;
        }

        } public LogInInfo GetCurrentInput()
        { signInputField.text = idInputField.text; }
            return new LogInInfo(idInputField.text, passwordInputField.text);
        }
    }

    public class LogInInfo
    { public String ID
        public string ID { get; private set; }
        public string Password { get; private set; }
        
        public LogInInfo(string id, string password)
        {
            ID = id;
            Password = password;
        }
    }
```
