#
# spec file for package python-jaraco.collections
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Enable only as needed
%global with_python2 0

%global pypi_name jaraco.collections
%global pkg_name jaraco-collections

# Common SRPM package
Name:           python-%{pkg_name}
Version:        3.0.0
Release:        0%{?dist}
Url:            https://github.com/jaraco/jaraco.collections
Summary:        Collection objects similar to those in stdlib by jaraco
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires:  epel-rpm-macros
%endif

%description
Models and classes to supplement the stdlib 'collections' module.

RangeMap
--------

A dictionary-like object that maps a range of values to a given value.

%if %{with_python2}
%package -n python2-%{pkg_name}
Url:            https://github.com/jaraco/jaraco.collections
Summary:        Collection objects similar to those in stdlib by jaraco
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm >= 1.15.0
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pkg_name}
Models and classes to supplement the stdlib 'collections' module.

RangeMap
--------

A dictionary-like object that maps a range of values to a given value.


%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pkg_name}
Url:            https://github.com/jaraco/jaraco.collections
Summary:        Collection objects similar to those in stdlib by jaraco
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 1.15.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pkg_name}
Models and classes to supplement the stdlib 'collections' module.

RangeMap
--------

A dictionary-like object that maps a range of values to a given value.

%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

# fix jaraco deps in setup so they do not get improperly generated
sed -i 's/jaraco.text/jaraco-text/' setup.cfg
sed -i 's/jaraco.classes/jaraco-classes/' setup.cfg
sed -i 's/jaraco.packaging/jaraco-packaging/' setup.cfg

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
%files -n python2-%{pkg_name}
%defattr(-,root,root,-)
%{python2_sitelib}/*
%endif # with_python2

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pkg_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%endif # with_python3

%changelog
