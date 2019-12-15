#
# spec file for package python-django-cors-headers
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Fedora >= 38 no longer publishes python2 by default
%if 0%{?fedora} >= 30
%global with_python2 0
%else
%global with_python2 1
%endif

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

%global pypi_name django-cors-headers

# Common SRPM package
Name:           python-%{pypi_name}
Version:        3.2.0
Release:        0%{?dist}
Url:            https://github.com/adamchainz/django-cors-headers
Summary:        django-cors-headers is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
django-cors-headers
===================

.. image:: https://travis-ci.org/adamchainz/django-cors-headers.svg?branch=master
   :target: https://travis-ci.org/adamchainz/django-cors-headers

.. image:: https://img.shields.io/pypi/v/django-cors-headers.svg
    :target: https://pypi.python.org/pypi/django-cors-headers/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/python/black

A Django App that adds Cross-Origin Resource Sharing (CORS) headers to
responses. This allows in-browser requests to your Django application from
other origins.

About CORS
----------

Adding CORS headers allows your resources to be accessed on other domains. It's
important you understand the implications before adding the headers, since you
could be unintentionally opening up your site's private data to others.

Some good resources to read on the subject are:

* The `Wikipedia Page <https://en.m.wikipedia.org/wiki/Cross-origin_resource_sharing>`_
* The `MDN Article <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS>`_
* The `HTML5 Rocks Tutorial <https://www.html5rocks.com/en/tutorials/cors/>`_

Requirements
------------

Python 3.5-3.8 supported.

Django 1.11-3.0 suppported.

Setup
-----

Install from **pip**:

.. code-block:: sh

    pip install django-cors-headers

and then add it to your installed apps:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'corsheaders',
        ...
    ]

You will also need to add a middleware class to listen in on responses:

.. code-block:: python

    MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]

``CorsMiddleware`` should be placed as high as possible, especially before any
middleware that can generate responses such as Django's ``CommonMiddleware`` or
Whitenoise's ``WhiteNoiseMiddleware``. If it is not before, it will not be able
to add the CORS headers to these responses.

Also if you are using ``CORS_REPLACE_HTTPS_REFERER`` it should be placed before
Django's ``CsrfViewMiddleware`` (see more below).

About
-----

**django-cors-headers** was created in January 2013 by Otto Yiu. It went
unmaintained from August 2015 and was forked in January 2016 to the package
`django-cors-middleware <https://github.com/zestedesavoir/django-cors-middleware>`_
by Laville Augustin at Zeste de Savoir.
In September 2016, Adam Johnson, Ed Morley, and others gained maintenance
responsibility for **django-cors-headers**
(`Issue 110 <https://github.com/adamchainz/django-cors-headers/issues/110>`__)
from Otto Yiu.
Basically all of the changes in the forked **django-cors-middleware** were
merged back, or re-implemented in a different way, so it should be possible to
switch back. If there's a feature that hasn't been merged, please open an issue
about it.

**django-cors-headers** has had `40+ contributors
<https://github.com/adamchainz/django-cors-headers/graphs/contributors>`__
in its time; thanks to every one of them.

Configuration
-------------

Configure the middleware's behaviour in your Django settings. You must add the
hosts that are allowed to do cross-site requests to
``CORS_ORIGIN_WHITELIST``, or set ``CORS_ORIGIN_ALLOW_ALL`` to ``True``
to allow all hosts.

``CORS_ORIGIN_ALLOW_ALL``
~~~~~~~~~~~~~~~~~~~~~~~~~
If ``True``, the whitelist will not be used and all origins will be accepted.
Defaults to ``False``.

``CORS_ORIGIN_WHITELIST``
~~~~~~~~~~~~~~~~~~~~~~~~~

A list of origins that are authorized to make cross-site HTTP requests.
Defaults to ``[]``.

An Origin is defined by
`the CORS RFC Section 3.2 <https://tools.ietf.org/html/rfc6454#section-3.2>`_
as a URI scheme + hostname + port, or one of the special values `'null'` or
`'file://'`.
Default ports (HTTPS = 443, HTTP = 80) are optional here.

The special value `null` is sent by the browser in
`"privacy-sensitive contexts" <https://tools.ietf.org/html/rfc6454#section-6>`__,
such as when the client is running from a ``file://`` domain.
The special value `file://` is sent accidentally by some versions of Chrome on
Android as per `this bug <https://bugs.chromium.org/p/chromium/issues/detail?id=991107>`__.

Example:

.. code-block:: python

    CORS_ORIGIN_WHITELIST = [
        "https://example.com",
        "https://sub.example.com",
        "http://localhost:8080",
        "http://127.0.0.1:9000"
    ]


``CORS_ORIGIN_REGEX_WHITELIST``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A list of strings representing regexes that match Origins that are authorized
to make cross-site HTTP requests. Defaults to ``[]``. Useful when
``CORS_ORIGIN_WHITELIST`` is impractical, such as when you have a large number
of subdomains.

Example:

.. code-block:: python

    CORS_ORIGIN_REGEX_WHITELIST = [
        r"^https://\w+\.example\.com$",
    ]

--------------

The following are optional settings, for which the defaults probably suffice.

``CORS_URLS_REGEX``
~~~~~~~~~~~~~~~~~~~

A regex which restricts the URL's for which the CORS headers will be sent.
Defaults to ``r'^.*$'``, i.e. match all URL's. Useful when you only need CORS
on a part of your site, e.g. an API at ``/api/``.

Example:

.. code-block:: python

    CORS_URLS_REGEX = r'^/api/.*$'

``CORS_ALLOW_METHODS``
~~~~~~~~~~~~~~~~~~~~~~

A list of HTTP verbs that are allowed for the actual request. Defaults to:

.. code-block:: python

    CORS_ALLOW_METHODS = [
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
    ]

The default can be imported as ``corsheaders.defaults.default_methods`` so you
can just extend it with your custom methods. This allows you to keep up to date
with any future changes. For example:

.. code-block:: python

    from corsheaders.defaults import default_methods

    CORS_ALLOW_METHODS = list(default_methods) + [
        'POKE',
    ]

``CORS_ALLOW_HEADERS``
~~~~~~~~~~~~~~~~~~~~~~

The list of non-standard HTTP headers that can be used when making the actual
request. Defaults to:

.. code-block:: python

    CORS_ALLOW_HEADERS = [
        'accept',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
    ]

The default can be imported as ``corsheaders.defaults.default_headers`` so you
can extend it with your custom headers. This allows you to keep up to date with
any future changes. For example:

.. code-block:: python

    from corsheaders.defaults import default_headers

    CORS_ALLOW_HEADERS = list(default_headers) + [
        'my-custom-header',
    ]

``CORS_EXPOSE_HEADERS``
~~~~~~~~~~~~~~~~~~~~~~~

The list of HTTP headers that are to be exposed to the browser. Defaults to
``[]``.


``CORS_PREFLIGHT_MAX_AGE``
~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of seconds a client/browser can cache the preflight response. If
this is 0 (or any falsey value), no max age header will be sent. Defaults to
``86400`` (one day).


**Note:** A preflight request is an extra request that is made when making a
"not-so-simple" request (e.g. ``Content-Type`` is not
``application/x-www-form-urlencoded``) to determine what requests the server
actually accepts. Read more about it in the
`CORS MDN article <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#Preflighted_requests>`_.

``CORS_ALLOW_CREDENTIALS``
~~~~~~~~~~~~~~~~~~~~~~~~~~

