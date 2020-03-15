%global pypi_name pytest-aiohttp

Name:           python-%{pypi_name}
Version:        0.3.0
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        A pytest plugin for aiohttp support

License:        ASL 2.0
URL:            https://github.com/aio-libs/pytest-aiohttp/
Source0:        https://github.com/aio-libs/pytest-aiohttp/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
The library allows to use aiohttp pytest plugin without need for implicitly
loading it like pytest_plugins = 'aiohttp.pytest_plugin'.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
The library allows to use aiohttp pytest plugin without need for implicitly
loading it like pytest_plugins = 'aiohttp.pytest_plugin'.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc CHANGES.rst README.rst
%license LICENSE
%{python3_sitelib}/pytest_aiohttp/
%{python3_sitelib}/pytest_aiohttp*.egg-info

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-2
- Change source (rhbz#1719010)

* Mon Jun 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package for Fedora
