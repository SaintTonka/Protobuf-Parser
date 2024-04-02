108-py-protobuf-template
========================

Шаблонный репозиторий задания "Разбор потока length-prefixed Protobuf сообщений на Python" (LEARNING_CENTER-108)

Virtual environment
===================

.. code-block:: bash

    python3 -m venv venv
    source venv/bin/activate # Unix
    venv\Scripts\activate # Windows
    pip install -r requirements.txt

Build
-----

.. code-block:: bash

    python3 setup.py build

Running tests
-------------

.. code-block:: bash

    python3 -m unittest discover tests
