# Created by pyp2rpm-3.3.4
%global pypi_name pyenchant

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        0%{?dist}
Summary:        Python bindings for the Enchant spellchecking system

License:        LGPL
URL:            https://pyenchant.github.io/pyenchant/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
pyenchant: Python bindings for the Enchant spellchecker .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pyenchant: Python bindings for the Enchant spellchecker .. image::


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/enchant
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Aug 23 2020 Nico KAdel-Garcia <nkadel@gmail.com> - 3.1.1-1
- Initial package.
