# Created by pyp2rpm-3.3.4
%global pypi_name docutils-stubs

Name:           python-%{pypi_name}
Version:        0.0.21
Release:        0%{?dist}
Summary:        PEP 561 type stubs for docutils

License:        None
URL:            https://github.com/tk0miya/docutils-stubs
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
docutils-stubs PEP 561_ based Type information for docutils_... _PEP 561: ..
_docutils:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(docutils) = 0.14
%description -n python3-%{pypi_name}
docutils-stubs PEP 561_ based Type information for docutils_... _PEP 561: ..
_docutils:


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/docutils_stubs-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Aug 23 2020 Nico Kadel-Garcia <nkadel@gmail.com> - 0.0.21-1
- Initial package.
