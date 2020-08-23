# Created by pyp2rpm-3.3.4
%global srcname django-split-settings
%global pypi_name django-split_settings
# Added for short references
%global shortmodname split_settings

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        0%{?dist}
Summary:        Organize Django settings into multiple files and directories

License:        None
URL:            https://django-split-settings.readthedocs.io
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
<p align"center"> <img src" alt"%{ssrcname} logo">
[![wemake.services]( [![Build Status](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
<p align"center"> <img src" alt"%{srcname} logo">
[![wemake.services]( [![Build Status](


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
# Django modules have funky naming
%{python3_sitelib}/%{shortmodname}
#%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/django_%{shortmodname}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Aug 22 2020 Nico KAdel-Garcia <nkadel@gmail.com> - 1.0.1-1
- Initial package.
- Tweak modname because split-settings does not match split_settings