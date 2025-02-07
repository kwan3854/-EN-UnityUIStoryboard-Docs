# Representing screen movement

## How to show screen pans

- You can display screen transitions from node to node.
- When planners mark screen transitions, it's easier for UI/UX designers to understand the intent of the plan, developers don't have to document the process separately, and there's less room for error.

## Planning examples

Let's walk through a very simple planning example.

We want to plan the login screen, the very first screen of our app, and represent it in a storyboard.

- First login `Page` we have a button called "Sign In".
-  When you press the 'Sign in' button, a popup will appear where you can enter your username and password. `Modal` where you can enter your username and password.
- In this modal window, there is a Login button, which you can click to log in after entering your username and password.
- After successful login, you will be taken to the main screen of the app.

Let's build a storyboard based on the above plan.

## Example storyboard

{% hint style="success" %}
You can rename a node by right-clicking on the node -> Rename.

> Page and Modal are named for ease of distinction, using the **Page and Modal must be followed by the name**to distinguish them.
> 
> *Example: Item Shop Page, Alert Modal....*
> {% endhint %}

<figure><img src="../../../../.gitbook/assets/Storyboard1.png" alt=""><figcaption><p>Example Storyboard</p></figcaption></figure>

- It consists of three UI elements
  - **Log In Page:** The initial screen where the login button exists.
  - **Log In Modal:** A pop-up window that proceeds with the actual login.
  - **Main Page:** The main screen you enter after a successful login.
- From the Log In Page, the only trunk line is the one leading to the Log In Modal.
  - The Log In Page can only bring up the Log In Modal.
-  The Log In Modal has two forks in the road.
  - Returning to the Log In Page: When you close the modal window, the
  - Going to the Main Page: When you successfully logged in.


