# BATS Client
The client of our Bioimage Annotation Tool for Segmentation for microscopy imaging.

![stability-wip](https://img.shields.io/badge/stability-work_in_progress-lightgrey.svg)
[![Documentation Status](https://readthedocs.org/projects/BATS/badge/?version=latest)](https://BATS.readthedocs.io/en/latest/?badge=latest)

## How to use?

### Installation 

For installing bats-client you will first need to clone the repo:

```
git clone https://github.com/HelmholtzAI-Consultants-Munich/BATS.git
```

Then navigate to the client directory:
```
cd BATS/src/client
```

In your dedicated environment run:
```
pip install -e .
```

This installation has been thoroughly tested using a conda environment with python version 3.9, 3.10, 3.11 and 3.12 on a macOS local machine.



#### Launch BATS client

* **Instance** segmentation:

  Make sure the server is already running, either locally or remotely. Then, depending on the configuration, simply run:
  ```
  bats-client --mode local
  ```
  or 
  ```
  bats-client --mode remote
  ```
  depending on whether your server is running locally or remotely.

* **Multi-class instance** segmentation:

  When you additionally have data with multiple classes you will need to define this on runtime. You will need to add the ```--multi-class``` and ```--num-classes``` arguments to you run and specify the number of classes in your data. For example, for a multi-class problem with three classes, run:
   ```
  bats-client --mode local --multi-class --num-classes 3
  ```

## Want to know more?
Visit our [documentation](https://BATS.readthedocs.io/en/latest/bats_client_installation.html) for more information and a step by step guide on how to run the client.