If ``True``, cookies will be allowed to be included in cross-site HTTP
requests. Defaults to ``False``.

Note: in Django 2.1 the `SESSION_COOKIE_SAMESITE`_ setting was added, set to
``'Lax'`` by default, which will prevent Django's session cookie being sent
cross-domain. Change it to ``None`` to bypass this security restriction.

.. _SESSION_COOKIE_SAMESITE: https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-SESSION_COOKIE_SAMESITE

CSRF Integration
----------------

Most sites will need to take advantage of the `Cross-Site Request Forgery
protection <https://docs.djangoproject.com/en/dev/ref/csrf/>`_ that Django
offers. CORS and CSRF are separate, and Django has no way of using your CORS
configuration to exempt sites from the ``Referer`` checking that it does on
secure requests. The way to do that is with its `CSRF_TRUSTED_ORIGINS setting
<https://docs.djangoproject.com/en/dev/ref/settings/#csrf-trusted-origins>`_.
For example:

.. code-block:: python

    CORS_ORIGIN_WHITELIST = [
        'http://read.only.com',
        'http://change.allowed.com',
    ]

    CSRF_TRUSTED_ORIGINS = [
        'change.allowed.com',
    ]

``CORS_REPLACE_HTTPS_REFERER``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``CSRF_TRUSTED_ORIGINS`` was introduced in Django 1.9, so users of earlier
versions will need an alternate solution. If ``CORS_REPLACE_HTTPS_REFERER`` is
``True``, ``CorsMiddleware`` will change the ``Referer`` header to something
that will pass Django's CSRF checks whenever the CORS checks pass. Defaults to
``False``.

Note that unlike ``CSRF_TRUSTED_ORIGINS``, this setting does not allow you to
distinguish between domains that are trusted to *read* resources by CORS and
domains that are trusted to *change* resources by avoiding CSRF protection.

With this feature enabled you should also add
``corsheaders.middleware.CorsPostCsrfMiddleware`` after
``django.middleware.csrf.CsrfViewMiddleware`` in your ``MIDDLEWARE_CLASSES`` to
undo the ``Referer`` replacement:

.. code-block:: python

    MIDDLEWARE_CLASSES = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        ...
        'django.middleware.csrf.CsrfViewMiddleware',
        'corsheaders.middleware.CorsPostCsrfMiddleware',
        ...
    ]

Signals
-------

If you have a use case that requires more than just the above configuration,
you can attach code to check if a given request should be allowed. For example,
this can be used to read the list of origins you allow from a model. Attach any
number of handlers to the ``check_request_enabled``
`Django signal <https://docs.djangoproject.com/en/1.10/ref/signals/>`_, which
provides the ``request`` argument (use ``**kwargs`` in your handler to protect
against any future arguments being added). If any handler attached to the
signal returns a truthy value, the request will be allowed.

For example you might define a handler like this:

.. code-block:: python

    # myapp/handlers.py
    from corsheaders.signals import check_request_enabled

    from myapp.models import MySite

    def cors_allow_mysites(sender, request, **kwargs):
        return MySite.objects.filter(host=request.host).exists()

    check_request_enabled.connect(cors_allow_mysites)

Then connect it at app ready time using a `Django AppConfig
<https://docs.djangoproject.com/en/1.10/ref/applications/>`_:

.. code-block:: python

    # myapp/__init__.py

    default_app_config = 'myapp.apps.MyAppConfig'

.. code-block:: python

    # myapp/apps.py

    from django.apps import AppConfig

    class MyAppConfig(AppConfig):
        name = 'myapp'

        def ready(self):
            # Makes sure all signal handlers are connected
            from myapp import handlers  # noqa

A common use case for the signal is to allow *all* origins to access a subset
of URL's, whilst allowing a normal set of origins to access *all* URL's. This
isn't possible using just the normal configuration, but it can be achieved with
a signal handler.

First set ``CORS_ORIGIN_WHITELIST`` to the list of trusted origins that are
allowed to access every URL, and then add a handler to
``check_request_enabled`` to allow CORS regardless of the origin for the
unrestricted URL's. For example:

.. code-block:: python

    # myapp/handlers.py
    from corsheaders.signals import check_request_enabled

    def cors_allow_api_to_everyone(sender, request, **kwargs):
        return request.path.startswith('/api/')

    check_request_enabled.connect(cors_allow_api_to_everyone)

History
=======

3.2.0 (2019-11-15)
------------------

* Converted setuptools metadata to configuration file. This meant removing the
  ``__version__`` attribute from the package. If you want to inspect the
  installed version, use
  ``importlib.metadata.version("django-cors-headers")``
  (`docs <https://docs.python.org/3.8/library/importlib.metadata.html#distribution-versions>`__ /
  `backport <https://pypi.org/project/importlib-metadata/>`__).
* Support Python 3.8.

3.1.1 (2019-09-30)
------------------

* Support the value `file://` for origins, which is accidentally sent by some
  versions of Chrome on Android.

3.1.0 (2019-08-13)
------------------

* Drop Python 2 support, only Python 3.5-3.7 is supported now.
* Fix all links for move from ``github.com/ottoyiu/django-cors-headers`` to
  ``github.com/adamchainz/django-cors-headers``.

3.0.2 (2019-05-28)
------------------

* Add a hint to the ``corsheaders.E013`` check to make it more obvious how to
  resolve it.

3.0.1 (2019-05-13)
------------------

* Allow 'null' in ``CORS_ORIGIN_WHITELIST`` check.

3.0.0 (2019-05-10)
------------------

* ``CORS_ORIGIN_WHITELIST`` now requires URI schemes, and optionally ports.
  This is part of the CORS specification
  (`Section 3.2 <https://tools.ietf.org/html/rfc6454#section-3.2>`_) that was
  not implemented in this library, except from with the
  ``CORS_ORIGIN_REGEX_WHITELIST`` setting. It fixes a security issue where the
  CORS middleware would allow requests between schemes, for example from
  insecure ``http://`` Origins to a secure ``https://`` site.

  You will need to update your whitelist to include schemes, for example from
  this:

  .. code-block:: python

      CORS_ORIGIN_WHITELIST = ['example.com']

  ...to this:

  .. code-block:: python

      CORS_ORIGIN_WHITELIST = ['https://example.com']

* Removed the ``CORS_MODEL`` setting, and associated class. It seems very few,
  or no users were using it, since there were no bug reports since its move to
  abstract in version 2.0.0 (2017-01-07). If you *are* using this
  functionality, you can continue by changing your model to not inherit from
  the abstract one, and add a signal handler for ``check_request_enabled`` that
  reads from your model. Note you'll need to handle the move to include schemes
  for Origins.

2.5.3 (2019-04-28)
------------------

* Tested on Django 2.2. No changes were needed for compatibility.
* Tested on Python 3.7. No changes were needed for compatibility.

2.5.2 (2019-03-15)
------------------

* Improve inclusion of tests in ``sdist`` to ignore ``.pyc`` files.

2.5.1 (2019-03-13)
------------------

* Include test infrastructure in ``sdist`` to allow consumers to use it.

2.5.0 (2019-03-05)
------------------

* Drop Django 1.8, 1.9, and 1.10 support. Only Django 1.11+ is supported now.

2.4.1 (2019-02-28)
------------------

* Fix ``DeprecationWarning`` from importing ``collections.abc.Sequence`` on
  Python 3.7.

2.4.0 (2018-07-18)
------------------

* Always add 'Origin' to the 'Vary' header for responses to enabled URL's,
  to prevent caching of responses intended for one origin being served for
  another.

