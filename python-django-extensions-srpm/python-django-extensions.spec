#
# spec file for package python-django-extensions
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Discard python2 compilation, not compatible with django-extensions
%global with_python2 0

%global pypi_name django-extensions

# Common SRPM package
Name:           python-%{pypi_name}
Version:        2.2.5
Release:        0%{?dist}
Url:            http://github.com/django-extensions/django-extensions
Summary:        Extensions for Django
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        %pypi_source
BuildArch:      noarch

%description
Django Extensions is a collection of custom extensions for the Django Framework.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        2.2.5
Release:        0%{?dist}
Url:            http://github.com/django-extensions/django-extensions
Summary:        Extensions for Django
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-six
# For python <= 3.5
Requires:       python2-typing
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Django Extensions is a collection of custom extensions for the Django Framework.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        2.2.5
Release:        0%{?dist}
Url:            http://github.com/django-extensions/django-extensions
Summary:        Extensions for Django
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-six
# For python < 3.5
#Requires:       python%{python3_pkgversion}-typing
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Django Extensions is a collection of custom extensions for the Django Framework.

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
