"""
Overview of bats_server Package
==============================

The bats_server package is structured to handle various server-side functionalities related model serving for segmentation and training. 

Submodules:
------------

bats_server.models
    Defines the CustomCellpose model for cell segmentation.
    The model handles evaluation and forward pass tasks.

bats_server.segmentationclasses
    Defines segmentation classes for specific projects, such as GFPProjectSegmentation, GeneralSegmentation, and MitoProjectSegmentation.
    These classes contain methods for segmenting images and training models on images and masks.

bats_server.serviceclasses
    Defines service classes, such as CustomBentoService and CustomRunnable, for serving the models with BentoML and handling computation on remote Python workers.

bats_server.utils
    Provides various utility functions for dealing with image storage, image processing, feature extraction, file handling, configuration reading, and path manipulation.

"""
