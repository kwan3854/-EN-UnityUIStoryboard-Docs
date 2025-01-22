# Use auto-initialization

{% hint style="warning" %}
Be sure to do this in a new project. If you want to apply it to an existing project, manually clean up your asmdefs, folder structure, etc.
{% endhint %}

## 1. Automatic initialization

### How to use auto-initialization

1. Click `Edit` -> `Project Settings...`

<figure><img src="../../../../.gitbook/assets/screenshot 2025-01-11 10.57.10.png" alt="" width="373"><figcaption><p>Project Settings</p></figcaption></figure>

2. select the UI Storyboard tab (you may see a Create Setup Variable button on first entry, click it if you do)
3. Enter a project name in the `Project Name` field
4. click the `Initialize Project Structure` button

<figure><img src="../../../.gitbook/assets/screenshot 2025-01-11 pm 10.57.23 (2).png" alt=""><figcaption><p>UI Storyboard Settings</p></figcaption></figure>

## 2. What does auto-initialization do?

### It creates a folder structure.

<figure><img src="../../../../.gitbook/assets/screenshot 2025-01-11 11:10.31 PM 11.10.31 (1).png" alt=""><figcaption><p>Directories</p></figcaption></figure>

### Create the Assembly Definitions.

* Proper use of `asmdef` prevents you from writing code that deviates from the promised structure, and makes your project compile faster.
* Auto-initialization.
  * Generates the required asmdefs that are needed at the most basic level.
  * Automatic generation of the most basic required references.

<figure><img src="../../../.gitbook/assets/screenshot 2025-01-11 11.12.47.png" alt=""><figcaption><p>Assembly Definition</p></figcaption></figure>

