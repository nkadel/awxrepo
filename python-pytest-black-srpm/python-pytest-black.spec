# Created by pyp2rpm-3.3.3
%global pypi_name pytest-black

Name:           python-%{pypi_name}
Version:        0.3.8
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        A pytest plugin to enable format checking with black

License:        MIT
URL:            https://github.com/shopkeep/pytest-black
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(black) >= 19.3b0
BuildRequires:  python3dist(pytest) >= 3.5.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(toml)

%description
pytest-black [![Build Status]( pytest plugin to enable format checking with
[black]( Requirements * [pytest]( * [black]( Installation $ pip install pytest-
blackUsage To run pytest with formatting checks provided by black: $ pytest
--black The plugin will output a diff of suggested formatting changes (if any
exist). Changes will _not_ be applied automatically.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python3dist(black) >= 19.3b0
Requires:       python3dist(pytest) >= 3.5.0
Requires:       python3dist(setuptools)
Requires:       python3dist(toml)
%description -n python%{python3_pkgversion}-%{pypi_name}
pytest-black [![Build Status]( pytest plugin to enable format checking with
[black]( Requirements * [pytest]( * [black]( Installation $ pip install pytest-
blackUsage To run pytest with formatting checks provided by black: $ pytest
--black The plugin will output a diff of suggested formatting changes (if any
exist). Changes will _not_ be applied automatically.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_black.py
#%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/pytest_black-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Mar 31 2020 Nico Kadel-Garcia <nkadel@gmail.com> - 0.3.8-1
- Initial package.
