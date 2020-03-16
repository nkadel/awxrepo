#
# spec file for package python-jaraco.logging
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Enable only as needed
%global with_python2 0

%global pypi_name jaraco.logging
%global pkg_name jaraco-logging

# Common SRPM package
Name:           python-%{pkg_name}
Version:        3.0.0
Release:        0%{?dist}
Url:            https://github.com/jaraco/jaraco.logging
Summary:        Support for Python logging facility
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires:  epel-rpm-macros
%endif

%description
Quickly solicit log level info from command-line parameters::

    parser = argparse.ArgumentParser()
    jaraco.logging.add_arguments(parser)
    args = parser.parse_args()
    jaraco.logging.setup(args)

%if %{with_python2}
%package -n python2-%{pkg_name}
Url:            https://github.com/jaraco/jaraco.logging
Summary:        Support for Python logging facility
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm >= 1.15.0
# requires stanza of py2pack
# install_requires stanza of py2pack
%{?python_provide:%python_provide python2-%{pkg_name}}

%description -n python2-%{pkg_name}
Quickly solicit log level info from command-line parameters::

    parser = argparse.ArgumentParser()
    jaraco.logging.add_arguments(parser)
    args = parser.parse_args()
    jaraco.logging.setup(args)




%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pkg_name}
Url:            https://github.com/jaraco/jaraco.logging
Summary:        Support for Python logging facility
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 1.15.0
# requires stanza of py2pack
# install_requires stanza of py2pack
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkg_name}}

%description -n python%{python3_pkgversion}-%{pkg_name}
Quickly solicit log level info from command-line parameters::

    parser = argparse.ArgumentParser()
    jaraco.logging.add_arguments(parser)
    args = parser.parse_args()
    jaraco.logging.setup(args)




%endif # with_python3

%prep
%autosetup -n %{pypi_name}-%{version}
# rename package to use a -
sed -i 's/%{pypi_name}/%{pkg_name}/' setup.cfg
# rename jaraco dependencies to use a -
sed -i 's/^\tjaraco\./	jaraco-/' setup.cfg

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
%files -n python2-%{pkg_name}
%defattr(-,root,root,-)
%{python2_sitelib}/*
# These excludes are provided by python2-jaraco
%exclude %{python2_sitelib}/jaraco/__init__*
%exclude %{python2_sitelib}/jaraco/__pycache__/__init__*
%endif # with_python2

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pkg_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
# These excludes are provided by python3-jaraco
%exclude %{python3_sitelib}/jaraco/__init__*
%exclude %{python3_sitelib}/jaraco/__pycache__/__init__*
%endif # with_python3

%changelog
