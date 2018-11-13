Initialise the SDK
==================

The first thing you'll need to do after adding the SDK is to initialise it in a custom `Application` subclass in your Android app.

.. code-block:: c#

  public class MainScript : MonoBehaviour {

    // initialization
    void Start () {

      AwesomeAds.init(true)
    }
  }


Where the `initSDK` method takes a boolean parameter indicating whether logging is enabled or not.
For production environments logging should be off.
