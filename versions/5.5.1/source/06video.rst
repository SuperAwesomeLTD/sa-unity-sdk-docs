Video Ads
=========

The following code block sets up a video ad and loads it:

.. code-block:: c#

    public class MainScript : MonoBehaviour {

        // initialization
        void Start () {

            // to display test ads
            SAVideoAd.enableTestMode ();

            // ask users to add two numbers when clicking on an ad
            SAVideoAd.enableParentalGate ();

            // lock orientation to portrait or landscape
            SAVideoAd.setOrientationPortrait ();

            // enable or disable the android back button
            SAVideoAd.enableBackButton ();

            // enable or disable a close button
            SAVideoAd.enableCloseButton ();

            // enable or disable auto-closing at the end
            SAVideoAd.disableCloseAtEnd ();

            // start loading ad data for a placement
            SAVideoAd.load (30479);
        }
    }

Once you've loaded an ad, you can also display it:

.. code-block:: c#

    public void playVideo () {

        // check if ad is loaded
        if (SAVideoAd.hasAdAvailable (30479)) {

            // display the ad
            SAVideoAd.play (30479);
        }
    }

These are default values for all the parameters:

================== =============
Parameter          Value
================== =============
Configuration 	   Production
Test mode          Disabled
Parental gate      Enabled
Orientation        Any
Closes at end      True
Close button       Disabled
Small click button Disabled
================== =============

.. note:: For iOS, when locking orientation with either the **setOrientationPortrait** or **setOrientationLandscape** methods, the SDK will first look at the list of orientations
          supported by your app and conform to that.
          If, for example, you set a video ad to display in landscape mode but your app only supports portrait orientations, the ad will show in portrait mode.
          There are no such restrictions for Android.
