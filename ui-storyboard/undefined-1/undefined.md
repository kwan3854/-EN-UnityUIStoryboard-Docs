# Install

{% hint style="success" %}

### We recommend using OpenUPM.

Unity UI Storyboard relies on many open source libraries. By using OpenUPM, you can automatically remove many dependencies. 

If for some reason you don't want to use OpenUPM, you'll need to resolve the dependencies yourself. Dependencies are defined in the [dependencies.md](../undefined/dependencies.md "mention")for the dependencies
{% endhint %}

## Use OpenUPM (recommended)

### Install using the command-line interface (recommended)

1. Navigate to the location of your Unity project
2. Enter the command below

```bash
openupm add com.kwanjoong.unityuistoryboard
```

### Install via package manager

1. `Edit` ->>. `Project Settings ->` `Package Manager`
2. Register a new Scoped Registry (or modify an already existing OpenUPM entry)

```
Name: package.openupm.com
URL: https://package.openupm.com
```

3. `Save` or `Apply` or click
4. `Window` -> click `Package Manager 열기`
5. `+` Click
6.  `Add package by name...` or `Add package from git URL...` 选择
7. `com.kwanjoong.unityuistoryboard` to the name
8. Enter the latest/desired version (e.g. 0.1.0)
9. `Add` Click

***

or [Packages/manifest.json](https://docs.unity3d.com/Manual/upm-manifestPrj.html) you can also insert the code below directly into

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

## Installing with Git and a Package Manager (not recommended)

1. `Window` ->Git `Package Manager 열기`
2. `+` Click
3. `Add package from git URL...` Select
4. `https://github.com/kwan3854/UnityUIStoryboard.git 입력`
5. `주의: 직접 의존성을 해소하세요.`


