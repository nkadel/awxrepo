#
# spec file for package python-irc
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
%global with_python3 1
%global with_python2 0

%global pypi_name irc

# Common SRPM package
Name:           python-%{pypi_name}
Version:        18.0.0
Release:        0%{?dist}
Url:            https://github.com/jaraco/irc
Summary:        IRC (Internet Relay Chat) protocol library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
This library provides a low-level implementation of the IRC protocol for
Python.  It provides an event-driven IRC client framework.  It has
a fairly thorough support for the basic IRC protocol, CTCP, and DCC
connections.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        18.0.0
Release:        0%{?dist}
Url:            https://github.com/jaraco/irc
Summary:        IRC (Internet Relay Chat) protocol library for Python
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm >= 1.5.0
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
This library provides a low-level implementation of the IRC protocol for
Python.  It provides an event-driven IRC client framework.  It has
a fairly thorough support for the basic IRC protocol, CTCP, and DCC
connections.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        18.0.0
Release:        0%{?dist}
Url:            https://github.com/jaraco/irc
Summary:        IRC (Internet Relay Chat) protocol library for Python
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 1.5.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
This library provides a low-level implementation of the IRC protocol for
Python.  It provides an event-driven IRC client framework.  It has
a fairly thorough support for the basic IRC protocol, CTCP, and DCC
connections.

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
