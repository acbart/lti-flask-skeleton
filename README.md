# lti-flask-skeleton
A template for developing an LTI application in Flask


Getting Started
===============

#. Provide a `config/secrets.yaml` file. An example is given by the `config/example-secrets.yaml` file, which you can rename and fill out according to your settings. Explanatory comments are included in this file.

#. Modify any fields in the `config/config.py` file that are marked TODO. Examples are given.

#. Obtain a PEM certificate. You'll eventually need one for your production server, but in the meantime you'll want one for local development. This process is one of the most frustrating steps, especially if you're on Windows, but it's worth it to be able to develop locally.

  #. Download and run this
  #. If you're on windows, you'll need to install the certificate
  #. Either way, ensure that there is a PEM file in your `certs/` directory and that it is correctly referenced in your `secrets.yaml`.

Running Your Site
=================

#. If you're using Chrome, you may need to click through a "Untrusted Certificate" error. This may look scary, but obviously you can trust your own site.