2.3.0 (2018-06-27)
------------------

* Match ``CORS_URLS_REGEX`` to ``request.path_info`` instead of
  ``request.path``, so the patterns can work without knowing the site's path
  prefix at configuration time.

2.2.1 (2018-06-27)
------------------

* Add ``Content-Length`` header to CORS preflight requests. This fixes issues
  with some HTTP proxies and servers, e.g. AWS Elastic Beanstalk.

2.2.0 (2018-02-28)
------------------

* Django 2.0 compatibility. Again there were no changes to the actual library
  code, so previous versions probably work.
* Ensured that ``request._cors_enabled`` is always a ``bool()`` - previously it
  could be set to a regex match object.

2.1.0 (2017-05-28)
------------------

* Django 1.11 compatibility. There were no changes to the actual library code,
  so previous versions probably work, though they weren't properly tested on
  1.11.

2.0.2 (2017-02-06)
------------------

* Fix when the check for ``CORS_MODEL`` is done to allow it to properly add
  the headers and respond to ``OPTIONS`` requests.

2.0.1 (2017-01-29)
------------------

* Add support for specifying 'null' in ``CORS_ORIGIN_WHITELIST``.

2.0.0 (2017-01-07)
------------------

* Remove previously undocumented ``CorsModel`` as it was causing migration
  issues. For backwards compatibility, any users previously using ``CorsModel``
  should create a model in their own app that inherits from the new
  ``AbstractCorsModel``, and to keep using the same data, set the model's
  ``db_table`` to 'corsheaders_corsmodel'. Users not using ``CorsModel``
  will find they have an unused table that they can drop.
* Make sure that ``Access-Control-Allow-Credentials`` is in the response if the
  client asks for it.

1.3.1 (2016-11-09)
------------------

* Fix a bug with the single check if CORS enabled added in 1.3.0: on Django
  < 1.10 shortcut responses could be generated by middleware above
  ``CorsMiddleware``, before it processed the request, failing with an
  ``AttributeError`` for ``request._cors_enabled``. Also clarified the docs
  that ``CorsMiddleware`` should be kept as high as possible in your middleware
  stack, above any middleware that can generate such responses.

1.3.0 (2016-11-06)
------------------

* Add checks to validate the types of the settings.
* Add the 'Do Not Track' header ``'DNT'`` to the default for
  ``CORS_ALLOW_HEADERS``.
* Add 'Origin' to the 'Vary' header of outgoing requests when not allowing all
  origins, as per the CORS spec. Note this changes the way HTTP caching works
  with your CORS-enabled responses.
* Check whether CORS should be enabled on a request only once. This has had a
  minor change on the conditions where any custom signals will be called -
  signals will now always be called *before* ``HTTP_REFERER`` gets replaced,
  whereas before they could be called before and after. Also this attaches the
  attribute ``_cors_enabled`` to ``request`` - please take care that other
  code you're running does not remove it.

1.2.2 (2016-10-05)
------------------

* Add ``CorsModel.__str__`` for human-readable text
* Add a signal that allows you to add code for more intricate control over when
  CORS headers are added.

1.2.1 (2016-09-30)
------------------

* Made settings dynamically respond to changes, and which allows you to import
  the defaults for headers and methods in order to extend them.

1.2.0 (2016-09-28)
------------------

* Drop Python 2.6 support.
* Drop Django 1.3-1.7 support, as they are no longer supported.
* Confirmed Django 1.9 support (no changes outside of tests were necessary).
* Added Django 1.10 support.
* Package as a universal wheel.

1.1.0 (2014-12-15)
------------------

* django-cors-header now supports Django 1.8 with its new application loading
  system! Thanks @jpadilla for making this possible and sorry for the delay in
  making a release.

1.0.0 (2014-12-13)
------------------

django-cors-headers is all grown-up :) Since it's been used in production for
many many deployments, I think it's time we mark this as a stable release.

* Switching this middleware versioning over to semantic versioning
* #46 add user-agent and accept-encoding default headers
* #45 pep-8 this big boy up

0.13 (2014-08-14)
-----------------

* Add support for Python 3
* Updated tests
* Improved documentation
* Small bugfixes

0.12 (2013-09-24)
-----------------

* Added an option to selectively enable CORS only for specific URLs

0.11 (2013-09-24)

* Added the ability to specify a regex for whitelisting many origin hostnames
  at once

0.10 (2013-09-05)
-----------------

* Introduced port distinction for origin checking
* Use ``urlparse`` for Python 3 support
* Added testcases to project

0.06 (2013-02-18)
-----------------

* Add support for exposed response headers

0.05 (2013-01-26)
-----------------

* Fixed middleware to ensure correct response for CORS preflight requests

0.04 (2013-01-25)
-----------------

* Add ``Access-Control-Allow-Credentials`` control to simple requests

0.03 (2013-01-22)
-----------------

* Bugfix to repair mismatched default variable names

0.02 (2013-01-19)
-----------------

* Refactor/pull defaults into separate file

0.01 (2013-01-19)
-----------------

* Initial release




%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        3.2.0
Release:        0%{?dist}
Url:            https://github.com/adamchainz/django-cors-headers
Summary:        django-cors-headers is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# requires stanza of py2pack
# install_requires stanza of py2pack
%if %{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
django-cors-headers
===================

.. image:: https://travis-ci.org/adamchainz/django-cors-headers.svg?branch=master
   :target: https://travis-ci.org/adamchainz/django-cors-headers

.. image:: https://img.shields.io/pypi/v/django-cors-headers.svg
    :target: https://pypi.python.org/pypi/django-cors-headers/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/python/black

A Django App that adds Cross-Origin Resource Sharing (CORS) headers to
responses. This allows in-browser requests to your Django application from
other origins.

About CORS
----------

Adding CORS headers allows your resources to be accessed on other domains. It's
important you understand the implications before adding the headers, since you
could be unintentionally opening up your site's private data to others.

Some good resources to read on the subject are:

* The `Wikipedia Page <https://en.m.wikipedia.org/wiki/Cross-origin_resource_sharing>`_
* The `MDN Article <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS>`_
* The `HTML5 Rocks Tutorial <https://www.html5rocks.com/en/tutorials/cors/>`_

Requirements
------------

Python 3.5-3.8 supported.

Django 1.11-3.0 suppported.

Setup
-----

Install from **pip**:

.. code-block:: sh

    pip install django-cors-headers

and then add it to your installed apps:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'corsheaders',
        ...
    ]

You will also need to add a middleware class to listen in on responses:

.. code-block:: python

    MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]

``CorsMiddleware`` should be placed as high as possible, especially before any
middleware that can generate responses such as Django's ``CommonMiddleware`` or
Whitenoise's ``WhiteNoiseMiddleware``. If it is not before, it will not be able
to add the CORS headers to these responses.

Also if you are using ``CORS_REPLACE_HTTPS_REFERER`` it should be placed before
Django's ``CsrfViewMiddleware`` (see more below).

About
-----

**django-cors-headers** was created in January 2013 by Otto Yiu. It went
unmaintained from August 2015 and was forked in January 2016 to the package
`django-cors-middleware <https://github.com/zestedesavoir/django-cors-middleware>`_
by Laville Augustin at Zeste de Savoir.
In September 2016, Adam Johnson, Ed Morley, and others gained maintenance
responsibility for **django-cors-headers**
(`Issue 110 <https://github.com/adamchainz/django-cors-headers/issues/110>`__)
from Otto Yiu.
Basically all of the changes in the forked **django-cors-middleware** were
merged back, or re-implemented in a different way, so it should be possible to
switch back. If there's a feature that hasn't been merged, please open an issue
about it.

