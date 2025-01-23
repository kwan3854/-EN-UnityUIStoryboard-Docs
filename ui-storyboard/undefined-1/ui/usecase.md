# UseCase

- Designed with only domain logic in mind.
- A single UseCase has only one clear use.
- A UseCase has only one method.
- It must be organized as an interface.

```csharp
public interface ISignInUseCase
{
    public UniTask<SignInResponseData> SignIn(SignInRequestData signInData);

    public class SignInRequestData
    {
        public string ID { get; private set; }
        public string Password { get; private set; }
        
        public SignInRequestData(string id, string password)
        {
            ID = id;
            Password = password;
        }
    }
    
    public class SignInResponseData
    {
        public bool IsSuccess { get; private set; }
        
        public SignInResponseData(bool isSuccess)
        {
            IsSuccess = isSuccess;
        }
    }
}
```

```csharp
public class SignInUseCase : ISignInUseCase
{
    private readonly ISignInRepository _accountRepository;

    [Inject]
    public SignInUseCase(ISignInRepository accountRepository)
    {
        _accountRepository = accountRepository;
    }

    public async UniTask<ISignInUseCase.SignInResponseData> SignIn(ISignInUseCase.SignInRequestData signInData)
    {
        return await SignInInternal(signInData);
    }

    private async UniTask<ISignInUseCase.SignInResponseData> SignInInternal(ISignInUseCase.SignInRequestData signInData)
    {
         var requestData =
            new ISignInRepository.SignInRequestData(signInData.ID, signInData.Password);
        var response = await _accountRepository.SignIn(requestData);
        return new ISignInUseCase.SignInResponseData(response.IsSuccess);
    }
}
```


