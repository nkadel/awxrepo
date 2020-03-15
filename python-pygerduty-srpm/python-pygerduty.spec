#
# spec file for package python-pygerduty
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

%global pypi_name pygerduty

# Common SRPM package
Name:           python-%{pypi_name}
Version:        0.38.2
Release:        0%{?dist}
Url:            https://github.com/dropbox/pygerduty
Summary:        Python Client Library for PagerDuty's REST API
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
Python Library for PagerDuty's REST API and Events API. This library
was originally written to support v1 and is currently being updated to
be compatible with v2 of the API. See "Migrating from v1 to v2" for
more details.


%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        0.38.2
Release:        0%{?dist}
Url:            https://github.com/dropbox/pygerduty
Summary:        Python Client Library for PagerDuty's REST API
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Python Library for PagerDuty's REST API and Events API. This library
was originally written to support v1 and is currently being updated to
be compatible with v2 of the API. See "Migrating from v1 to v2" for
more details.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%clean
rm -rf %{buildroot}

%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/*

%changelog
