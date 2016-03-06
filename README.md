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
  
Moving to Production
====================
  
#. Change the `main.py` file's configuration load from `TestConfig` to `ProductionConfig`.
#. Set up a production database on the server, making sure there is a reference to it in the `config/config.py` file.

Running Your Site
=================

#. If you're using Chrome, you may need to click through a "Untrusted Certificate" error. This may look scary, but obviously you can trust your own site.

#. Run the secure server by using `manage.py` with the `secure` command:

    > python manage.py secure

PEM Files?
==========

LTI Authentication uses the OAuth standard, which is a secure protocol over HTTPS for communication between computers. It's a giant pain, but a necessary part of doing modern web business. LTI requires a certificate for your server to do business. You'll need to have your production server's certificate signed by a trusted entity (some universities will have a service for this), which means shelling out some money annually. Fortunately, your local development instance can have a self-signed certificate, which will only cause a very minor nuisance when you start work everyday (you have to tell Chrome not to worry about the fact that it's self-signed).