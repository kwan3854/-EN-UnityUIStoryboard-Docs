# Using auto-initialization

{% hint style="warning" %}
Be sure to do this in a new project. If you want to apply it to an existing project, manually clean up the asmdef and folder structure, etc.
{% endhint %}

## 1\. auto-initialize

### How to use auto-initialization

1. `Edit`\-> Initialize `Project Settings...` Click

<figure><img src="../../../../.gitbook/assets/ProjectSettingsMenu.png" alt="" width="373"><figcaption><p>Project Settings</p></figcaption></figure>

2. Select the UI Storyboard tab (you may see a Create Setup Variable button on first entry, click it if you do)
3. `Project Name` Enter a name for your project in
4. `Initialize Project Structure`Click the button

<figure><img src="../../../../.gitbook/assets/SettingInitialize.png" alt=""><figcaption><p>UI Storyboard Settings</p></figcaption></figure>

## 2\. What does auto-initialization do?

### It creates a folder structure.

<figure><img src="../../../../.gitbook/assets/StoryboardDirectoryStructure.png" alt=""><figcaption><p>Directories</p></figcaption></figure>

### Create the Assembly Definitions.

- `asmdef` Proper use of assembly definitions prevents you from writing code that deviates from the promised structure and makes your project compile faster.
- Auto-initialization is
  - will generate the required asmdefs you need by default.
  - Automatically generates the required reference, which is the most basic.

<figure><img src="../../../../.gitbook/assets/asmdef.png" alt=""><figcaption><p>Assembly Definition</p></figcaption></figure>


