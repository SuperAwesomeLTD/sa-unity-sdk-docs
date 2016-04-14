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

Integrate the Unity SDK
^^^^^^^^^^^^^^^^^^^^^^^

To integrate the base Unity SDK into your app, first download the
`SuperAwesome.unitypackage <https://github.com/SuperAwesomeLTD/sa-unity-sdk-docs/raw/master/source/res/SuperAwesome.unitypackage>`_
file and import it into your Unity project as a custom assets package.

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
In order to complete the SDK integration, skip to either the iOS or Android section of this documentation.

Add iOS dependencies
^^^^^^^^^^^^^^^^^^^^

To complete integrating the SDK for iOS, you'll need to follow the next steps (once):

Build the project for iOS
-------------------------

To do this, click on **File > Build Settings** menu.
There, select the **iOS** option and check the **Symlink Unity Libraries** and **Development build** options.
Then, click on **Build** and save the new XCode project on your drive.

.. image:: img/IMG_04_iOSBuild.png

Add the SuperAwesome iOS SDK via CocoaPods
------------------------------------------

Next, you'll need to add the AwesomeAds iOS SDK by following the quick guide below:

Install CocoaPods (if you haven't already):

.. code-block:: shell

    sudo gem install cocoapods


Go to your project's directory and initialize CocoaPods:

.. code-block:: shell

    cd /project_root
    pod init


This will create a new file simply called **Podfile**. Open it and alter it to look like this:

.. code-block:: shell

    # Uncomment this line to define a global platform for your project
    platform :ios, '6.0'

    target 'Unity-iPhone' do
      pod 'SuperAwesome/Unity'
    end


Save the file and exit it. Then execute

.. code-block:: shell

    pod update


to tell CocoaPods to add the SuperAwesome iOS SDK library and Unity plugins to your project.
Don't forget to open the **.xcworkspace** file to open your project in Xcode, instead of the .xcproj file, from here on out.

Final setup
-----------

After the CocoaPod dependency has been added, you have to make some changes to the default Unity build configuration, as the CocoaPods settings need
to be propagated in the build target but won't have done so since Unity has already set these values.

In the **Build Settings** tab you will need to search for each of **OTHER_LDFLAGS**, **OTHER_CFLAGS** and **HEADER_SEARCH_PATHS**,
double-click on them, and add **$(inherited)** to the list of existing values for these settings.
You likely will have also received a message when running **pod update**, warning you to do this.

.. image:: img/IMG_05.png
.. image:: img/IMG_06.png
.. image:: img/IMG_07.png

Finally, when targeting devices for iOS 9 onwards, don't forget to add, for the moment, the following key to your plist file:

.. code-block:: xml

    <dict>
    	<key>NSAllowsArbitraryLoads</key>
    	<true/>
    </dict>


to be able to load data over both HTTPS and HTTP.

Once this is done your iOS project will be ready to use and any calls to the native SDK from your Unity project will work as expected.

Add Android dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

To complete integrating the SDK for Android, you'll need to follow the next steps (once):

Build the project for Android
-----------------------------

To do this, click on **File > Build Settings** menu.
There, select the **Android** option and check the **Google Android Project** and **Development build** options.
Then, click on **Build** and save the new Android project on your drive.

.. image:: img/IMG_08_AndroidBuild.png

Create the settings file
------------------------

Then, go to your new project folder:

.. code-block:: shell

    cd /project_root


And in the root of the project create an empty file called **settings.gradle**.

.. image:: img/IMG_08_AndroidProjectStructure.png

Then, using Android Studio, import your Unity Android project by selecting the .gradle file you just created (and following all instructions).

.. image:: img/IMG_08_ImportingAndroid.png

Add the SuperAwesome Android SDK via Gradle
-------------------------------------------

Next, you'll need to add the AwesomeAds Android SDK by following the quick guide below.

Just include the following in your module's **build.gradle** file (usually the file under **MyApplication/app/**):

.. code-block:: shell

    repositories {
        maven {
            url  "http://dl.bintray.com/sharkofmirkwood/maven"
        }
    }

    dependencies {
        compile 'tv.superawesome.sdk:sa-sdk:<sdk_version_android>@aar'
        compile 'com.google.android.gms:play-services:8.4.0'
    }



and click **Sync Task** when prompted.

.. image:: img/IMG_09_GradleSetup.png

If you'd want to install the SDK from a .jar archive, not through Gradle, follow the instructions
`here </extdocs/sa-mobile-sdk-android/html/02integrate.html#add-the-sdk-as-a-jar-library>`_.

Final setup
-----------

Finally, you'll need to do a small change to your default Unity Android manifest file.
Find the line

.. code-block:: xml

    <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="false" />

and set the value to **true**.
If you don't do this then banner ads won't be clickable on Android.

Before you begin
^^^^^^^^^^^^^^^^

Please remember that in Unity, click events are not triggered at all unless there is an EventSystem UI object.
If this doesn't exist in the Hierarchy, add one from the **GameObject > UI** menu.

Also, since the Unity SDK uses the iOS / Android native SDK, testing your app in Unity won't show ads. Only by playing the app on a simulator
or device will the whole ad process be triggered.
