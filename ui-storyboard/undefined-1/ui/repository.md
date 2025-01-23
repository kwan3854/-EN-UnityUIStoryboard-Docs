# Repository

- `Gateway`and `UseCase`as an intermediary between
- `UseCase`was implemented with only domain logic in mind, `Gateway`is the bridge between the two, as it only thinks about communicating with the outside world.
  - In this case, it caches and processes the necessary data, handles communication exceptions, etc.
  - Caching data is done using the `Repository`is one of the important roles of `Repository`object's lifetime, so it's very important to make sure that the `Repository`has a certain lifetime and which `LifetimeScope`to which it should belong.

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