**django-cors-headers** has had `40+ contributors
<https://github.com/adamchainz/django-cors-headers/graphs/contributors>`__
in its time; thanks to every one of them.

Configuration
-------------

Configure the middleware's behaviour in your Django settings. You must add the
hosts that are allowed to do cross-site requests to
``CORS_ORIGIN_WHITELIST``, or set ``CORS_ORIGIN_ALLOW_ALL`` to ``True``
to allow all hosts.

``CORS_ORIGIN_ALLOW_ALL``
~~~~~~~~~~~~~~~~~~~~~~~~~
If ``True``, the whitelist will not be used and all origins will be accepted.
Defaults to ``False``.

``CORS_ORIGIN_WHITELIST``
~~~~~~~~~~~~~~~~~~~~~~~~~

A list of origins that are authorized to make cross-site HTTP requests.
Defaults to ``[]``.

An Origin is defined by
`the CORS RFC Section 3.2 <https://tools.ietf.org/html/rfc6454#section-3.2>`_
as a URI scheme + hostname + port, or one of the special values `'null'` or
`'file://'`.
Default ports (HTTPS = 443, HTTP = 80) are optional here.

The special value `null` is sent by the browser in
`"privacy-sensitive contexts" <https://tools.ietf.org/html/rfc6454#section-6>`__,
such as when the client is running from a ``file://`` domain.
The special value `file://` is sent accidentally by some versions of Chrome on
Android as per `this bug <https://bugs.chromium.org/p/chromium/issues/detail?id=991107>`__.

Example:

.. code-block:: python

    CORS_ORIGIN_WHITELIST = [
        "https://example.com",
        "https://sub.example.com",
        "http://localhost:8080",
        "http://127.0.0.1:9000"
    ]


``CORS_ORIGIN_REGEX_WHITELIST``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A list of strings representing regexes that match Origins that are authorized
to make cross-site HTTP requests. Defaults to ``[]``. Useful when
``CORS_ORIGIN_WHITELIST`` is impractical, such as when you have a large number
of subdomains.

Example:

.. code-block:: python

    CORS_ORIGIN_REGEX_WHITELIST = [
        r"^https://\w+\.example\.com$",
    ]

--------------

The following are optional settings, for which the defaults probably suffice.

``CORS_URLS_REGEX``
~~~~~~~~~~~~~~~~~~~

A regex which restricts the URL's for which the CORS headers will be sent.
Defaults to ``r'^.*$'``, i.e. match all URL's. Useful when you only need CORS
on a part of your site, e.g. an API at ``/api/``.

Example:

.. code-block:: python

    CORS_URLS_REGEX = r'^/api/.*$'

``CORS_ALLOW_METHODS``
~~~~~~~~~~~~~~~~~~~~~~

A list of HTTP verbs that are allowed for the actual request. Defaults to:

.. code-block:: python

    CORS_ALLOW_METHODS = [
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
    ]

The default can be imported as ``corsheaders.defaults.default_methods`` so you
can just extend it with your custom methods. This allows you to keep up to date
with any future changes. For example:

.. code-block:: python

    from corsheaders.defaults import default_methods

    CORS_ALLOW_METHODS = list(default_methods) + [
        'POKE',
    ]

``CORS_ALLOW_HEADERS``
~~~~~~~~~~~~~~~~~~~~~~

The list of non-standard HTTP headers that can be used when making the actual
request. Defaults to:

.. code-block:: python

    CORS_ALLOW_HEADERS = [
        'accept',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
    ]

The default can be imported as ``corsheaders.defaults.default_headers`` so you
can extend it with your custom headers. This allows you to keep up to date with
any future changes. For example:

.. code-block:: python

    from corsheaders.defaults import default_headers

    CORS_ALLOW_HEADERS = list(default_headers) + [
        'my-custom-header',
    ]

``CORS_EXPOSE_HEADERS``
~~~~~~~~~~~~~~~~~~~~~~~

The list of HTTP headers that are to be exposed to the browser. Defaults to
``[]``.


``CORS_PREFLIGHT_MAX_AGE``
~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of seconds a client/browser can cache the preflight response. If
this is 0 (or any falsey value), no max age header will be sent. Defaults to
``86400`` (one day).


**Note:** A preflight request is an extra request that is made when making a
"not-so-simple" request (e.g. ``Content-Type`` is not
``application/x-www-form-urlencoded``) to determine what requests the server
actually accepts. Read more about it in the
`CORS MDN article <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#Preflighted_requests>`_.

``CORS_ALLOW_CREDENTIALS``
~~~~~~~~~~~~~~~~~~~~~~~~~~

If ``True``, cookies will be allowed to be included in cross-site HTTP
requests. Defaults to ``False``.

Note: in Django 2.1 the `SESSION_COOKIE_SAMESITE`_ setting was added, set to
``'Lax'`` by default, which will prevent Django's session cookie being sent
cross-domain. Change it to ``None`` to bypass this security restriction.

.. _SESSION_COOKIE_SAMESITE: https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-SESSION_COOKIE_SAMESITE

CSRF Integration
----------------

Most sites will need to take advantage of the `Cross-Site Request Forgery
protection <https://docs.djangoproject.com/en/dev/ref/csrf/>`_ that Django
offers. CORS and CSRF are separate, and Django has no way of using your CORS
configuration to exempt sites from the ``Referer`` checking that it does on
secure requests. The way to do that is with its `CSRF_TRUSTED_ORIGINS setting
<https://docs.djangoproject.com/en/dev/ref/settings/#csrf-trusted-origins>`_.
For example:

.. code-block:: python

    CORS_ORIGIN_WHITELIST = [
        'http://read.only.com',
        'http://change.allowed.com',
    ]

    CSRF_TRUSTED_ORIGINS = [
        'change.allowed.com',
    ]

``CORS_REPLACE_HTTPS_REFERER``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``CSRF_TRUSTED_ORIGINS`` was introduced in Django 1.9, so users of earlier
versions will need an alternate solution. If ``CORS_REPLACE_HTTPS_REFERER`` is
``True``, ``CorsMiddleware`` will change the ``Referer`` header to something
that will pass Django's CSRF checks whenever the CORS checks pass. Defaults to
``False``.

Note that unlike ``CSRF_TRUSTED_ORIGINS``, this setting does not allow you to
distinguish between domains that are trusted to *read* resources by CORS and
domains that are trusted to *change* resources by avoiding CSRF protection.

With this feature enabled you should also add
``corsheaders.middleware.CorsPostCsrfMiddleware`` after
``django.middleware.csrf.CsrfViewMiddleware`` in your ``MIDDLEWARE_CLASSES`` to
undo the ``Referer`` replacement:

.. code-block:: python

    MIDDLEWARE_CLASSES = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        ...
        'django.middleware.csrf.CsrfViewMiddleware',
        'corsheaders.middleware.CorsPostCsrfMiddleware',
        ...
    ]

Signals
-------

If you have a use case that requires more than just the above configuration,
you can attach code to check if a given request should be allowed. For example,
this can be used to read the list of origins you allow from a model. Attach any
number of handlers to the ``check_request_enabled``
`Django signal <https://docs.djangoproject.com/en/1.10/ref/signals/>`_, which
provides the ``request`` argument (use ``**kwargs`` in your handler to protect
against any future arguments being added). If any handler attached to the
signal returns a truthy value, the request will be allowed.

