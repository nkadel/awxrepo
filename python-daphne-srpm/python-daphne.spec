#
# spec file for package python-daphne
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

%global with_python2 0

%global pypi_name daphne

# Common SRPM package
Name:           python-%{pypi_name}
Version:        2.4.0
Release:        0%{?dist}
Url:            https://github.com/django/daphne
Summary:        Django ASGI (HTTP/WebSocket) server
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
Daphne is a HTTP, HTTP2 and WebSocket protocol server for
`ASGI <https://github.com/django/asgiref/blob/master/specs/asgi.rst>`_ and
`ASGI-HTTP <https://github.com/django/asgiref/blob/master/specs/www.rst>`_,
developed to power Django Channels.

It supports automatic negotiation of protocols; there's no need for URL
prefixing to determine WebSocket endpoints versus HTTP endpoints.

*Note:* Daphne 2 is not compatible with Channels 1.x applications, only with
Channels 2.x and other ASGI applications. Install a 1.x version of Daphne
for Channels 1.x support.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        2.4.0
Release:        0%{?dist}
Url:            https://github.com/django/daphne
Summary:        Django ASGI (HTTP/WebSocket) server
License:        BSD (FIXME:No SPDX)

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
#BuildRequires:  python2-asgiref >= 8.10
#BuildRequires:  python2-autobahn >= 8.10
#BuildRequires:  python2-twisted >= 10.7
# Added manually
BuildRequires:  python2-pytest-runner
Requires:  python2-asgiref >= 8.10
Requires:  python2-autobahn >= 8.10
Requires:  python2-twisted >= 10.7
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Daphne is a HTTP, HTTP2 and WebSocket protocol server for
`ASGI <https://github.com/django/asgiref/blob/master/specs/asgi.rst>`_ and
`ASGI-HTTP <https://github.com/django/asgiref/blob/master/specs/www.rst>`_,
developed to power Django Channels.

It supports automatic negotiation of protocols; there's no need for URL
prefixing to determine WebSocket endpoints versus HTTP endpoints.

*Note:* Daphne 2 is not compatible with Channels 1.x applications, only with
Channels 2.x and other ASGI applications. Install a 1.x version of Daphne
for Channels 1.x support.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        2.4.0
Release:        0%{?dist}
Url:            https://github.com/django/daphne
Summary:        Django ASGI (HTTP/WebSocket) server
License:        BSD (FIXME:No SPDX)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
#BuildRequires:  python%{python3_pkgversion}-asgiref >= 8.10
#BuildRequires:  python%{python3_pkgversion}-autobahn >= 8.10
#BuildRequires:  python%{python3_pkgversion}-twisted >= 10.7
# Added manually
BuildRequires:  python%{python3_pkgversion}-pytest-runner
Requires:  python%{python3_pkgversion}-asgiref >= 8.10
Requires:  python%{python3_pkgversion}-autobahn >= 8.10
Requires:  python%{python3_pkgversion}-twisted >= 10.7
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Daphne is a HTTP, HTTP2 and WebSocket protocol server for
`ASGI <https://github.com/django/asgiref/blob/master/specs/asgi.rst>`_ and
`ASGI-HTTP <https://github.com/django/asgiref/blob/master/specs/www.rst>`_,
developed to power Django Channels.

It supports automatic negotiation of protocols; there's no need for URL
prefixing to determine WebSocket endpoints versus HTTP endpoints.

*Note:* Daphne 2 is not compatible with Channels 1.x applications, only with
Channels 2.x and other ASGI applications. Install a 1.x version of Daphne
for Channels 1.x support.

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
%{__mv} $RPM_BUILD_ROOT%{_bindir}/daphne $RPM_BUILD_ROOT%{_bindir}/daphne-%{python2_version}
%{__ln_s} daphne-%{python2_version} $RPM_BUILD_ROOT%{_bindir}/daphne
%endif # with_python2

%if %{with_python3}
%py3_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/daphne $RPM_BUILD_ROOT%{_bindir}/daphne-%{python3_version}
%{__ln_s} daphne-%{python3_version} $RPM_BUILD_ROOT%{_bindir}/daphne
%endif # with_python3

%clean
rm -rf %{buildroot}

%if %{with_python2}
%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%{python2_sitelib}/*
%{_bindir}/daphne-%{python2_version}
%if ! %{with_python3}
%{_bindir}/daphne
%endif
%endif # with_python2

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/daphne-%{python3_version}
%{_bindir}/daphne
%endif # with_python3

%changelog
