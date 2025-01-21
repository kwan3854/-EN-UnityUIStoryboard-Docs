# Express screen movement

## How to show screen pans

* You can display screen transitions by connecting nodes and nodes.
* When planners mark screen transitions, it is easier for UI/UX designers to understand the planning intent, developers do not need to organize the screen transition process through separate documentation, and there is less room for mistakes.

## Planning examples

Let's take a look at a very simple planning example.

We want to plan the login screen, the very first screen of our app, and represent it in a storyboard.

* On the first login `Page`, there is a button called `Sign In`.
* After pressing the 'Sign In' button, a popup `Modal' will appear where you can enter your username and password.
* In this modal window, there is a login button, enter your username and password and press it to log in.
* After successful login, you will be taken to the main screen of the app.

Let's build a storyboard based on the above plan.

## Example storyboard

{% hint style="success" %}
You can rename a node by right-clicking on it -> Rename.

> > Page and Modal should be named with Page and Modal after them to make it easier to recognize them.
>
> > _Example: Item Shop Page, Alert Modal...._
{% endhint %}

<figure><img src="../../../.gitbook/assets/screenshot 2025-01-12 AM 12.37.14.png" alt=""><figcaption><p>Example Storyboard</p></figcaption></figure>

* Consists of three UI elements.
  * **Log In Page:** This is the initial screen where the login button exists.
  * **Log In Modal:** The popup window where the actual login takes place.
  * **Main Page:** The main screen that you can enter after a successful login.
* The Log In Page is the only trunk line to the Log In Modal.
  * The Log In Page is only capable of displaying the Log In Modal.
* From the Log In Modal, there are two paths to take.
  * Return to the Log In Page: when the modal window is closed.
  * Go to Main Page: When logging in successfully.
