#
# spec file for package python-commonmark
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

%global pypi_name commonmark

# Common SRPM package
Name:           python-%{pypi_name}
Version:        0.9.1
Release:        0%{?dist}
Url:            https://github.com/rtfd/commonmark.py
Summary:        Python parser for the CommonMark Markdown spec
License:        BSD-3-Clause
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        %pypi_source
BuildArch:      noarch

%description
commonmark.py
=============

commonmark.py is a pure Python port of `jgm <https://github.com/jgm>`__'s
`commonmark.js <https://github.com/jgm/commonmark.js>`__, a
Markdown parser and renderer for the
`CommonMark <http://commonmark.org>`__ specification, using only native
modules. Once both this project and the CommonMark specification are
stable we will release the first ``1.0`` version and attempt to keep up
to date with changes in ``commonmark.js``.

%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        0.9.1
Release:        0%{?dist}
Url:            https://github.com/rtfd/commonmark.py
Summary:        Python parser for the CommonMark Markdown spec
License:        BSD-3-Clause

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
commonmark.py
=============

commonmark.py is a pure Python port of `jgm <https://github.com/jgm>`__'s
`commonmark.js <https://github.com/jgm/commonmark.js>`__, a
Markdown parser and renderer for the
`CommonMark <http://commonmark.org>`__ specification, using only native
modules. Once both this project and the CommonMark specification are
stable we will release the first ``1.0`` version and attempt to keep up
to date with changes in ``commonmark.js``.

commonmark.py is tested against the CommonMark spec with Python versions
2.7, 3.4, 3.5, 3.6, and 3.7.

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
%{_bindir}/*

%changelog
