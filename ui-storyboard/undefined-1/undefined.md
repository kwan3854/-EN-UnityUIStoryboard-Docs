# install

{% hint style="success" %}
### We recommend using OpenUPM.

Unity UI Storyboard relies on many opensource libraries. By using OpenUPM, you can automatically remove many dependencies &#x20;

If for some reason you don't want to use OpenUPM, you will need to resolve the dependencies manually. See [dependencies.md](../undefined/dependencies.md "mention") for the dependencies
{% endhint %}

## Use OpenUPM (recommended)

### Install using the command-line interface (recommended)

1. navigate to the location of your Unity project
2. enter the command below

```bash
openupm add com.kwanjoong.unityuistoryboard
```bash openupm add com.kwanjoong.unityuistoryboard

### Install via package manager

1. `Edit` -> `Project Settings ->` `Package Manager`
2. register a new Scoped Registry (or modify an already existing OpenUPM entry)

```
Name: package.openupm.com
URL: https://package.openupm.com
```

3. Click `Save` or `Apply` 4.
4. `Window` -> `Open Package Manager`
5. click `+`
6. select &#x20;`Add package by name...` or `Add package from git URL...`
7. Paste `com.kwanjoong.unityuistoryboard` as the name
8. enter the latest/desired version (e.g. 0.1.0)
9. Click `Add



Alternatively, you can insert the code below directly into [Packages/manifest.json](https://docs.unity3d.com/Manual/upm-manifestPrj.html).

```json
{
    "scopedRegistries": [
        {
            "name": "package.openupm.com",
            "url": "https://package.openupm.com",
            "scopes": []
        }
    ],
    "dependencies": {
        "com.kwanjoong.unityuistoryboard": "0.1.0"
    }
}
```

## Install using Git and a package manager (not recommended)

1. Open `Window` -> `Open Package Manager`.
2. click `+`
3. Select `Add package from git URL...` 3.
4. enter https://github.com/kwan3854/UnityUIStoryboard.git
5. click `Caution: remove direct dependencies`.
