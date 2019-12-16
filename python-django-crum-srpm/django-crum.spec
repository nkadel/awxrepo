#
# spec file for package python-django-crum
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

%global pypi_name django-crum

# Common SRPM package
Name:           python-%{pypi_name}
Version:        0.7.5
Release:        0%{?dist}
Url:            https://github.com/ninemoreminutes/django-crum/
Summary:        Django middleware to capture current request and user.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
Django-CRUM (Current Request User Middleware) captures the current request and
user in thread local storage.

It enables apps to check permissions, capture audit trails or otherwise access
the current request and user without requiring the request object to be passed
directly. It also offers a context manager to allow for temporarily
impersonating another user.

It provides a signal to extend the built-in function for getting the current
user, which could be helpful when using custom authentication methods or user
models.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        0.7.5
Release:        0%{?dist}
Url:            https://github.com/ninemoreminutes/django-crum/
Summary:        Django middleware to capture current request and user.
License:        BSD (FIXME:No SPDX)

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:	python2-pytest-runner
Requires:	python2-django >= 1.8
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Django-CRUM (Current Request User Middleware) captures the current request and
user in thread local storage.

It enables apps to check permissions, capture audit trails or otherwise access
the current request and user without requiring the request object to be passed
directly. It also offers a context manager to allow for temporarily
impersonating another user.

It provides a signal to extend the built-in function for getting the current
user, which could be helpful when using custom authentication methods or user
models.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        0.7.5
Release:        0%{?dist}
Url:            https://github.com/ninemoreminutes/django-crum/
Summary:        Django middleware to capture current request and user.
License:        BSD (FIXME:No SPDX)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:	python%{python3_pkgversion}-pytest-runner
Requires:	python%{python3_pkgversion}-django >= 1.8

%description -n python%{python3_pkgversion}-%{pypi_name}
Django-CRUM (Current Request User Middleware) captures the current request and
user in thread local storage.

It enables apps to check permissions, capture audit trails or otherwise access
the current request and user without requiring the request object to be passed
directly. It also offers a context manager to allow for temporarily
impersonating another user.

It provides a signal to extend the built-in function for getting the current
user, which could be helpful when using custom authentication methods or user
models.

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
