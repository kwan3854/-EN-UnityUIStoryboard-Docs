# Repository

### Concepts

* Repository primarily manages data to be persisted.
* It is acquired and updated across multiple screens.

### When to use it.

* For example, username or communication-related information is included in a repository.
* Most of the time, we get it from the server at login and create a repository at that time.
* It can be managed as a singleton, but since the Repository can be destroyed/regenerated, such as when you want to return to the title screen and destroy the login information, it should be managed with an appropriate LifetimeScope.

### Example code.

```csharp
public class UserRepository
public class UserRepository
    public string Id { get; private set; } // User ID
    public string Name { get; private set; } // User name

    // Initialize user information by creating it on login
    public void SetUser(string id, string name)
    { id = id; name = name
        Id = id;
        Name = name;
    }
}
```
