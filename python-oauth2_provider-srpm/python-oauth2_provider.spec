# Created by pyp2rpm-3.3.4
%global pypi_name oauth2_provider

Name:           python-%{pypi_name}
Version:        0.0
Release:        0%{?dist}
Summary:        UNKNOWN

License:        None
URL:            http://github.com/eventray/oauth2_provider
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(webtest)

%description
UNKNOWN

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
UNKNOWN


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

#%check
#%{__python3} setup.py test

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Aug 22 2020 Nico KAdel-Garcia <nkadel@gmail.com> - 0.0-1
- Initial package.
- Tarball contains no docs
- %%check does not work
