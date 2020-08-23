#
# spec file for package python-amqp
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

%global pypi_name amqp

# Common SRPM package
Name:           python-%{pypi_name}
Version:        2.5.2
Release:        0%{?dist}
Url:            http://github.com/celery/py-amqp
Summary:        Low-level AMQP client for Python (fork of amqplib).
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by `kombu`_ as a pure python
alternative when `librabbitmq`_ is not available.


%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        2.5.2
Release:        0%{?dist}
Url:            http://github.com/celery/py-amqp
Summary:        Low-level AMQP client for Python (fork of amqplib).
License:        BSD (FIXME:No SPDX)

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:  python2-vine >= 1.1.3
Conflicts: python2-vine >= 5.0.0
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by `kombu`_ as a pure python
alternative when `librabbitmq`_ is not available.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        2.5.2
Release:        0%{?dist}
Url:            http://github.com/celery/py-amqp
Summary:        Low-level AMQP client for Python (fork of amqplib).
License:        BSD (FIXME:No SPDX)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:  python%{python3_pkgversion}-vine >= 1.1.3
Conflicts: python%{python3_pkgversion}-vine >= 5.0.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by `kombu`_ as a pure python
alternative when `librabbitmq`_ is not available.

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
