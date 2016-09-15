Interstitial Ads
================

The following code block sets up an interstitial ad and loads it:

.. code-block:: c#

    public class MainScript : MonoBehaviour {

        // initialization
        void Start () {

            // to display test ads
            SAInterstitialAd.enableTestMode ();

            // lock orientation to portrait or landscape
            SAInterstitialAd.setOrientationPortrait ();

            // ask users to add two numbers when clicking on an ad
            SAInterstitialAd.enableParentalGate ();

            // start loading ad data for a placement
            SAInterstitialAd.load (30473);
        }
    }

Once you've loaded an ad, you can also display it:

.. code-block:: c#

    public void playInterstitial () {

        // check if ad is loaded
        if (SAInterstitialAd.hasAdAvailable (30473)) {

            // display the ad
            SAInterstitialAd.play (30473);
        }
    }
