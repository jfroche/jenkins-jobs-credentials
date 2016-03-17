Credentials Plugin for jenkins job builder
==========================================

This plugin enable jenkins job builder (http://docs.openstack.org/infra/jenkins-job-builder/) to create credentials using the credentials plugin ( https://wiki.jenkins-ci.org/display/JENKINS/Credentials+Plugin)
inside a folder with the folders plugin (https://wiki.jenkins-ci.org/display/JENKINS/CloudBees+Folders+Plugin).

To store ssh keys in the credentials you will also need the ssh credentials plugin ( https://wiki.jenkins-ci.org/display/JENKINS/Credentials+Plugin/SSH+Credentials+Plugin).

.. image:: https://travis-ci.org/jfroche/jenkins-job-builder.svg?branch=master
    :target: https://travis-ci.org/jfroche/jenkins-job-builder-credentials

Documentation
=============

Please see http://jenkins-job-builder-credentials.readthedocs.org/


INSTALL
=======

.. code-block:: bash

    $ pip install jenkins-jobs-credentials

Development
===========

.. code-block:: bash

    $ pip install tox
    # ... make changes ...
    $ tox


RUNNING TESTS
=============

.. code-block:: bash

    $ make test

BUILD DOCS
==========

.. code-block:: bash

    $ make docs

TODO
====

* Domain support
