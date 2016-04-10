# lti-flask-skeleton
A template for developing an LTI application in Flask


Getting Started
===============

#. Obtain a PEM certificate. You'll eventually need one for your production server, but in the meantime you'll want one for local development. This process is one of the most frustrating steps, especially if you're on Windows, but it's worth it to be able to develop locally.

  #. Download and run this
  #. If you're on windows, you'll need to install the certificate
  #. Either way, ensure that there is a PEM file in your `certs/` directory and that it is correctly referenced in your `secrets.yaml`.
  
#. Choose your database for the local development instance and the production server. For the local development instance, I recommend using SQLite since it is lightweight and easy. For the production server, you will probably want to use MySQL or PostGres. You will not need to define the database schema yet, but you will need to make this decision. If you decide to use SQLite for your test server, carefully test your schema on the MySQL server early on, since you might find differences in their support (in particular, foreign key references and column typing).

#. Provide a `config/secrets.yaml` file. An example is given by the `config/example-secrets.yaml` file, which you can rename and fill out according to your settings. Explanatory comments are included in this file.

#. Modify any fields in the `config/config.py` file that are marked TODO. Examples are given.
  
Moving to Production
====================
  
#. Change the `main.py` file's configuration load from `TestConfig` to `ProductionConfig`.
#. Set up a production database on the server, making sure there is a reference to it in the `config/config.py` file.

Running Your Site
=================

#. Run the secure server by using `manage.py` with the `secure` command:

    > python manage.py secure
    
#. If everything goes well, you should be told that your server is running, and that you can access it a specific URL (e.g., "https://localhost:5000").

#. If you're using Chrome, you may need to click through a "Untrusted Certificate" error. This may look scary, but obviously you can trust your own site.

PEM Files?
==========

LTI Authentication uses the OAuth standard, which is a secure protocol over HTTPS for communication between computers. It's a giant pain, but a necessary part of doing modern web business. LTI requires a certificate for your server, showing to visitors that someone else has endorsed you. You'll need to have your production server's certificate signed by a trusted entity (some universities will have a service for this), which means shelling out some money annually. Fortunately, your local development instance can have a self-signed certificate, which will only cause a very minor nuisance when you start every other work session (you have to tell Chrome not to worry about the fact that it's self-signed).