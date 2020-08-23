# Created by pyp2rpm-3.3.4
%global pypi_name sphinxcontrib-qthelp

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        0%{?dist}
Summary:        sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document

License:        BSD
URL:            http://sphinx-doc.org/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils-stubs)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(docutils-stubs)
Requires:       python3dist(flake8)
Requires:       python3dist(mypy)
Requires:       python3dist(pytest)
%description -n python3-%{pypi_name}
sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document.


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
%{python3_sitelib}/sphinxcontrib_qthelp-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Aug 23 2020 Nico Kadel-Garcia <nkadel@gmail.com> - 1.0.3-1
- Initial package.