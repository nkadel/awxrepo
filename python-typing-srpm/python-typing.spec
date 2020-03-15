#
# spec file for package python-typing
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

%global with_python3 1

%global with_python2 0

%global pypi_name typing

# Common SRPM package
Name:           python-%{pypi_name}
Version:        3.7.4.1
Release:        0%{?dist}
Url:            https://docs.python.org/3/library/typing.html
Summary:        Type Hints for Python
License:        Python-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
Typing -- Type Hints for Python

This is a backport of the standard library typing module to Python
versions older than 3.5.  (See note below for newer versions.)

Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a
concise, standard format, and it has been designed to also be used by
static and runtime type checkers, static analyzers, IDEs and other
tools.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        3.7.4.1
Release:        0%{?dist}
Url:            https://docs.python.org/3/library/typing.html
Summary:        Type Hints for Python
License:        Python-2.0

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Typing -- Type Hints for Python

This is a backport of the standard library typing module to Python
versions older than 3.5.  (See note below for newer versions.)

Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a
concise, standard format, and it has been designed to also be used by
static and runtime type checkers, static analyzers, IDEs and other
tools.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        3.7.4.1
Release:        0%{?dist}
Url:            https://docs.python.org/3/library/typing.html
Summary:        Type Hints for Python
License:        Python-2.0

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Typing -- Type Hints for Python

This is a backport of the standard library typing module to Python
versions older than 3.5.  (See note below for newer versions.)

Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a
concise, standard format, and it has been designed to also be used by
static and runtime type checkers, static analyzers, IDEs and other
tools.

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
