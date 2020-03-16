#
# spec file for package python-importlib-resources
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Enable only as needed
%global with_python2 0

%global pypi_name importlib_resources

# Common SRPM package
Name:           python-%{pypi_name}
Version:        1.3.1
Release:        0%{?dist}
Url:            http://importlib-resources.readthedocs.io/
Summary:        Read resources from Python packages
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires:  epel-rpm-macros
%endif

%description
``importlib_resources`` is a backport of Python standard library
`importlib.resources
<https://docs.python.org/3.9/library/importlib.html#module-importlib.resources>`_
module for Python 2.7, and 3.4 through 3.8.  Users of Python 3.9 and beyond
should use the standard library module, since for these versions,
``importlib_resources`` just delegates to that module.

The key goal of this module is to replace parts of `pkg_resources
<https://setuptools.readthedocs.io/en/latest/pkg_resources.html>`_ with a
solution in Python's stdlib that relies on well-defined APIs.  This makes
reading resources included in packages easier, with more stable and consistent
semantics.

%if %{with_python2}
%package -n python2-%{pypi_name}
Url:            http://importlib-resources.readthedocs.io/
Summary:        Read resources from Python packages
License:        Apache-2.0

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm >= 3.4.1
# Is this neeeded
BuildRequires:  python2-toml
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
``importlib_resources`` is a backport of Python standard library
`importlib.resources
<https://docs.python.org/3.9/library/importlib.html#module-importlib.resources>`_
module for Python 2.7, and 3.4 through 3.8.  Users of Python 3.9 and beyond
should use the standard library module, since for these versions,
``importlib_resources`` just delegates to that module.

The key goal of this module is to replace parts of `pkg_resources
<https://setuptools.readthedocs.io/en/latest/pkg_resources.html>`_ with a
solution in Python's stdlib that relies on well-defined APIs.  This makes
reading resources included in packages easier, with more stable and consistent
semantics.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Url:            http://importlib-resources.readthedocs.io/
Summary:        Read resources from Python packages
License:        Apache-2.0

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 3.4.1
# Is this needed
BuildRequires:  python%{python3_pkgversion}-toml
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
``importlib_resources`` is a backport of Python standard library
`importlib.resources
<https://docs.python.org/3.9/library/importlib.html#module-importlib.resources>`_
module for Python 2.7, and 3.4 through 3.8.  Users of Python 3.9 and beyond
should use the standard library module, since for these versions,
``importlib_resources`` just delegates to that module.

The key goal of this module is to replace parts of `pkg_resources
<https://setuptools.readthedocs.io/en/latest/pkg_resources.html>`_ with a
solution in Python's stdlib that relies on well-defined APIs.  This makes
reading resources included in packages easier, with more stable and consistent
semantics.

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
