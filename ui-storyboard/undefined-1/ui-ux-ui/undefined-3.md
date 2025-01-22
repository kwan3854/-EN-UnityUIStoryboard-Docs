# Tips for newbies

## The importance of color palettes

### Centralized management of color

* UI design in games often involves using the same or similar design in many places, just with different colors.
* This is a development practice that stems from several reasons.
  * Saving resources: the same resources can be recycled. This has a positive impact on development costs, game performance, etc.
  * Ease of adding variety: You can create UIs that feel different with relatively little effort.

### Organize your design

* UI/UX artists should always design with a set of key colors and apply them to shared resources.
* Organize the color palette systematically according to the plan.
* Image resources, etc. should be white/gray so that we can colorize them and use them in Unity. (They should never be colored by themselves).

{% hint style="success" %}
If you don't have an organized color palette system or internal tooling in place, consider using UPalette, an open-source UI color palette system.
{% endhint %}

## Resource management and performance

### In a UI-centric app, performance is the designer's responsibility.

* In UI-centric apps, it's safe to say that the UI/UX artist is responsible for over 90% of the app's performance.
* Due to the nature of game engines, most of the performance load comes from resources.
* Poor resource management (duplicate resources / too big resources / poor sprite atlas management) will cause a very large performance hit;

### Recycle resources as much as possible

* Don't create too many different resources.
* Try to mix/rearrange/color a few basic elements to give variety.

### Think 9-Slice

* 9-Slice is a very common way of using image resources in game engines.
* The image is cut into nine slices and stretched.
* Think of it as a way to recycle resources by creating a minimum-sized resource and stretching it to use multiple sizes.
* Please create/manage resources in a form that can be used as 9-Slice in the game engine.

## Naming is consistent

### prefix and postfix

* prefix: leading.
* postfix: trailing.

Start your project with the proper prefix and postfix naming conventions for naming resources.

Projects with inconsistent naming conventions become incredibly unmanageable as they grow in size and as the project progresses.

### Let's split up folders

* Divide folders appropriately based on the use of resources and different design intentions.
* Organize them so that they are easy for others to find.
* This is also very much related to the Sprite Atlas below (performance optimization).

## Sprite Atlas

* Keeping your Sprite Atlas organized and bundled appropriately for different uses can lead to very large performance gains.

## Other Notes

### Notches (safe area)

* Most modern smartphones have areas that cover the screen, such as notches/punch holes.
* Artists must take this into account when designing the screen composition.







