# set upstream name variable
%global pypi_name pycares


Name:           python-%{pypi_name}
Version:        3.0.0
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        Python interface for c-ares

License:        MIT
URL:            https://github.com/saghul/pycares
Source0:        %pypi_source
Patch0:         fix-version_pycares_docs_conf.py.patch

BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-cffi
# for docs
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme

%description
pycares is a Python module which provides an interface to
c-ares. c-ares is a C library that performs DNS requests and name
resolutions asynchronously.

%package     -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Python interface for c-ares
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
pycares is a Python module which provides an interface to
c-ares. c-ares is a C library that performs DNS requests and name
resolutions asynchronously.

%package     -n python-%{pypi_name}-doc
Summary:        Documentation for python-pycares
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-%{pypi_name}

%description -n python-%{pypi_name}-doc
pycares is a Python module which provides an interface to
c-ares. c-ares is a C library that performs DNS requests and name
resolutions asynchronously.

This package contains documentation in reST and HTML formats.



%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%if ! 0%{?el7}
# Build sphinx documentation
pushd docs/
# Force python3 settings
#make html
make html PYTHON="%{__python3}" SPHINXBUILD=sphinx-build-%{python3_version}
popd # docs
%endif

%install
%py3_install

# Install html docs
%if ! 0%{?el7}
mkdir -p %{buildroot}%{_pkgdocdir}/
cp -pr docs/_build/html %{buildroot}%{_pkgdocdir}/

# Move HTML sources
mv -f %{buildroot}%{_pkgdocdir}/html/_sources/ %{buildroot}%{_pkgdocdir}/rst/
%endif

# Remove buildinfo sphinx documentation
rm -rf %{buildroot}%{_pkgdocdir}/html/.buildinfo

# Fix non-standard modes (775)
chmod 755 %{buildroot}%{python3_sitearch}/%{pypi_name}/_cares.cpython-*.so


%check
%{__python3} setup.py test -s pycares._cares



%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst ChangeLog
# For arch-specific packages: sitearch
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-*.egg-info/


%files -n python-%{pypi_name}-doc
%doc examples/
%if ! 0%{?el7}
%{_pkgdocdir}/
%endif


%changelog
* Sat Aug 24 2019 Matthieu Saulnier <fantom@fedoraproject.org> - 3.0.0-1
- Bump version to 3.0.0
  - add cffi and sphinx_rtd_theme as buildrequires
  - create patch to fix path for the get_version function in docs dir
- Rebuild for RHBZ#1736524 (FTBFS in Fedora rawhide/f31)
- Removing Python 2 stuff https://fedoraproject.org/wiki/Changes/F31_Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.7

* Wed Apr  4 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 2.3.0-2
- Remove useless code duplication step
- Add missing %%python_provide macro in subpackages
- Cleanup rst doc script in %%install section
- Fix file ownership in doc subpackage

* Mon Apr  2 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 2.3.0-1
- Initial package
