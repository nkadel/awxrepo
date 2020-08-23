#
# spec file for package python-jaraco.itertools
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

%global with_python2 0

%global pypi_name jaraco.itertools
%global pkg_name jaraco-itertools

# Common SRPM package
Name:           python-%{pkg_name}
Version:        5.0.0
Release:        0%{?dist}
Url:            https://github.com/jaraco/jaraco.itertools
Summary:        jaraco.itertools
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description


%if %{with_python2}
%package -n python2-%{pkg_name}
Version:        5.0.0
Release:        0%{?dist}
Url:            https://github.com/jaraco/jaraco.itertools
Summary:        jaraco.itertools
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm >= 1.15
%{?python_provide:%python_provide python2-%{pkg_name}}

%description -n python2-%{pypi_name}


%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pkg_name}
Version:        5.0.0
Release:        0%{?dist}
Url:            https://github.com/jaraco/jaraco.itertools
Summary:        jaraco.itertools
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 1.15
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkg_name}}

%description -n python%{python3_pkgversion}-%{pkg_name}

%endif # with_python3

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
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
