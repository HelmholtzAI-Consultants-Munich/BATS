"""
Overview of bats_client Package
==============================

The `bats_client` package contains modules and subpackages for interacting with a server for model inference and training. It provides functionalities for managing GUI windows, handling image storage, and connecting to the server for model operations.

Subpackages
------------

- **bats_client.gui package**: Contains modules for GUI components.
  
  - **Submodules**:
  
    - ``bats_client.gui.main_window``: Defines the main application window and associated event functions.
    - ``bats_client.gui.napari_window``: Manages the Napari window and its functionalities.
    - ``bats_client.gui.welcome_window``: Implements the welcome window and its interactions.

- **bats_client.utils package**: Contains utility modules for various tasks.
  
  - **Submodules**:
  
    - ``bats_client.utils.bentoml_model``: Handles interactions with BentoML for model inference and training.
    - ``bats_client.utils.fsimagestorage``: Provides functions for managing images stored in the filesystem.
    - ``bats_client.utils.settings``: Defines initialization functions and settings.
    - ``bats_client.utils.utils``: Offers various utility functions for common tasks.

Submodules
------------

- **bats_client.app module**: Defines the core application class and related functionalities.
  
  - **Classes**:
  
    - ``bats_client.app.Application``: Represents the main application and provides methods for image management, model interaction, and server connectivity.
    - ``bats_client.app.ImageStorage``: Abstract base class for image storage operations.
    - ``bats_client.app.Model``: Abstract base class for model operations.

This package structure allows for easy management of GUI components, image storage, model interactions, and server connectivity within the bats_client application.

"""
