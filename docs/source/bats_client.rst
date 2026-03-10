bats\_client package
===================

The bats_client package contains modules and subpackages for interacting with a server for model inference. It provides functionalities for managing GUI windows, handling image storage, and connecting to the server for model operations.

bats_client.app
   Defines the core application class and related functionalities.
    - ``bats_client.app.Application``: Represents the main application and provides methods for image management, model interaction, and server connectivity.
    - ``bats_client.app.DataSync``: Abstract base class for data synchronization operations.
    - ``bats_client.app.ImageStorage``: Abstract base class for image storage operations.
    - ``bats_client.app.Model``: Abstract base class for model operations.

bats_client.gui
   Contains modules for GUI components.
    - ``bats_client.gui.main_window``: Defines the main application window and associated event functions.
    - ``bats_client.gui.napari_window``: Manages the Napari window and its functionalities.
    - ``bats_client.gui.welcome_window``: Implements the welcome window and its interactions.

bats_client.utils
   Contains utility modules for various tasks.
    - ``bats_client.utils.bentoml_model``: Handles interactions with BentoML for model inference.
    - ``bats_client.utils.fsimagestorage``: Provides functions for managing images stored in the filesystem.
    - ``bats_client.utils.settings``: Defines initialization functions and settings.
    - ``bats_client.utils.sync_src_dst``: Implements data synchronization between source and destination.
    - ``bats_client.utils.utils``: Offers various utility functions for common tasks.


Submodules
----------

bats\_client.app module
----------------------

.. automodule:: bats_client.app
   :members:
   :undoc-members:
   :show-inheritance:

bats\_client.gui module
----------------------
.. toctree::
   :maxdepth: 4

   bats_client.gui
   
bats\_client.utils module
------------------------
.. toctree::
   :maxdepth: 4

   bats_client.utils
   
