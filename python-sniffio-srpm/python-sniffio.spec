# what it's called on pypi
%global srcname sniffio
# what it's imported as
%global libname sniffio
# name of egg info directory
%global eggname sniffio
# package name fragment
%global pkgname sniffio

%global _description \
You're writing a library.  You've decided to be ambitious, and support multiple\
async I/O packages, like Trio, and asyncio, and ... You've written a bunch of\
clever code to handle all the differences.  But... how do you know which piece\
of clever code to run?  This is a tiny package whose only purpose is to let you\
detect which async library your code is running under.


Name:           python-%{pkgname}
Version:        1.1.0
#Release:        2%%{?dist}
Release:        0%{?dist}
Summary:        Sniff out which async library your code is running under
License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/sniffio
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif


%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-curio
%if 0%{?rhel}
BuildRequires:  python%{python3_pkgversion}-contextvars
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%check
py.test-%{python3_version} --verbose


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Carl George <carl@george.computer> - 1.1.0-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 12 2018 Carl George <carl@george.computer> - 1.0.0-1
- Initial package
