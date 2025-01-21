# UseCase

* 오직 도메인 로직만을 생각해서 설계.
* 하나의 UseCase는 오직 하나의 명확한 사용 용도만 있음.
* UseCase는 단 하나의 메서드만을 가진다.
* 반드시 인터페이스로 구성한다.

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
