#
# spec file for package python-contextvars
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

%global with_python2 0

%global pypi_name contextvars

# Common SRPM package
Name:           python-%{pypi_name}
Version:        2.4
Release:        0%{?dist}
Url:            http://github.com/MagicStack/contextvars
Summary:        PEP 567 Backport
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
PEP 567 Backport
================

This package implements a backport of Python 3.7 ``contextvars``
module (see PEP 567) for Python 3.6.

**Important:** at this moment this package does not provide an
asyncio event loop with PEP 567 support yet.  Stay tuned for updates.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        2.4
Release:        0%{?dist}
Url:            http://github.com/MagicStack/contextvars
Summary:        PEP 567 Backport
License:        Apache-2.0

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
PEP 567 Backport
================

This package implements a backport of Python 3.7 ``contextvars``
module (see PEP 567) for Python 3.6.

**Important:** at this moment this package does not provide an
asyncio event loop with PEP 567 support yet.  Stay tuned for updates.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        2.4
Release:        0%{?dist}
Url:            http://github.com/MagicStack/contextvars
Summary:        PEP 567 Backport
License:        Apache-2.0

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
PEP 567 Backport
================

This package implements a backport of Python 3.7 ``contextvars``
module (see PEP 567) for Python 3.6.

**Important:** at this moment this package does not provide an
asyncio event loop with PEP 567 support yet.  Stay tuned for updates.

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
