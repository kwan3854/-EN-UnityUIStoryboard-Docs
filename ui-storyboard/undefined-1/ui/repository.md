# Repository

* `Gateway`와 `UseCase`의 중개자 역할을 함.
* `UseCase`는 오직 도메인 로직만을 생각해서 구현되었고, `Gateway`는 오직 외부와의 통신만을 생각했기 때문에 그 중간에서 둘을 이어주는 역할을 함.
  * 이 때, 필요한 데이터의 캐싱, 가공, 통신 익셉션 처리 등등을 하게 됨.
  * 데이터의 캐싱은 `Repository`의 중요한 역할 중 하나인데, `Repository`객체의 수명과도 아주 깊게 연관되어있으므로, 해당 `Repository`가 어떤 수명을 가지고 어떤 `LifetimeScope`에 소속되어야 할지 잘 설계해야함.

```csharp
public class AccountRepository : ISignInRepository, ISignOutRepository,
    ISignUpRepository, IDeleteAccountRepository,
    IAccountInfoRepository
{
    private readonly IHttpClientGateway _httpClientGateway;
    
    private const string URL = "url";
    
    private string _id;
    private string _token;
    private string _nickName;

    [Inject]
    public AccountRepository(IHttpClientGateway httpClientGateway)
    {
        _httpClientGateway = httpClientGateway;
    }
    
    public async UniTask<ISignInRepository.SignInResponseData> SignIn(ISignInRepository.SignInRequestData signInData)
    {
        var requestData = new HttpSignInRequest(signInData.ID, signInData.Password);
        var httpResponse = await _httpClientGateway
            .RequestAsync<HttpSignInRequest, HttpSignInResponse>(URL, requestData);

        if (!httpResponse.IsSuccess)
        {
            return new ISignInRepository.SignInResponseData(false);
        }
            
        _token = httpResponse.Token;
        _nickName = httpResponse.NickName;
        _id = signInData.ID;
        
        return new ISignInRepository.SignInResponseData(true);
    }

    public async UniTask<ISignOutRepository.SignOutResponseData> SignOut()
    {
        var requestData = new HttpSignOutRequest(_token);
        var httpResponse = await _httpClientGateway
            .RequestAsync<HttpSignOutRequest, HttpSignInResponse>(URL, requestData);
        
        if (!httpResponse.IsSuccess)
        {
            return new ISignOutRepository.SignOutResponseData(false, "Sign out failed");
        }
        
        _token = null;
        _nickName = null;
        _id = null;
        
        return new ISignOutRepository.SignOutResponseData(true, "Sign out");
    }

    public async UniTask<ISignUpRepository.SignUpResponseData> SignUp(ISignUpRepository.SignUpRequestData signUpData)
    {
        throw new System.NotImplementedException();
    }

    public async UniTask<IDeleteAccountRepository.DeleteAccountResponseData> DeleteAccount(IDeleteAccountRepository.DeleteAccountRequestData deleteAccountData)
    {
        throw new System.NotImplementedException();
    }
    
    public IAccountInfoRepository.AccountInfo GetCurrentAccountInfo()
    {
        return new IAccountInfoRepository.AccountInfo("id", "nickName", "token");
    }
    
    [Serializable]
    public class HttpSignInRequest
    {
        [JsonProperty("id")]
        public string ID { get; }
        [JsonProperty("password")]
        public string Password { get; }

        public HttpSignInRequest(string id, string password)
        {
            ID = id;
            Password = password;
        }
    }
    
    [Serializable]
    public class HttpSignInResponse
    {
        [JsonProperty("isSuccess")]
        public bool IsSuccess { get; }
        
        [JsonProperty("token")]
        public string Token { get; }

        [JsonProperty("nickName")]
        public string NickName { get; }

        public HttpSignInResponse(bool isSuccess, string nickName, string token)
        {
            IsSuccess = isSuccess;
            NickName = nickName;
            Token = token;
        }
    }
    
    [Serializable]
    public class HttpSignOutRequest
    {
        [JsonProperty("token")]
        public string Token { get; }

        public HttpSignOutRequest(string token)
        {
            Token = token;
        }
    }
}
```
