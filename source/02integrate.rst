Getting started
===============

The SuperAwesome Unity SDK, as of version 3.0.8, is built with extensions to iOS / Android in order to work together
with the SuperAwesome Android or iOS SDK.
This in turn allows you to harness the full power of native components, such as video based on AVFoundation / VideoView technology,
proper WebViews, better fullscreen experience, etc.

**Note:** This document assumes:

* a Unity 4 / 5 Project named **UnityDemo**,
* containing a single scene, called **MainScene**, with a camera linked to
* a single C# file, called **MainScript.as**, that acts as main class.

Integrate Unity SDK
^^^^^^^^^^^^^^^^^^^

To integrate the base Unity SDK into your app, first download the
[SuperAwesome.unitypackage](https://github.com/SuperAwesomeLTD/sa-unity-sdk/blob/develop_v3/SuperAwesome.unitypackage?raw=true)
file and import it into your Unity project as a custom assets package.

You should see an image similar to this:

![](img/IMG_02_Import.png "Importing the SuperAwesome.unitypackage")

Select all the files, and click Import.
If all goes well you should have a series of new folders and files in your Assets directory.

![](img/IMG_03_Assets.png "The new assets folder")

The Unity SDK is essentially a thin layer of classes, functions and plugins used to communicate with the iOS or Android native SDKs. These two, depending on the case, will handle all the heavy lifting when it comes to actually loading ad data.
Rendering ads on screen falls also on the native SDKs for all three types of ads supported:
* Banner Ads
* Fullscreen or Interstitial Ads
* Preroll or Video Ads

This is so that your games or apps have the best support for rich media or third party tags.
In order to complete the SDK integration, skip to either the iOS or Android section of this documentation.

Add iOS dependencies
^^^^^^^^^^^^^^^^^^^^

Add Android dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

Final setup
^^^^^^^^^^^

Please remember that in Unity, click events are not triggered at all unless there is an EventSystem UI object.
If this doesn't exist in the Hierarchy, add one from the **GameObject > UI** menu.

Also, since the Unity SDK uses the iOS / Android native SDK, testing your app in Unity won't show ads. Only by playing the app on a simulator
or device will the whole ad process be triggered.
