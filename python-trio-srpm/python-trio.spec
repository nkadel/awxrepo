# what it's called on pypi
%global srcname trio
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python.  Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.  A web spider that wants to fetch lots of
pages in parallel, a web server that needs to juggle lots of downloads and
websocket connections at the same time, a process supervisor monitoring
multiple subprocesses... that sort of thing.  Compared to other libraries, Trio
attempts to distinguish itself with an obsessive focus on usability and
correctness.  Concurrency is complicated; we try to make it easy to get things
right.}

%bcond_without  tests


Name:           python-%{pkgname}
Version:        0.11.0
#Release:        2%%{?dist}
Release:        0%{?dist}
Summary:        An async/await-native I/O library for humans and snake people
License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/trio
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description %{common_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pyOpenSSL
BuildRequires:  python%{python3_pkgversion}-trustme
BuildRequires:  python%{python3_pkgversion}-attrs >= 18.2.0
BuildRequires:  python%{python3_pkgversion}-sortedcontainers
BuildRequires:  python%{python3_pkgversion}-async-generator >= 1.9
BuildRequires:  python%{python3_pkgversion}-idna
BuildRequires:  python%{python3_pkgversion}-outcome
BuildRequires:  python%{python3_pkgversion}-sniffio
%endif
Requires:       python%{python3_pkgversion}-attrs >= 18.2.0
Requires:       python%{python3_pkgversion}-sortedcontainers
Requires:       python%{python3_pkgversion}-async-generator >= 1.9
Requires:       python%{python3_pkgversion}-idna
Requires:       python%{python3_pkgversion}-outcome
Requires:       python%{python3_pkgversion}-sniffio
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose trio/_core/tests
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Carl George <carl@george.computer> - 0.11.0-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Carl George <carl@george.computer> - 0.7.0-1
- Initial package
