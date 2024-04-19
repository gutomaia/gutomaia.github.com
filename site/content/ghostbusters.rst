Ghostbusters
############

:date: 2017-02-16 22:15
:modified: 2017-02-16 22:15
:tags: ghostbusters, travis, ci, automation, smartthings
:Category: automation
:slug: ghostbusters
:authors: Guto Maia
:sumary: python smartthings your CI

.. figure:: {static}/images/stranger_things_ghostbusters.jpg
    :align: center
    :alt: stranger things ghostbusters
    :scale: 50%

I had my childhood in the eighties, and 'course, I used to wake up on staturday morning to watch ghostbusters. Then, when I though for a continuos integration lamp, I know it should have the "prohibed ghost sign"! In this post, I'm gonna show you, how to use your smartthings hub to notify you when your travis deploy is broken.


Well, it's not hard, in fact, you might get yours working in a couple of minutes. As said, I will need a Smarthing Hub and a Switch. Then you need to follow the steps on `Iotdb Smartthings <https://github.com/dpjanes/iotdb-smartthings>`_.

With that setup, your smarthing thing had a JSON api that you can call on the cloud. All you need is the URL for the device and the access token. (I will post a simple code later)

And finally, add the SMARTTHINGS_URL and SMARTTHINGS_ACCESS_TOKEN vars to your travis settings and the following code .travis file.

.. code-block:: yml

    after_failure: >-
      curl -X PUT -H "Authorization: Bearer ${SMARTTHINGS_ACCESS_TOKEN}" -H "Content-Type: application/json" -d '{"switch": 1}' ${SMARTTHINGS_URL}


.. figure:: {static}/images/ghostbusters_lamp.jpg
    :align: center
    :alt: Who are you gonna call?
    :scale: 50%


Then, when a build got rogue on wedNESday, I got it! I ain't gotta a build falling. Not on my watch!
