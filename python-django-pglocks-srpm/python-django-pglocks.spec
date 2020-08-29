#
# spec file for package python-django-pglocks
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Enable only as needed
%global with_python2 0

%global pypi_name django-pglocks

# Common SRPM package
Name:           python-%{pypi_name}
Version:        1.0.4
Release:        0%{?dist}
Url:            https://github.com/Xof/django-pglocks
Summary:        django_pglocks provides useful context managers for advisory locks for PostgreSQL.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        %pypi_source
BuildArch:      noarch

%description
django-pglocks provides a useful context manager to manage PostgreSQL advisory locks. It requires Django (tested with 1.5), PostgreSQL, and (probably) psycopg2.

%if %{with_python2}
%package -n python2-%{pypi_name}
Url:            https://github.com/Xof/django-pglocks
Summary:        django_pglocks provides useful context managers for advisory locks for PostgreSQL.
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# requires stanza of py2pack
# install_requires stanza of py2pack
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
django-pglocks provides a useful context manager to manage PostgreSQL advisory locks. It requires Django (tested with 1.5), PostgreSQL, and (probably) psycopg2.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Url:            https://github.com/Xof/django-pglocks
Summary:        django_pglocks provides useful context managers for advisory locks for PostgreSQL.
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# requires stanza of py2pack
# install_requires stanza of py2pack
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
django-pglocks provides a useful context manager to manage PostgreSQL advisory locks. It requires Django (tested with 1.5), PostgreSQL, and (probably) psycopg2.

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
