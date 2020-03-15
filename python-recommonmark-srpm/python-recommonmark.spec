#
# spec file for package python-recommonmark
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

%global pypi_name recommonmark

# Common SRPM package
Name:           python-%{pypi_name}
Version:        0.6.0
Release:        0%{?dist}
Url:            https://github.com/rtfd/recommonmark
Summary:        A docutils-compatibility bridge to CommonMark, enabling you to write CommonMark inside of Docutils & Sphinx projects.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
A docutils-compatibility bridge to CommonMark.

This allows you to write CommonMark inside of Docutils & Sphinx projects.

%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        0.6.0
Release:        0%{?dist}
Url:            https://github.com/rtfd/recommonmark
Summary:        A docutils-compatibility bridge to CommonMark, enabling you to write CommonMark inside of Docutils & Sphinx projects.
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
A docutils-compatibility bridge to CommonMark.

This allows you to write CommonMark inside of Docutils & Sphinx projects.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%clean
rm -rf %{buildroot}

%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/cm2*

%changelog
