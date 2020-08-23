#
# spec file for package python-django-jsonbfield
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

%global with_python3 1

%global with_python2 0

%global pypi_name django-jsonbfield

# Common SRPM package
Name:           python-%{pypi_name}
Version:        0.1.0
Release:        0%{?dist}
Url:            https://github.com/totalgood/django-jsonbfield/
Summary:        Django JSONField that utilized PostGRESQL jsonb field type
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
This is basically a standalone version of the JSONB support in the
Postgres contrib package of the Django master branch, targeted for the
Django 1.9 release.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        0.1.0
Release:        0%{?dist}
Url:            https://github.com/totalgood/django-jsonbfield/
Summary:        Django JSONField that utilized PostGRESQL jsonb field type
License:        BSD (FIXME:No SPDX)

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
This is basically a standalone version of the JSONB support in the
Postgres contrib package of the Django master branch, targeted for the
Django 1.9 release.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        0.1.0
Release:        0%{?dist}
Url:            https://github.com/totalgood/django-jsonbfield/
Summary:        Django JSONField that utilized PostGRESQL jsonb field type
License:        BSD (FIXME:No SPDX)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
This is basically a standalone version of the JSONB support in the
Postgres contrib package of the Django master branch, targeted for the
Django 1.9 release.

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
