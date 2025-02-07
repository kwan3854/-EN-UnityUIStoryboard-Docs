# Tips for newbies

## The importance of color palettes

### Centralizing color

- UI design in games often involves using the same or similar designs in multiple places, just with different colors.
- This is a development practice that stems from several reasons.
  - Saves resources: The same resources can be recycled. This has a positive impact on development costs, game performance, and more.
  - Easier to add variety: You can create UIs with different looks and feel with relatively little effort.

### Organize your design

- UI/UX artists should always design with a set of key colors and apply them to shared resources as a base.
- Please keep your color palette organized and in line with your plans.
- Make sure that image resources, etc. are white/gray so that we can colorize them and use them in Unity (they should never be colored by themselves).

{% hint style="success" %}
If you don't have a structured color palette system or internal tooling in place, try UPalette, an open-source UI color palette system.
{% endhint %}

## Resource management and performance

### In UI-centric apps, performance is the responsibility of the designer.

- In a UI-centric app, it's safe to say that the UI/UX artist is responsible for over 90% of the app's performance.
- Due to the nature of game engines, most of the performance load comes from resources.
- Poor resource management (duplicate resources/too large resources/incorrect sprite atlas management) is a huge performance drain. 

### Recycle resources as much as possible

- Don't create too many different resources.
- Try combining/rearranging/coloring a few basic elements to add variety.

### Think 9-Slice

- 9-Slice is a very common way of using image resources in game engines.
- It uses an image by slicing it into nine pieces and stretching them.
- Think of it as a way of recycling resources - creating a minimum-sized resource and stretching it to use in a variety of sizes.
- Please create/manage resources in a form that can be used as 9-Slice in the game engine.

## The naming should be consistent with

### prefix and postfix

- prefix: What comes before.
- postfix: trailing.

Establish proper prefix and postfix naming conventions when naming your resources, then start your project.

Projects with inconsistent naming conventions become incredibly unmanageable as they grow in size and as the project progresses.

### Let's split folders

- Divide your folders appropriately based on where your resources will be used and your different design intentions.
- Organize them so they're easy for others to find.
- This is also very much related to the Sprite Atlas (performance optimization) below.

## Sprite Atlas

- Depending on your usage, bundling and managing your Sprite Atlas appropriately can yield significant performance gains.

## Other Notes

### Notch (safe area)

- Most modern smartphones have an area that covers the screen, such as a notch or punch hole.
- Artists must take this into account when designing the screen composition.


