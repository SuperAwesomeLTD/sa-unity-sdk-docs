Game Wall
=========

The following code block sets up a Game Wall ad and loads it:

.. code-block:: c#

    public class MainScript : MonoBehaviour {

        // initialization
        void Start () {

            // to display test ads
            SAGameWall.enableTestMode ();

            // ask users to add two numbers when clicking on an ad
            SAGameWall.enableParentalGate ();

            // enable or disable the android back button
            SAGameWall.enableBackButton ();

            // start loading ad data for a placement
            SAGameWall.load (88888);
        }
    }

Once you've loaded an ad, you can also display it:

.. code-block:: c#

    public void playInterstitial () {

        // check if ad is loaded
        if (SAGameWall.hasAdAvailable (88888)) {

            // display the ad
            SAGameWall.play (88888);
        }
    }
