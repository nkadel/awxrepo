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
BuildRequires:  epel-rpm-macros
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

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        1.3.0
Release:        0%{?dist}
Url:            http://github.com/celery/vine
Summary:        Promises, promises, promises.
License:        BSD (FIXME:No SPDX)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

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