For example you might define a handler like this:

.. code-block:: python

    # myapp/handlers.py
    from corsheaders.signals import check_request_enabled

    from myapp.models import MySite

    def cors_allow_mysites(sender, request, **kwargs):
        return MySite.objects.filter(host=request.host).exists()

    check_request_enabled.connect(cors_allow_mysites)

Then connect it at app ready time using a `Django AppConfig
<https://docs.djangoproject.com/en/1.10/ref/applications/>`_:

.. code-block:: python

    # myapp/__init__.py

    default_app_config = 'myapp.apps.MyAppConfig'

.. code-block:: python

    # myapp/apps.py

    from django.apps import AppConfig

    class MyAppConfig(AppConfig):
        name = 'myapp'

        def ready(self):
            # Makes sure all signal handlers are connected
            from myapp import handlers  # noqa

A common use case for the signal is to allow *all* origins to access a subset
of URL's, whilst allowing a normal set of origins to access *all* URL's. This
isn't possible using just the normal configuration, but it can be achieved with
a signal handler.

First set ``CORS_ORIGIN_WHITELIST`` to the list of trusted origins that are
allowed to access every URL, and then add a handler to
``check_request_enabled`` to allow CORS regardless of the origin for the
unrestricted URL's. For example:

.. code-block:: python

    # myapp/handlers.py
    from corsheaders.signals import check_request_enabled

    def cors_allow_api_to_everyone(sender, request, **kwargs):
        return request.path.startswith('/api/')

    check_request_enabled.connect(cors_allow_api_to_everyone)

History
=======

3.2.0 (2019-11-15)
------------------

* Converted setuptools metadata to configuration file. This meant removing the
  ``__version__`` attribute from the package. If you want to inspect the
  installed version, use
  ``importlib.metadata.version("django-cors-headers")``
  (`docs <https://docs.python.org/3.8/library/importlib.metadata.html#distribution-versions>`__ /
  `backport <https://pypi.org/project/importlib-metadata/>`__).
* Support Python 3.8.

3.1.1 (2019-09-30)
------------------

* Support the value `file://` for origins, which is accidentally sent by some
  versions of Chrome on Android.

3.1.0 (2019-08-13)
------------------

* Drop Python 2 support, only Python 3.5-3.7 is supported now.
* Fix all links for move from ``github.com/ottoyiu/django-cors-headers`` to
  ``github.com/adamchainz/django-cors-headers``.

3.0.2 (2019-05-28)
------------------

* Add a hint to the ``corsheaders.E013`` check to make it more obvious how to
  resolve it.

3.0.1 (2019-05-13)
------------------

* Allow 'null' in ``CORS_ORIGIN_WHITELIST`` check.

3.0.0 (2019-05-10)
------------------

* ``CORS_ORIGIN_WHITELIST`` now requires URI schemes, and optionally ports.
  This is part of the CORS specification
  (`Section 3.2 <https://tools.ietf.org/html/rfc6454#section-3.2>`_) that was
  not implemented in this library, except from with the
  ``CORS_ORIGIN_REGEX_WHITELIST`` setting. It fixes a security issue where the
  CORS middleware would allow requests between schemes, for example from
  insecure ``http://`` Origins to a secure ``https://`` site.

  You will need to update your whitelist to include schemes, for example from
  this:

  .. code-block:: python

      CORS_ORIGIN_WHITELIST = ['example.com']

  ...to this:

  .. code-block:: python

      CORS_ORIGIN_WHITELIST = ['https://example.com']

* Removed the ``CORS_MODEL`` setting, and associated class. It seems very few,
  or no users were using it, since there were no bug reports since its move to
  abstract in version 2.0.0 (2017-01-07). If you *are* using this
  functionality, you can continue by changing your model to not inherit from
  the abstract one, and add a signal handler for ``check_request_enabled`` that
  reads from your model. Note you'll need to handle the move to include schemes
  for Origins.

2.5.3 (2019-04-28)
------------------

* Tested on Django 2.2. No changes were needed for compatibility.
* Tested on Python 3.7. No changes were needed for compatibility.

2.5.2 (2019-03-15)
------------------

* Improve inclusion of tests in ``sdist`` to ignore ``.pyc`` files.

2.5.1 (2019-03-13)
------------------

* Include test infrastructure in ``sdist`` to allow consumers to use it.

2.5.0 (2019-03-05)
------------------

* Drop Django 1.8, 1.9, and 1.10 support. Only Django 1.11+ is supported now.

2.4.1 (2019-02-28)
------------------

* Fix ``DeprecationWarning`` from importing ``collections.abc.Sequence`` on
  Python 3.7.

2.4.0 (2018-07-18)
------------------

* Always add 'Origin' to the 'Vary' header for responses to enabled URL's,
  to prevent caching of responses intended for one origin being served for
  another.

2.3.0 (2018-06-27)
------------------

* Match ``CORS_URLS_REGEX`` to ``request.path_info`` instead of
  ``request.path``, so the patterns can work without knowing the site's path
  prefix at configuration time.

2.2.1 (2018-06-27)
------------------

* Add ``Content-Length`` header to CORS preflight requests. This fixes issues
  with some HTTP proxies and servers, e.g. AWS Elastic Beanstalk.

2.2.0 (2018-02-28)
------------------

* Django 2.0 compatibility. Again there were no changes to the actual library
  code, so previous versions probably work.
* Ensured that ``request._cors_enabled`` is always a ``bool()`` - previously it
  could be set to a regex match object.

2.1.0 (2017-05-28)
------------------

* Django 1.11 compatibility. There were no changes to the actual library code,
  so previous versions probably work, though they weren't properly tested on
  1.11.

2.0.2 (2017-02-06)
------------------

* Fix when the check for ``CORS_MODEL`` is done to allow it to properly add
  the headers and respond to ``OPTIONS`` requests.

2.0.1 (2017-01-29)
------------------

* Add support for specifying 'null' in ``CORS_ORIGIN_WHITELIST``.

2.0.0 (2017-01-07)
------------------

* Remove previously undocumented ``CorsModel`` as it was causing migration
  issues. For backwards compatibility, any users previously using ``CorsModel``
  should create a model in their own app that inherits from the new
  ``AbstractCorsModel``, and to keep using the same data, set the model's
  ``db_table`` to 'corsheaders_corsmodel'. Users not using ``CorsModel``
  will find they have an unused table that they can drop.
* Make sure that ``Access-Control-Allow-Credentials`` is in the response if the
  client asks for it.

1.3.1 (2016-11-09)
------------------

* Fix a bug with the single check if CORS enabled added in 1.3.0: on Django
  < 1.10 shortcut responses could be generated by middleware above
  ``CorsMiddleware``, before it processed the request, failing with an
  ``AttributeError`` for ``request._cors_enabled``. Also clarified the docs
  that ``CorsMiddleware`` should be kept as high as possible in your middleware
  stack, above any middleware that can generate such responses.

1.3.0 (2016-11-06)
------------------

* Add checks to validate the types of the settings.
* Add the 'Do Not Track' header ``'DNT'`` to the default for
  ``CORS_ALLOW_HEADERS``.
* Add 'Origin' to the 'Vary' header of outgoing requests when not allowing all
  origins, as per the CORS spec. Note this changes the way HTTP caching works
  with your CORS-enabled responses.
