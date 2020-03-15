# what it's called on pypi
%global srcname async_generator
# what it's imported as
%global libname async_generator
# name of egg info directory
%global eggname async_generator
# package name fragment
%global pkgname async-generator

%global _description \
This library generally tries hard to match the semantics of Python 3.6's native\
async generators in every detail (PEP 525), with additional support for yield\
from and for returning non-None values from an async generator (under the\
theory that these may well be added to native async generators one day).


Name:           python-%{pkgname}
Version:        1.10
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        Async generators and context managers
License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/async_generator
Source0:        %pypi_source
BuildArch:      noarch


%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -r %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if 0%{?fedora}
%check
py.test-%{python3_version} --verbose
%endif

%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Carl George <carl@george.computer> - 1.10-1
- Initial package
