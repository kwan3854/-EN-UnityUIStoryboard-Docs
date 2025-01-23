# Repository

### Concepts

- Repositories primarily manage data to be persisted.
- It is acquired and updated across multiple screens.

### When to use it?

- For example, usernames, communication-related information, etc. are handled by including them in a repository.
- In most cases, we get it from the server at login and create the repository at that time.
- You can manage it as a singleton, but make sure to manage it with the appropriate LifetimeScope because the Repository can be destroyed/rebuilt, for example, when you want to return to the title screen and destroy the login information.

### Example code

```csharp
public class UserRepository
{
    public string Id { get; private set; } // 유저 ID
    public string Name { get; private set; } // 유저명

    // 로그인 시 생성하여 사용자 정보 초기화
    public void SetUser(string id, string name)
    {
        Id = id;
        Name = name;
    }
}
```