* Check whether CORS should be enabled on a request only once. This has had a
  minor change on the conditions where any custom signals will be called -
  signals will now always be called *before* ``HTTP_REFERER`` gets replaced,
  whereas before they could be called before and after. Also this attaches the
  attribute ``_cors_enabled`` to ``request`` - please take care that other
  code you're running does not remove it.

1.2.2 (2016-10-05)
------------------

* Add ``CorsModel.__str__`` for human-readable text
* Add a signal that allows you to add code for more intricate control over when
  CORS headers are added.

1.2.1 (2016-09-30)
------------------

* Made settings dynamically respond to changes, and which allows you to import
  the defaults for headers and methods in order to extend them.

1.2.0 (2016-09-28)
------------------

* Drop Python 2.6 support.
* Drop Django 1.3-1.7 support, as they are no longer supported.
* Confirmed Django 1.9 support (no changes outside of tests were necessary).
* Added Django 1.10 support.
* Package as a universal wheel.

1.1.0 (2014-12-15)
------------------

* django-cors-header now supports Django 1.8 with its new application loading
  system! Thanks @jpadilla for making this possible and sorry for the delay in
  making a release.

1.0.0 (2014-12-13)
------------------

django-cors-headers is all grown-up :) Since it's been used in production for
many many deployments, I think it's time we mark this as a stable release.

* Switching this middleware versioning over to semantic versioning
* #46 add user-agent and accept-encoding default headers
* #45 pep-8 this big boy up

0.13 (2014-08-14)
-----------------

* Add support for Python 3
* Updated tests
* Improved documentation
* Small bugfixes

0.12 (2013-09-24)
-----------------

* Added an option to selectively enable CORS only for specific URLs

0.11 (2013-09-24)

* Added the ability to specify a regex for whitelisting many origin hostnames
  at once

0.10 (2013-09-05)
-----------------

* Introduced port distinction for origin checking
* Use ``urlparse`` for Python 3 support
* Added testcases to project

0.06 (2013-02-18)
-----------------

* Add support for exposed response headers

0.05 (2013-01-26)
-----------------

* Fixed middleware to ensure correct response for CORS preflight requests

0.04 (2013-01-25)
-----------------

* Add ``Access-Control-Allow-Credentials`` control to simple requests

0.03 (2013-01-22)
-----------------

* Bugfix to repair mismatched default variable names

0.02 (2013-01-19)
-----------------

* Refactor/pull defaults into separate file

0.01 (2013-01-19)
-----------------

* Initial release




%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        3.2.0
Release:        0%{?dist}
Url:            https://github.com/adamchainz/django-cors-headers
Summary:        django-cors-headers is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# requires stanza of py2pack
# install_requires stanza of py2pack
%if %{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
django-cors-headers
===================

.. image:: https://travis-ci.org/adamchainz/django-cors-headers.svg?branch=master
   :target: https://travis-ci.org/adamchainz/django-cors-headers

.. image:: https://img.shields.io/pypi/v/django-cors-headers.svg
    :target: https://pypi.python.org/pypi/django-cors-headers/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/python/black

A Django App that adds Cross-Origin Resource Sharing (CORS) headers to
responses. This allows in-browser requests to your Django application from
other origins.

About CORS
----------

Adding CORS headers allows your resources to be accessed on other domains. It's
important you understand the implications before adding the headers, since you
could be unintentionally opening up your site's private data to others.

Some good resources to read on the subject are:

* The `Wikipedia Page <https://en.m.wikipedia.org/wiki/Cross-origin_resource_sharing>`_
* The `MDN Article <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS>`_
* The `HTML5 Rocks Tutorial <https://www.html5rocks.com/en/tutorials/cors/>`_

Requirements
------------

Python 3.5-3.8 supported.

Django 1.11-3.0 suppported.

Setup
-----

Install from **pip**:

.. code-block:: sh

    pip install django-cors-headers

and then add it to your installed apps:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'corsheaders',
        ...
    ]

You will also need to add a middleware class to listen in on responses:

.. code-block:: python

    MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]

``CorsMiddleware`` should be placed as high as possible, especially before any
middleware that can generate responses such as Django's ``CommonMiddleware`` or
Whitenoise's ``WhiteNoiseMiddleware``. If it is not before, it will not be able
to add the CORS headers to these responses.

Also if you are using ``CORS_REPLACE_HTTPS_REFERER`` it should be placed before
Django's ``CsrfViewMiddleware`` (see more below).

About
-----

**django-cors-headers** was created in January 2013 by Otto Yiu. It went
unmaintained from August 2015 and was forked in January 2016 to the package
`django-cors-middleware <https://github.com/zestedesavoir/django-cors-middleware>`_
by Laville Augustin at Zeste de Savoir.
In September 2016, Adam Johnson, Ed Morley, and others gained maintenance
responsibility for **django-cors-headers**
(`Issue 110 <https://github.com/adamchainz/django-cors-headers/issues/110>`__)
from Otto Yiu.
Basically all of the changes in the forked **django-cors-middleware** were
merged back, or re-implemented in a different way, so it should be possible to
switch back. If there's a feature that hasn't been merged, please open an issue
about it.

**django-cors-headers** has had `40+ contributors
<https://github.com/adamchainz/django-cors-headers/graphs/contributors>`__
in its time; thanks to every one of them.

Configuration
-------------

Configure the middleware's behaviour in your Django settings. You must add the
hosts that are allowed to do cross-site requests to
``CORS_ORIGIN_WHITELIST``, or set ``CORS_ORIGIN_ALLOW_ALL`` to ``True``
to allow all hosts.

``CORS_ORIGIN_ALLOW_ALL``
~~~~~~~~~~~~~~~~~~~~~~~~~
If ``True``, the whitelist will not be used and all origins will be accepted.
Defaults to ``False``.

``CORS_ORIGIN_WHITELIST``
~~~~~~~~~~~~~~~~~~~~~~~~~

A list of origins that are authorized to make cross-site HTTP requests.
Defaults to ``[]``.

An Origin is defined by
`the CORS RFC Section 3.2 <https://tools.ietf.org/html/rfc6454#section-3.2>`_
as a URI scheme + hostname + port, or one of the special values `'null'` or
`'file://'`.
Default ports (HTTPS = 443, HTTP = 80) are optional here.

The special value `null` is sent by the browser in
`"privacy-sensitive contexts" <https://tools.ietf.org/html/rfc6454#section-6>`__,
such as when the client is running from a ``file://`` domain.
The special value `file://` is sent accidentally by some versions of Chrome on
Android as per `this bug <https://bugs.chromium.org/p/chromium/issues/detail?id=991107>`__.

Example:

.. code-block:: python

    CORS_ORIGIN_WHITELIST = [
        "https://example.com",
        "https://sub.example.com",
        "http://localhost:8080",
        "http://127.0.0.1:9000"
    ]


``CORS_ORIGIN_REGEX_WHITELIST``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A list of strings representing regexes that match Origins that are authorized
to make cross-site HTTP requests. Defaults to ``[]``. Useful when
``CORS_ORIGIN_WHITELIST`` is impractical, such as when you have a large number
of subdomains.

Example:

.. code-block:: python

    CORS_ORIGIN_REGEX_WHITELIST = [
        r"^https://\w+\.example\.com$",
    ]

--------------

The following are optional settings, for which the defaults probably suffice.

``CORS_URLS_REGEX``
~~~~~~~~~~~~~~~~~~~

A regex which restricts the URL's for which the CORS headers will be sent.
Defaults to ``r'^.*$'``, i.e. match all URL's. Useful when you only need CORS
on a part of your site, e.g. an API at ``/api/``.

Example:

