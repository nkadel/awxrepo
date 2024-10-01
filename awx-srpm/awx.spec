# Created by pyp2rpm-3.3.10
%global pypi_name awx
%global pypi_version 0.1.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        AWX Satellite Data Reader

License:        None
URL:            https://github.com/wqshen/AwxReader
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pyproj)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(xarray)

%description
 python reader for satellite product format data (.AWX)This package provide a
user-friendly interface to AWX data, it can read 3 type AWX, that is- Product
Type 1, geostationary satellite image product - Product Type 2, polar orbiting
satellite image product - Product Type 3, Grid product README- en
[English](README.md) - zh_CN [简体中文](README.zh-CN.md) Installinstall from
pypishell pip install...

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?py3_provide:%py3_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python3dist(numpy)
Requires:       python3dist(pyproj)
Requires:       python3dist(setuptools)
Requires:       python3dist(xarray)

%description -n python%{python3_pkgversion}-%{pypi_name}
 python reader for satellite product format data (.AWX)This package provide a
user-friendly interface to AWX data, it can read 3 type AWX, that is- Product
Type 1, geostationary satellite image product - Product Type 2, polar orbiting
satellite image product - Product Type 3, Grid product README- en
[English](README.md) - zh_CN [简体中文](README.zh-CN.md) Installinstall from
pypishell pip install...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
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
%{_bindir}/awx_info
%{_bindir}/awx_to_nc
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Thu Sep 19 2024 Nico Kadel-Garcia <nkadel@gmail.com> - 0.1.1-1
- Initial package.
