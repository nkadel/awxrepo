# Created by pyp2rpm-3.3.4
%global srcname mypy_extensions
%global pypi_name mypy-extensions

Name:           python-%{pypi_name}
Version:        0.4.3
Release:        1%{?dist}
Summary:        Experimental type system extensions for programs checked with the mypy typechecker

License:        MIT License
URL:            https://github.com/python/mypy_extensions
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Mypy Extensions The "%{srcname}" module defines experimental extensions to
the standard "typing" module that are supported by the mypy typechecker.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(typing) >= 3.5.3
%description -n python3-%{pypi_name}
Mypy Extensions The "%{srcname}" module defines experimental extensions to
the standard "typing" module that are supported by the mypy typechecker.


%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/mypy_extensions.py
#%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/mypy_extensions-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Aug 23 2020 Nico KAdel-Garcia <nkadel@gmail.com> - 0.4.3-1
- Initial package.
