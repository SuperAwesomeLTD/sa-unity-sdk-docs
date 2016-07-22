Integrate the SDK
=================

The SuperAwesome Unity SDK, as of version 3.0.8, is built with extensions to iOS / Android in order to work together
with the SuperAwesome Android or iOS SDK.
This in turn allows you to harness the full power of native components, such as video based on AVFoundation / VideoView technology,
proper WebViews, better fullscreen experience, etc.

**Note:** This document assumes:

* a Unity 4 / 5 Project named **UnityDemo**,
* containing a single scene, called **MainScene**, with a camera linked to
* a single C# file, called **MainScript.as**, that acts as main class.

Add the Unity SDK
^^^^^^^^^^^^^^^^^

To integrate the base Unity SDK into your app, you have two options:

1) Download the latest full SuperAwesome SDK: `SuperAwesomeSDK-<sdk_version_unity>.Unity.full.unitypackage <https://github.com/SuperAwesomeLTD/sa-sdk-build-repo/blob/master/package/SuperAwesomeSDK-<sdk_version_unity>.Unity.full.unitypackage?raw=true>`_.
The **full** version will contain everything you need in order to load and display banner, interstitial and video ads as well as the 3rd party `Moat Analytics <https://moat.com/analytics>`_ module.

2) Download the latest base SuperAwesome SDK: `SuperAwesomeSDK-<sdk_version_unity>.Unity.base.unitypackage <https://github.com/SuperAwesomeLTD/sa-sdk-build-repo/blob/master/package/SuperAwesomeSDK-<sdk_version_unity>.Unity.base.unitypackage?raw=true>`_.
This has the same functionality as the full version, but lacks the Moat Analytics module.

Either download you choose, you can then import it into your Unity project as a custom assets package.

You should see an image similar to this:

.. image:: img/IMG_02_Import.png

Select all the files, and click Import.
If all goes well you should have a series of new folders and files in your Assets directory.

.. image:: img/IMG_03_Assets.png

As mentioned, the Unity SDK is essentially a thin layer of classes, functions and plugins used to communicate with the iOS or Android native SDKs.
These two, depending on the case, will handle all the heavy lifting when it comes to actually loading ad data.
Rendering ads on screen falls also on the native SDKs for all three types of ads supported:

* Banner Ads
* Fullscreen or Interstitial Ads
* Preroll or Video Ads

This is so that your games or apps have the best support for rich media or third party tags.

For iOS
-------

When exporting to an XCode project you'll need to add the following flag to **Other linker flags** in **Build Settings**: '-ObjC'

For Android
-----------

When exporting to an Android Studio project you'll need to find the following entry from your AndroidManifest.xml file

.. code-block:: xml

    <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="false" />

and set its value to **true**. This will ensure then banner ads will be clickable.

Before you begin
----------------

Since the Unity SDK uses the iOS / Android native SDK, testing your app in Unity won't show ads. Only by playing the app on a simulator
or device will the whole ad process be triggered.
