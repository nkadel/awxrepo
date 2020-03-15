#
# spec file for package python-social-auth-app-django
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Enable only as needed
%global with_python2 0

%global pypi_name social-auth-app-django

# Common SRPM package
Name:           python-%{pypi_name}
Version:        3.1.0
Release:        0%{?dist}
Url:            https://github.com/python-social-auth/social-app-django
Summary:        Python Social Authentication, Django integration.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires:  epel-rpm-macros
%endif

%description
Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

This is the [Django](https://www.djangoproject.com/) component of the
[python-social-auth ecosystem](https://github.com/python-social-auth/social-core),
it implements the needed functionality to integrate
[social-auth-core](https://github.com/python-social-auth/social-core)
in a Django based project.

%if %{with_python2}
%package -n python2-%{pypi_name}
Url:            https://github.com/python-social-auth/social-app-django
Summary:        Python Social Authentication, Django integration.
License:        BSD (FIXME:No SPDX)

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# requires stanza of py2pack
# install_requires stanza of py2pack
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

This is the [Django](https://www.djangoproject.com/) component of the
[python-social-auth ecosystem](https://github.com/python-social-auth/social-core),
it implements the needed functionality to integrate
[social-auth-core](https://github.com/python-social-auth/social-core)
in a Django based project.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Url:            https://github.com/python-social-auth/social-app-django
Summary:        Python Social Authentication, Django integration.
License:        BSD (FIXME:No SPDX)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# requires stanza of py2pack
# install_requires stanza of py2pack
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

This is the [Django](https://www.djangoproject.com/) component of the
[python-social-auth ecosystem](https://github.com/python-social-auth/social-core),
it implements the needed functionality to integrate
[social-auth-core](https://github.com/python-social-auth/social-core)
in a Django based project.

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