.. code-block:: python

    CORS_URLS_REGEX = r'^/api/.*$'

``CORS_ALLOW_METHODS``
~~~~~~~~~~~~~~~~~~~~~~

A list of HTTP verbs that are allowed for the actual request. Defaults to:

.. code-block:: python

    CORS_ALLOW_METHODS = [
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
    ]

The default can be imported as ``corsheaders.defaults.default_methods`` so you
can just extend it with your custom methods. This allows you to keep up to date
with any future changes. For example:

.. code-block:: python

    from corsheaders.defaults import default_methods

    CORS_ALLOW_METHODS = list(default_methods) + [
        'POKE',
    ]

``CORS_ALLOW_HEADERS``
~~~~~~~~~~~~~~~~~~~~~~

The list of non-standard HTTP headers that can be used when making the actual
request. Defaults to:

.. code-block:: python

    CORS_ALLOW_HEADERS = [
        'accept',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
    ]

The default can be imported as ``corsheaders.defaults.default_headers`` so you
can extend it with your custom headers. This allows you to keep up to date with
any future changes. For example:

.. code-block:: python

    from corsheaders.defaults import default_headers

    CORS_ALLOW_HEADERS = list(default_headers) + [
        'my-custom-header',
    ]

``CORS_EXPOSE_HEADERS``
~~~~~~~~~~~~~~~~~~~~~~~

The list of HTTP headers that are to be exposed to the browser. Defaults to
``[]``.


``CORS_PREFLIGHT_MAX_AGE``
~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of seconds a client/browser can cache the preflight response. If
this is 0 (or any falsey value), no max age header will be sent. Defaults to
``86400`` (one day).


**Note:** A preflight request is an extra request that is made when making a
"not-so-simple" request (e.g. ``Content-Type`` is not
``application/x-www-form-urlencoded``) to determine what requests the server
actually accepts. Read more about it in the
`CORS MDN article <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#Preflighted_requests>`_.

``CORS_ALLOW_CREDENTIALS``
~~~~~~~~~~~~~~~~~~~~~~~~~~

If ``True``, cookies will be allowed to be included in cross-site HTTP
requests. Defaults to ``False``.

Note: in Django 2.1 the `SESSION_COOKIE_SAMESITE`_ setting was added, set to
``'Lax'`` by default, which will prevent Django's session cookie being sent
cross-domain. Change it to ``None`` to bypass this security restriction.

.. _SESSION_COOKIE_SAMESITE: https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-SESSION_COOKIE_SAMESITE

CSRF Integration
----------------

Most sites will need to take advantage of the `Cross-Site Request Forgery
protection <https://docs.djangoproject.com/en/dev/ref/csrf/>`_ that Django
offers. CORS and CSRF are separate, and Django has no way of using your CORS
configuration to exempt sites from the ``Referer`` checking that it does on
secure requests. The way to do that is with its `CSRF_TRUSTED_ORIGINS setting
<https://docs.djangoproject.com/en/dev/ref/settings/#csrf-trusted-origins>`_.
For example:

.. code-block:: python

    CORS_ORIGIN_WHITELIST = [
        'http://read.only.com',
        'http://change.allowed.com',
    ]

    CSRF_TRUSTED_ORIGINS = [
        'change.allowed.com',
    ]

``CORS_REPLACE_HTTPS_REFERER``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``CSRF_TRUSTED_ORIGINS`` was introduced in Django 1.9, so users of earlier
versions will need an alternate solution. If ``CORS_REPLACE_HTTPS_REFERER`` is
``True``, ``CorsMiddleware`` will change the ``Referer`` header to something
that will pass Django's CSRF checks whenever the CORS checks pass. Defaults to
``False``.

Note that unlike ``CSRF_TRUSTED_ORIGINS``, this setting does not allow you to
distinguish between domains that are trusted to *read* resources by CORS and
domains that are trusted to *change* resources by avoiding CSRF protection.

With this feature enabled you should also add
``corsheaders.middleware.CorsPostCsrfMiddleware`` after
``django.middleware.csrf.CsrfViewMiddleware`` in your ``MIDDLEWARE_CLASSES`` to
undo the ``Referer`` replacement:

.. code-block:: python

    MIDDLEWARE_CLASSES = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        ...
        'django.middleware.csrf.CsrfViewMiddleware',
        'corsheaders.middleware.CorsPostCsrfMiddleware',
        ...
    ]

Signals
-------

If you have a use case that requires more than just the above configuration,
you can attach code to check if a given request should be allowed. For example,
this can be used to read the list of origins you allow from a model. Attach any
number of handlers to the ``check_request_enabled``
`Django signal <https://docs.djangoproject.com/en/1.10/ref/signals/>`_, which
provides the ``request`` argument (use ``**kwargs`` in your handler to protect
against any future arguments being added). If any handler attached to the
signal returns a truthy value, the request will be allowed.

For example you might define a handler like this:

.. code-block:: python

    # myapp/handlers.py
    from corsheaders.signals import check_request_enabled

    from myapp.models import MySite

    def cors_allow_mysites(sender, request, **kwargs):
        return MySite.objects.filter(host=request.host).exists()

    check_request_enabled.connect(cors_allow_mysites)

Then connect it at app ready time using a `Django AppConfig
<https://docs.djangoproject.com/en/1.10/ref/applications/>`_:

.. code-block:: python

    # myapp/__init__.py

    default_app_config = 'myapp.apps.MyAppConfig'

.. code-block:: python

    # myapp/apps.py

    from django.apps import AppConfig

    class MyAppConfig(AppConfig):
        name = 'myapp'

        def ready(self):
            # Makes sure all signal handlers are connected
            from myapp import handlers  # noqa

A common use case for the signal is to allow *all* origins to access a subset
of URL's, whilst allowing a normal set of origins to access *all* URL's. This
isn't possible using just the normal configuration, but it can be achieved with
a signal handler.

First set ``CORS_ORIGIN_WHITELIST`` to the list of trusted origins that are
allowed to access every URL, and then add a handler to
``check_request_enabled`` to allow CORS regardless of the origin for the
unrestricted URL's. For example:

.. code-block:: python

    # myapp/handlers.py
    from corsheaders.signals import check_request_enabled

    def cors_allow_api_to_everyone(sender, request, **kwargs):
        return request.path.startswith('/api/')

    check_request_enabled.connect(cors_allow_api_to_everyone)

History
=======

3.2.0 (2019-11-15)
------------------

* Converted setuptools metadata to configuration file. This meant removing the
  ``__version__`` attribute from the package. If you want to inspect the
  installed version, use
  ``importlib.metadata.version("django-cors-headers")``
  (`docs <https://docs.python.org/3.8/library/importlib.metadata.html#distribution-versions>`__ /
  `backport <https://pypi.org/project/importlib-metadata/>`__).
* Support Python 3.8.

3.1.1 (2019-09-30)
------------------

* Support the value `file://` for origins, which is accidentally sent by some
  versions of Chrome on Android.

3.1.0 (2019-08-13)
------------------

* Drop Python 2 support, only Python 3.5-3.7 is supported now.
* Fix all links for move from ``github.com/ottoyiu/django-cors-headers`` to
  ``github.com/adamchainz/django-cors-headers``.

3.0.2 (2019-05-28)
------------------

* Add a hint to the ``corsheaders.E013`` check to make it more obvious how to
  resolve it.

3.0.1 (2019-05-13)
------------------

* Allow 'null' in ``CORS_ORIGIN_WHITELIST`` check.

3.0.0 (2019-05-10)
------------------

