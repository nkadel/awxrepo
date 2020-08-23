# Created by pyp2rpm-3.3.4
%global pypi_name sphinxcontrib-jsmath

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        0%{?dist}
Summary:        A sphinx extension which renders display math in HTML via JavaScript

License:        BSD
URL:            http://sphinx-doc.org/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
sphinxcontrib-jsmath is a sphinx extension which renders display math in HTML
via JavaScript.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(flake8)
Requires:       python3dist(mypy)
Requires:       python3dist(pytest)
%description -n python3-%{pypi_name}
sphinxcontrib-jsmath is a sphinx extension which renders display math in HTML
via JavaScript.


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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_jsmath-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Aug 23 2020 Nico Kadel-Garcia <nkadel@gmail.com> - 1.0.1-1
- Initial package.
