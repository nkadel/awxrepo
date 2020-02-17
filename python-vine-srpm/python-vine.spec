#
# spec file for package python-vine
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

%global pypi_name vine

# Common SRPM package
Name:           python-%{pypi_name}
Version:        1.3.0
Release:        0%{?dist}
Url:            http://github.com/celery/vine
Summary:        Promises, promises, promises.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
=====================================================================
 vine - Python Promises
=====================================================================

|build-status| |coverage| |license| |wheel| |pyversion| |pyimp|

:Version: 1.3.0
:Web: https://vine.readthedocs.io/
:Download: https://pypi.org/project/vine/
:Source: http://github.com/celery/vine/
:Keywords: promise, async, future

About
=====


.. |build-status| image:: https://secure.travis-ci.org/celery/vine.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/celery/vine

.. |coverage| image:: https://codecov.io/github/celery/vine/coverage.svg?branch=master
    :target: https://codecov.io/github/celery/vine?branch=master

.. |license| image:: https://img.shields.io/pypi/l/vine.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/vine.svg
    :alt: Vine can be installed via wheel
    :target: https://pypi.org/project/vine/

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/vine.svg
    :alt: Supported Python versions.
    :target: https://pypi.org/project/vine/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/vine.svg
    :alt: Support Python implementations.
    :target: https://pypi.org/project/vine/


%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        1.3.0
Release:        0%{?dist}
Url:            http://github.com/celery/vine
Summary:        Promises, promises, promises.
License:        BSD (FIXME:No SPDX)

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
=====================================================================
 vine - Python Promises
=====================================================================

|build-status| |coverage| |license| |wheel| |pyversion| |pyimp|

:Version: 1.3.0
:Web: https://vine.readthedocs.io/
:Download: https://pypi.org/project/vine/
:Source: http://github.com/celery/vine/
:Keywords: promise, async, future

About
=====


.. |build-status| image:: https://secure.travis-ci.org/celery/vine.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/celery/vine

.. |coverage| image:: https://codecov.io/github/celery/vine/coverage.svg?branch=master
    :target: https://codecov.io/github/celery/vine?branch=master

.. |license| image:: https://img.shields.io/pypi/l/vine.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/vine.svg
    :alt: Vine can be installed via wheel
    :target: https://pypi.org/project/vine/

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/vine.svg
    :alt: Supported Python versions.
    :target: https://pypi.org/project/vine/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/vine.svg
    :alt: Support Python implementations.
    :target: https://pypi.org/project/vine/





%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        1.3.0
Release:        0%{?dist}
Url:            http://github.com/celery/vine
Summary:        Promises, promises, promises.
License:        BSD (FIXME:No SPDX)

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
=====================================================================
 vine - Python Promises
=====================================================================

|build-status| |coverage| |license| |wheel| |pyversion| |pyimp|

:Version: 1.3.0
:Web: https://vine.readthedocs.io/
:Download: https://pypi.org/project/vine/
:Source: http://github.com/celery/vine/
:Keywords: promise, async, future

About
=====


.. |build-status| image:: https://secure.travis-ci.org/celery/vine.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/celery/vine

.. |coverage| image:: https://codecov.io/github/celery/vine/coverage.svg?branch=master
    :target: https://codecov.io/github/celery/vine?branch=master

.. |license| image:: https://img.shields.io/pypi/l/vine.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/vine.svg
    :alt: Vine can be installed via wheel
    :target: https://pypi.org/project/vine/

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/vine.svg
    :alt: Supported Python versions.
    :target: https://pypi.org/project/vine/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/vine.svg
    :alt: Support Python implementations.
    :target: https://pypi.org/project/vine/





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