* ``CORS_ORIGIN_WHITELIST`` now requires URI schemes, and optionally ports.
  This is part of the CORS specification
  (`Section 3.2 <https://tools.ietf.org/html/rfc6454#section-3.2>`_) that was
  not implemented in this library, except from with the
  ``CORS_ORIGIN_REGEX_WHITELIST`` setting. It fixes a security issue where the
  CORS middleware would allow requests between schemes, for example from
  insecure ``http://`` Origins to a secure ``https://`` site.

  You will need to update your whitelist to include schemes, for example from
  this:

  .. code-block:: python

      CORS_ORIGIN_WHITELIST = ['example.com']

  ...to this:

  .. code-block:: python

      CORS_ORIGIN_WHITELIST = ['https://example.com']

* Removed the ``CORS_MODEL`` setting, and associated class. It seems very few,
  or no users were using it, since there were no bug reports since its move to
  abstract in version 2.0.0 (2017-01-07). If you *are* using this
  functionality, you can continue by changing your model to not inherit from
  the abstract one, and add a signal handler for ``check_request_enabled`` that
  reads from your model. Note you'll need to handle the move to include schemes
  for Origins.

2.5.3 (2019-04-28)
------------------

* Tested on Django 2.2. No changes were needed for compatibility.
* Tested on Python 3.7. No changes were needed for compatibility.

2.5.2 (2019-03-15)
------------------

* Improve inclusion of tests in ``sdist`` to ignore ``.pyc`` files.

2.5.1 (2019-03-13)
------------------

* Include test infrastructure in ``sdist`` to allow consumers to use it.

2.5.0 (2019-03-05)
------------------

* Drop Django 1.8, 1.9, and 1.10 support. Only Django 1.11+ is supported now.

2.4.1 (2019-02-28)
------------------

* Fix ``DeprecationWarning`` from importing ``collections.abc.Sequence`` on
  Python 3.7.

2.4.0 (2018-07-18)
------------------

* Always add 'Origin' to the 'Vary' header for responses to enabled URL's,
  to prevent caching of responses intended for one origin being served for
  another.

2.3.0 (2018-06-27)
------------------

* Match ``CORS_URLS_REGEX`` to ``request.path_info`` instead of
  ``request.path``, so the patterns can work without knowing the site's path
  prefix at configuration time.

2.2.1 (2018-06-27)
------------------

* Add ``Content-Length`` header to CORS preflight requests. This fixes issues
  with some HTTP proxies and servers, e.g. AWS Elastic Beanstalk.

2.2.0 (2018-02-28)
------------------

* Django 2.0 compatibility. Again there were no changes to the actual library
  code, so previous versions probably work.
* Ensured that ``request._cors_enabled`` is always a ``bool()`` - previously it
  could be set to a regex match object.

2.1.0 (2017-05-28)
------------------

* Django 1.11 compatibility. There were no changes to the actual library code,
  so previous versions probably work, though they weren't properly tested on
  1.11.

2.0.2 (2017-02-06)
------------------

* Fix when the check for ``CORS_MODEL`` is done to allow it to properly add
  the headers and respond to ``OPTIONS`` requests.

2.0.1 (2017-01-29)
------------------

* Add support for specifying 'null' in ``CORS_ORIGIN_WHITELIST``.

2.0.0 (2017-01-07)
------------------

* Remove previously undocumented ``CorsModel`` as it was causing migration
  issues. For backwards compatibility, any users previously using ``CorsModel``
  should create a model in their own app that inherits from the new
  ``AbstractCorsModel``, and to keep using the same data, set the model's
  ``db_table`` to 'corsheaders_corsmodel'. Users not using ``CorsModel``
  will find they have an unused table that they can drop.
* Make sure that ``Access-Control-Allow-Credentials`` is in the response if the
  client asks for it.

1.3.1 (2016-11-09)
------------------

* Fix a bug with the single check if CORS enabled added in 1.3.0: on Django
  < 1.10 shortcut responses could be generated by middleware above
  ``CorsMiddleware``, before it processed the request, failing with an
  ``AttributeError`` for ``request._cors_enabled``. Also clarified the docs
  that ``CorsMiddleware`` should be kept as high as possible in your middleware
  stack, above any middleware that can generate such responses.

1.3.0 (2016-11-06)
------------------

* Add checks to validate the types of the settings.
* Add the 'Do Not Track' header ``'DNT'`` to the default for
  ``CORS_ALLOW_HEADERS``.
* Add 'Origin' to the 'Vary' header of outgoing requests when not allowing all
  origins, as per the CORS spec. Note this changes the way HTTP caching works
  with your CORS-enabled responses.
* Check whether CORS should be enabled on a request only once. This has had a
  minor change on the conditions where any custom signals will be called -
  signals will now always be called *before* ``HTTP_REFERER`` gets replaced,
  whereas before they could be called before and after. Also this attaches the
  attribute ``_cors_enabled`` to ``request`` - please take care that other
  code you're running does not remove it.

1.2.2 (2016-10-05)
------------------

* Add ``CorsModel.__str__`` for human-readable text
* Add a signal that allows you to add code for more intricate control over when
  CORS headers are added.

1.2.1 (2016-09-30)
------------------

* Made settings dynamically respond to changes, and which allows you to import
  the defaults for headers and methods in order to extend them.

1.2.0 (2016-09-28)
------------------

* Drop Python 2.6 support.
* Drop Django 1.3-1.7 support, as they are no longer supported.
* Confirmed Django 1.9 support (no changes outside of tests were necessary).
* Added Django 1.10 support.
* Package as a universal wheel.

1.1.0 (2014-12-15)
------------------

* django-cors-header now supports Django 1.8 with its new application loading
  system! Thanks @jpadilla for making this possible and sorry for the delay in
  making a release.

1.0.0 (2014-12-13)
------------------

django-cors-headers is all grown-up :) Since it's been used in production for
many many deployments, I think it's time we mark this as a stable release.

* Switching this middleware versioning over to semantic versioning
* #46 add user-agent and accept-encoding default headers
* #45 pep-8 this big boy up

0.13 (2014-08-14)
-----------------

* Add support for Python 3
* Updated tests
* Improved documentation
* Small bugfixes

0.12 (2013-09-24)
-----------------

* Added an option to selectively enable CORS only for specific URLs

0.11 (2013-09-24)

* Added the ability to specify a regex for whitelisting many origin hostnames
  at once

0.10 (2013-09-05)
-----------------

* Introduced port distinction for origin checking
* Use ``urlparse`` for Python 3 support
* Added testcases to project

0.06 (2013-02-18)
-----------------

* Add support for exposed response headers

0.05 (2013-01-26)
-----------------

* Fixed middleware to ensure correct response for CORS preflight requests

0.04 (2013-01-25)
-----------------

* Add ``Access-Control-Allow-Credentials`` control to simple requests

0.03 (2013-01-22)
-----------------

* Bugfix to repair mismatched default variable names

0.02 (2013-01-19)
-----------------

* Refactor/pull defaults into separate file

0.01 (2013-01-19)
-----------------

* Initial release




%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with_python2}
%py2_build
%endif # with_python2

%if %{with_python3}
%py3_build
%endif # with_python3

%install
%if %{with_python2}
%py2_install
%endif # with_python2

%if %{with_python3}
%py3_install
%endif # with_python3

%clean
rm -rf %{buildroot}

%if %{with_python2}
%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%{python2_sitelib}/*
%endif # with_python2

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%endif # with_python3

%changelog