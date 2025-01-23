# View

{% hint style="warning" %}
View code must use the `Page`/ / / or`Modal` for each /. 
{% endhint %}

## Getting a reference with SerializeField

```csharp
[SerializeField] private TMPro.TMP_InputField idInputField;
[SerializeField] private TMPro.TMP_InputField passwordInputField;
[SerializeField] private Button signInButton;
```

- ID Input Fields
- PW input field
- Login button

for the login button.

## Exposing events with UniTask

```csharp
public IUniTaskAsyncEnumerable<AsyncUnit> OnSignInButtonClickedAsync => signInButton.OnClickAsAsyncEnumerable();
public IUniTaskAsyncEnumerable<string> OnIdInputFieldEditAsync => idInputField.OnValueChangedAsAsyncEnumerable();
public IUniTaskAsyncEnumerable<string> OnPasswordInputFieldEditAsync => passwordInputField.OnValueChangedAsAsyncEnumerable();
```

- Expose events using IUniTaskAsyncEnumerable.
  - Using IUniTaskAsyncEnumerable has the advantage of making your code easier to process and more readable, such as processing input through an input buffer or ignoring duplicate inputs while they are being processed.
- These will be used by the Liftcycle (presenter) side.

## Other Lifecycle-side methods to use

```csharp
// 뷰의 초기화에 사용됩니다. Lifecycle 측으로부터 모델을 입력받아 view의 초기 표현에 사용됩니다.
public void SetView(SignInModalModel model)

// 로그인 버튼의 활성화 여부를 조절하는데 사용됩니다.
public void SetSignInButtonInteractable(bool isInteractable)

// 현재 뷰의 ID/PW 입력 정보를 반환합니다.
public LogInInfo GetCurrentInput()
```

## Finished code

```csharp
public class SignInModalView : ModalViewBase
    {
        [SerializeField] private TMPro.TMP_InputField idInputField;
        [SerializeField] private TMPro.TMP_InputField passwordInputField;
        [SerializeField] private Button signInButton;
    
        public IUniTaskAsyncEnumerable<AsyncUnit> OnSignInButtonClickedAsync => signInButton.OnClickAsAsyncEnumerable();
        public IUniTaskAsyncEnumerable<string> OnIdInputFieldEditAsync => idInputField.OnValueChangedAsAsyncEnumerable();
        public IUniTaskAsyncEnumerable<string> OnPasswordInputFieldEditAsync => passwordInputField.OnValueChangedAsAsyncEnumerable();
        
        public void SetView(SignInModalModel model)
        {
            // 예시에서는 작성하지 않았습니다만,
            // 뷰의 초기화 정보를 받아 화면에 뿌려주는 역할을 하게 됩니다.
            // 예) ID/PW의 PlaceHolder text, 안내 메시지 등등... 을 구현하면 괜찮겠네요.
        }

        public void SetSignInButtonInteractable(bool isInteractable)
        {
            signInButton.interactable = isInteractable;
        }

        public LogInInfo GetCurrentInput()
        {
            return new LogInInfo(idInputField.text, passwordInputField.text);
        }
    }

    public class LogInInfo
    {
        public string ID { get; private set; }
        public string Password { get; private set; }
        
        public LogInInfo(string id, string password)
        {
            ID = id;
            Password = password;
        }
    }
```


