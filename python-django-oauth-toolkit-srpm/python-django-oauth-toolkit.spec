#
# spec file for package python-django-oauth-toolkit
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

%global with_python3 1

%global with_python2 0

%global pypi_name django-oauth-toolkit

# Common SRPM package
Name:           python-%{pypi_name}
Version:        1.1.3
Release:        0%{?dist}
Url:            https://github.com/jazzband/django-oauth-toolkit
Summary:        OAuth2 Provider for Django
License:        BSD License (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
Django OAuth Toolkit
====================

*OAuth2 goodies for the Djangonauts!*

If you are facing one or more of the following:
 * Your Django app exposes a web API you want to protect with OAuth2 authentication,
 * You need to implement an OAuth2 authorization server to provide tokens management for your infrastructure,

 %if %{with_python2}
%package -n python2-%{pypi_name}
Release:        0%{?dist}
Url:            https://github.com/jazzband/django-oauth-toolkit
Summary:        OAuth2 Provider for Django
License:        BSD License (FIXME:No SPDX)

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Django OAuth Toolkit
====================

*OAuth2 goodies for the Djangonauts!*

If you are facing one or more of the following:
 * Your Django app exposes a web API you want to protect with OAuth2 authentication,
 * You need to implement an OAuth2 authorization server to provide tokens management for your infrastructure,

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Release:        0%{?dist}
Url:            https://github.com/jazzband/django-oauth-toolkit
Summary:        OAuth2 Provider for Django
License:        BSD License (FIXME:No SPDX)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Django OAuth Toolkit
====================

*OAuth2 goodies for the Djangonauts!*

If you are facing one or more of the following:
 * Your Django app exposes a web API you want to protect with OAuth2 authentication,
 * You need to implement an OAuth2 authorization server to provide tokens management for your infrastructure,

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
