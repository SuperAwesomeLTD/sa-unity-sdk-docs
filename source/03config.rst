Configuring the SDK
===================

Once you've integrated the SuperAwesome SDK, you can access all functionality by including the SuperAwesome library
in any C# script file you may want to use it.

.. code-block:: c#

    using SuperAwesome

There are also a few global SDK parameters you can change according to your needs:

=============  ==============  =======
Parameter      Values          Meaning
=============  ==============  =======
Configuration  | Production *  | Should always get ads from production server

Test mode      | Enabled       | Should the SDK serve test ads. For test
               | Disabled *    | placements (30471, 30476, etc) must be Enabled.
=============  ==============  =======
 * = denotes default values

You can leave these settings as they are or change them to fit your testing or production needs, as follows:

.. code-block:: c#

    using UnityEngine;
    using System.Collections;
    using SuperAwesome;

    public class MainScript : MonoBehaviour {

    	// Use this for initialization
    	void Start () {
            SuperAwesome.SuperAwesome.instance.setConfigurationProduction ();
            SuperAwesome.SuperAwesome.instance.enableTestMode ();
            // SuperAwesome.SuperAwesome.instance.disableTestMode ();
    	}

    	// Update is called once per frame
    	void Update () {

    	}
    }
