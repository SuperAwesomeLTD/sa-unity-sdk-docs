Load ads
========

If you want more control over the ads that you load and display, the next sections will present how to load and display ads through
Unity C# scripting.

The SDK employs a two-step process:
First, you'll need to load ad data for each placement you'll want to display.
Then, once that data is successfully loaded, you can finally show the ad.
The two steps are independent of each other so you can easily pre-load ads for later use, saving performance.

In the code snippet below we'll start by loading data for the test placement **30471**.
A good place to do this is in a C# script's **Start()** function,
where we'll create a **SALoader** object to help us.

SALoader is a SDK class whose sole role is to load, parse, process and validate ad data.
You'll usually need just one instance per script.

.. code-block:: c#

    public class MainScript : MonoBehaviour {

        // create the loader reference
        SALoader loader = null;

        void Start () {

            // setup AwesomeAds
            SuperAwesome.SuperAwesome.instance.enableTestMode ();

            // create an instance of SALoader
            loader = SALoader.createInstance ();
            loader.loadAd (30471);
        }

        void Update () {

        }
    }

The **loadAd(30471)** function loads data asynchronously, so as not to block the main UI thread.
When it's done, it calls two important callback methods, **didLoadAd(SAAd loadedAd)** and **didFailToLoadAdForPlacementId(int placementId)**,
to notify you of either success or failure.
In order to use these callbacks:

* your script must implement the **SALoaderInterface**

.. code-block:: c#

    public class MainScript : MonoBehaviour, SALoaderInterface

* it must be set as delegate for the SALoader object created earlier

.. code-block:: c#

    public class MainScript : MonoBehaviour, SALoaderInterface {

        // create the loader reference
        SALoader loader = null;

        void Start () {

            // setup AwesomeAds
            SuperAwesome.SuperAwesome.instance.enableTestMode ();

            // create an instance of SALoader
            loader = SALoader.createInstance ();
            // assign delegate
            loader.loaderDelegate = this;
            loader.loadAd (30471);
        }
    }

* finally, your script must also implement the two callback methods mentioned above

.. code-block:: c#

    public class MainScript : MonoBehaviour, SALoaderInterface {

        // rest of your implementation

        public void didLoadAd(SAAd ad) {
            // at this moment ad data is ready
            ad.print();
    	}

    	public void didFailToLoadAd(int placementId) {
    		// at this moment no ad could be found
    	}
    }

You'll notice that didLoadAd(SAAd ad) has a callback parameter of type **SAAd**. The SAAd class contains all the information needed to
actually display an ad, such as format (image, video), dimensions, click URL, video information, creative details, etc.
You can find out all details by calling the **print()** function, as shown in the example.

Save an ad for later use
^^^^^^^^^^^^^^^^^^^^^^^^

To save ads for later use, you can do something like this:

.. code-block:: c#

    public class MainScript : MonoBehaviour, SALoaderInterface {

        // create the loader reference
    	SALoader loader = null;

        // create the SAAd reference
        // for banner ad data
    	SAAd bannerAdData = null;

    	void Start () {

            // setup AwesomeAds
            SuperAwesome.SuperAwesome.instance.enableTestMode ();

            loader = SALoader.createInstance ();
            loader.loaderDelegate = this;
            loader.loadAd (30471);
    	}

    	// Update is called once per frame
    	void Update () {

    	}

    	public void didLoadAd(SAAd ad) {
            // at this moment ad data is ready
            // and can be saved
            bannerAdData = ad;
    	}

    	public void didFailToLoadAd(int placementId) {
            // at this moment no ad could be found
    	}
    }

Save multiple ads for later use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Finally, if you want to load multiple ads and save them for later use, you can do as such:

.. code-block:: c#

    public class MainScript : MonoBehaviour, SALoaderInterface {

        // create the loader reference
        SALoader loader = null;

        // create multiple SAAd references
        SAAd bannerAdData = null;
        SAAd interstitialAdData = null;
        SAAd videoAdData = null;

        void Start () {

            // setup AwesomeAds
            SuperAwesome.SuperAwesome.instance.enableTestMode ();

            loader = SALoader.createInstance ();
            loader.loaderDelegate = this;
            // load ad data for a banner
            loader.loadAd(30471);
            // and for an interstitial
            banner.loadAd(30473);
            // and for a video
            banner.loadAd(30479);
        }

        // Update is called once per frame
        void Update () {

        }

        public void didLoadAd(SAAd ad) {
            // at this moment ad data is ready
            // and can be saved
            if (ad.placementId == 30471) {
                bannerAdData = ad;
            } else if (ad.placementId == 30473) {
                interstitialAdData = ad;
            } else if (ad.placementId == 30479) {
                videoAdData = ad;
            }
        }

        public void didFailToLoadAd(int placementId) {
            // at this moment no ad could be found
        }
    }
