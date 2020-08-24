# Created by pyp2rpm-3.3.4
%global pypi_name sphinx-rst-builder

Name:           python-%{pypi_name}
Version:        0.0.3
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        Sphinx reStructuredText builder

License:        BSD-2-Clause
URL:            https://github.com/davidfritzsche/sphinx-rst-builder
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Sphinx reStructuredText Builder *******************************Sphinx <
extension to build reST (reStructuredText < files.This extension is in
particular useful to use in combination with the autodoc extension to
automatically generate documentation for use by any rst parser (such as the
GitHub wiki).In itself, the extension is fairly straightforward – it takes the
parsed reST file from Sphinx...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(sphinx) >= 2
%description -n python3-%{pypi_name}
Sphinx reStructuredText Builder *******************************Sphinx <
extension to build reST (reStructuredText < files.This extension is in
particular useful to use in combination with the autodoc extension to
automatically generate documentation for use by any rst parser (such as the
GitHub wiki).In itself, the extension is fairly straightforward – it takes the
parsed reST file from Sphinx...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/sphinx_rst_builder
%{python3_sitelib}/sphinx_rst_builder-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Aug 24 2020 Koji Builder <koji@dummy.lan> - 0.0.3-1
- Initial package.
