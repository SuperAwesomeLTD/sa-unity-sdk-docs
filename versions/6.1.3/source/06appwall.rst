App Wall
========

The following code block sets up an App Wall ad and loads it:

.. code-block:: c#

    public class MainScript : MonoBehaviour {

        // initialization
        void Start () {

            // to display test ads
            SAAppWall.enableTestMode ();

            // enable or disable the android back button
            SAAppWall.enableBackButton ();

            // start loading ad data for a placement
            SAAppWall.load (88888);
        }
    }

Once you've loaded an ad, you can also display it:

.. code-block:: c#

    public void playInterstitial () {

        // check if ad is loaded
        if (SAAppWall.hasAdAvailable (88888)) {

            // display the ad
            SAAppWall.play (88888);
        }
    }

These are the default values:

================== =============
Parameter          Value
================== =============
Configuration 	   Production
Test mode          Disabled
================== =============
