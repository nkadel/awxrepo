#
# spec file for package python-django-auth-ldap
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

%global pypi_name django-auth-ldap

# Common SRPM package
Name:           python-%{pypi_name}
Version:        2.1.0
Release:        0%{?dist}
Url:            https://github.com/django-auth-ldap/django-auth-ldap
Summary:        Django LDAP authentication backend.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        2.1.0
Release:        0%{?dist}
Url:            https://github.com/django-auth-ldap/django-auth-ldap
Summary:        Django LDAP authentication backend.
License:        BSD (FIXME:No SPDX)

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-django >= 1.11
Requires:       python2-python-django >= 3.1
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        2.1.0
Release:        0%{?dist}
Url:            https://github.com/django-auth-ldap/django-auth-ldap
Summary:        Django LDAP authentication backend.
License:        BSD (FIXME:No SPDX)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-django >= 1.11
Requires:       python%{python3_pkgversion}-python-django >= 3.1
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.

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
