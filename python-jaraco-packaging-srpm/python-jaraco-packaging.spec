# Created by pyp2rpm-3.2.2
%global pypi_name jaraco.packaging
%global pkg_name jaraco-packaging
# This package is interdependant on rst-linker to build docs
# will build both with out docs and add docs in later
%bcond_with docs 

Name:           python-%{pkg_name}
Version:        6.1
Release:        8%{?dist}
Summary:        Tools to supplement packaging Python releases

License:        MIT
URL:            https://github.com/jaraco/jaraco.packaging
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
Tools for packaging.dependency_tree A dist-utils command for reporting the
dependency tree as resolved by setup-tools. Use after installing a package.show
A dist-utils command for reporting the attributes of a distribution, such as the
version or author name.

%package -n python%{python3_pkgversion}-jaraco
Summary: A Parent package for jaraco's parent dir and init file.
BuildRequires:  python%{python3_pkgversion}-devel
%{?python_provide:%python_provide python%{python3_pkgversion}-jaraco}

%description -n python%{python3_pkgversion}-jaraco
A Parent package for jaraco's parent dir and init file.

%package -n python%{python3_pkgversion}-%{pkg_name}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-jaraco
Requires:       python%{python3_pkgversion}-rst-linker
Requires:       python%{python3_pkgversion}-six >= 1.4
Requires:       python%{python3_pkgversion}-setuptools

BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 1.15.0
BuildRequires:  python%{python3_pkgversion}-six >= 1.4
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkg_name}}

%description -n python%{python3_pkgversion}-%{pkg_name}
Tools for packaging.dependency_tree A dist-utils command for reporting the
dependency tree as resolved by setup-tools. Use after installing a package.show
A dist-utils command for reporting the attributes of a distribution, such as the
version or author name.


%if %{with docs}
%package -n python-%{pkg_name}-doc
Summary:        jaraco.packaging documentation

BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-rst-linker

%description -n python-%{pkg_name}-doc
Documentation for jaraco.packaging
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# rename package in setup to -
sed -i 's/name = %{pypi_name}/name = %{pkg_name}/' setup.cfg
# rename jaraco dependencies to use a -
sed -i 's/^\tjaraco\./	jaraco-/' setup.cfg

%build
%py3_build
%if %{with docs}
# generate html docs 
# This package requires itself to build docs :/
PYTHONPATH=./ sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-jaraco
%license LICENSE
%doc README.rst
%{python3_sitelib}/jaraco
%exclude %{python3_sitelib}/jaraco/packaging

%files -n python%{python3_pkgversion}-%{pkg_name}
%license LICENSE
%doc README.rst
%{_bindir}/upload-package
%{_bindir}/dependency-tree
%{python3_sitelib}/jaraco/packaging
%{python3_sitelib}/jaraco_packaging-%{version}-py?.?.egg-info

%if %{with docs}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc html 
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Dan Radez <dradez@redhat.com> - 6.1-7
- fixing egg info

* Mon Apr 08 2019 Dan Radez <dradez@redhat.com> - 6.1-6
- Updating doc reqs in prep to enable doc build

* Fri Apr 05 2019 Dan Radez <dradez@redhat.com> - 6.1-5
- fixing python-jaraco-packaging requires... again

* Fri Apr 05 2019 Dan Radez <dradez@redhat.com> - 6.1-4
- fixing python-jaraco-packaging requires.

* Fri Apr 05 2019 Dan Radez <dradez@redhat.com> - 6.1-3
- adding python-jaraco subpackage.

* Fri Apr 05 2019 Dan Radez <dradez@redhat.com> - 6.1-2
- adding py3 subpackage.

* Tue Apr 02 2019 Dan Radez <dradez@redhat.com> - 6.1-1
- Initial package.
