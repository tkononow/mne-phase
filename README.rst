.. -*- mode: rst -*-

|Travis|_ |AppVeyor|_ |Codecov|_ |CircleCI|_ |ReadTheDocs|_

.. |Travis| image:: https://travis-ci.org/brainthemind/mne-phase.svg?branch=master
.. _Travis: https://travis-ci.org/brainthemind/mne-phase

.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/4qrnsuohh5g53i5u?svg=true
.. _AppVeyor: https://ci.appveyor.com/project/brainthemind/mne-phase

.. |Codecov| image:: https://codecov.io/gh/brainthemind/mne-phase/branch/master/graph/badge.svg
.. _Codecov: https://codecov.io/gh/brainthemind/mne-phase

.. |CircleCI| image:: https://circleci.com/gh/brainthemind/mne-phase.svg?style=svg
.. _CircleCI: https://circleci.com/gh/brainthemind/mne-phase/tree/master

.. |ReadTheDocs| image:: https://readthedocs.org/projects/mne-phase/badge/?version=latest
.. _ReadTheDocs: https://mne-phase.readthedocs.io/en/latest/?badge=latest

mne-phase - A template for mne-python compatible extensions
======================================================================

.. _mne-python: https://martinos.org/mne/stable/index.html

**mne-phase** is a template project for mne-python_ compatible
extensions.

*Thank you for cleanly contributing to the mne-python ecosystem!*

.. _documentation: https://mne-phase.readthedocs.io/en/latest/quick_start.html

Refer to the documentation_ to modify the template for your own mne-python
extension or follow this quick reference::

    $ git clone https://github.com/brainthemind/mne-phase.git mne-foo
    $ cd mne-foo
    $ # update mne_project_template_bootstrap.sh
    $ bash mne_project_template_bootstrap.sh
    $ rm mne_project_template_bootstrap.sh
    $ rm -rf .git
    $ git init && git add . && git commit -m 'Initial commit'
    $ git remote add origin https://github.com/your_remote/mne-foo.git
    $ git push origin master
    $ # Activate all CIs

Notice that appveyor badge image needs to be updated manually. Go where ``_AppVeyor:`` pints
in the resulting `README.rst` after bootstraping and substitute `4qrnsuohh5g53i5u` with
the relevant information from `settings` -> `badges` in appveyor's website of your project.
