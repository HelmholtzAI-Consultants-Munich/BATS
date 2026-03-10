bats\_server package
===================

The bats_server package is structured to handle various server-side functionalities related model serving for segmentation and training. 

bats_server.models
    Defines various models for cell classification and segmentation, currently CustomCellposeModel.
    These models handle tasks such as evaluation, forward pass, and updating configurations.

bats_server.segmentationclasses
    Defines segmentation classes for specific projects, such as GFPProjectSegmentation, GeneralSegmentation, and MitoProjectSegmentation.
    These classes contain methods for segmenting images and training models on images and masks.

bats_server.serviceclasses
    Defines service classes, such as CustomBentoService and CustomRunnable, for serving the models with BentoML and handling computation on remote Python workers.

bats_server.utils
    Provides various utility functions for dealing with image storage, image processing, feature extraction, file handling, configuration reading, and path manipulation.


Submodules
----------

bats\_server.models module
-------------------------

.. automodule:: bats_server.models
   :members:
   :undoc-members:
   :show-inheritance:

bats\_server.segmentationclasses module
--------------------------------------

.. automodule:: bats_server.segmentationclasses
   :members:
   :undoc-members:
   :show-inheritance:

bats\_server.serviceclasses module
---------------------------------

.. automodule:: bats_server.serviceclasses
   :members:
   :undoc-members:
   :show-inheritance:

bats\_server.utils module
---------------------------------

.. toctree::
   :maxdepth: 4

   bats_server.utils
