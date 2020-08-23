# Created by pyp2rpm-3.2.2
%global srcname rst.linker
%global pypi_name rst-linker
# This package is interdependant on jaraco-packaging to build docs
# will build both with out docs and add docs in later
%bcond_with docs

Name:           python-%{pypi_name}
Version:        1.10
#Release:        5%%{?dist}
Release:        0.1%{?dist}
Summary:        Can add links and perform other custom replacements to rst

License:        MIT
URL:            https://github.com/jaraco/rst.linker
Source0:        %pypi_source
BuildArch:      noarch
 
%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
 rst.linker provides a routine for adding links and performing other custom
replacements to restructured text files as a Sphinx extension.License License
is indicated in the project metadata (typically one or more of the Trove
classifiers). For more details, see this explanation < In your sphinx
configuration file, include rst.linker as an extension and then add a
link_files configuration section...

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-dateutil

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pathspec
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 1.15.0
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-dateutil
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%{description}

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        rst.linker documentation
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-jaraco-packaging

%description -n python-%{pypi_name}-doc
Documentation for rst.linker
%endif

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info
# rename package using a -
sed -i 's/rst.linker/rst-linker/' setup.py
# Reset python in setup.py

%build
%py3_build
%if %{with docs}
# generate html docs 
# this package requires itself to build docs :/
PYTHONPATH=./ sphinx-build-%{python3_version} docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
# BuildRequires:  python(2/3)-path does not meet the test-requirement for path.py
#%%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/rst
%{python3_sitelib}/rst_linker-%{version}-py?.?.egg-info

%if %{with docs}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html 
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Dan Radez <dradez@redhat.com> - 1.10-4
- fixing egg info

* Mon Apr 08 2019 Dan Radez <dradez@redhat.com> - 1.10-3
- fixing dep to prep for enabling docs build

* Fri Apr 05 2019 Dan Radez <dradez@redhat.com> - 1.10-2
- adding py3 subpackage.

* Wed May 02 2018 Dan Radez <dradez@redhat.com> - 1.10-1
- Initial package.
