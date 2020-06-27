script.flix.dummy
=================
A dummy provider for `Flix`_, mainly used for testing providers integration.

What is a provider?
-------------------

Providers are normal `Kodi`_ script `addons <https://kodi.wiki/view/Add-ons>`_ and thus can be installed/updated/distributed just like any other addon.
However, a provider must follow a set of rules:

- The provider name must follow the format **script.flix.{name}**, otherwise it won't be discovered.
- Provide a `xbmc.python.script` extension point: see `this <https://kodi.wiki/view/HOW-TO:Script_addon>`_.
- Implement the `Provider` API: see `flix.provider.Provider <https://flix.readthedocs.io/en/latest/flix_api.html#flix.provider.Provider>`_.

.. _Kodi: https://kodi.tv
.. _Flix: https://github.com/i96751414/plugin.video.flix
