# FIXME python3-pytests is not available in epel7
%bcond_with tests

%global pypi_name chardet

Name:           python3-%{pypi_name}
Version:        3.0.4
#Release:        1R%{?dist}
Release:        0%{?dist}
Summary:        Character encoding auto-detection in Python
License:        LGPLv2
URL:            https://github.com/%{pypi_name}/%{pypi_name}
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{?with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif
%if 0%{?python3_other_pkgversion}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%if 0%{?with tests}
BuildRequires:  python%{python3_other_pkgversion}-pytest
%endif
%endif

%global _description\
Character encoding auto-detection in Python. As\
smart as your browser. Open source.

%description %_description

%if %{python3_pkgversion} != 3
%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Character encoding auto-detection in Python %{python3_version}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%_description
This package is for Python3 with version %{python3_version} .
%endif

%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-%{pypi_name}
Summary:        Character encoding auto-detection in Python %{python3_other_version}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}}

%description -n python%{python3_other_pkgversion}-%{pypi_name}
%_description
This package is for Python3 with version %{python3_other_version} .
%endif


%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build
%{?python3_other_pkgversion: %py3_other_build}

%install
%py3_install
mv %{buildroot}%{_bindir}/chardetect %{buildroot}%{_bindir}/chardetect-%{python3_version}
ln -s chardetect-%{python3_version} %{buildroot}%{_bindir}/chardetect-3
%if 0%{?python3_other_pkgversion}
%py3_other_install
mv %{buildroot}%{_bindir}/chardetect %{buildroot}%{_bindir}/chardetect-%{python3_other_version}
%endif

%check
%if %{with tests}
%{__python3} -m pytest -v
%{?python3_other_pkgversion: %{__python3_other} -m pytest -v}
%endif


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/chardetect-%{python3_version}
%{_bindir}/chardetect-3

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_other_sitelib}/%{pypi_name}/
%{python3_other_sitelib}/%{pypi_name}-%{version}-py%{python3_other_version}.egg-info/
%{_bindir}/chardetect-%{python3_other_version}
%endif


%changelog
* Thu Aug 22 2019 Orion Poplawski <orion@nwra.com> - 3.0.4-1
- Update to 3.0.4

* Tue Apr  2 2019 Orion Poplawski <orion@nwra.com> - 2.3.0-6
- Fix chardetect-3 link (bug #1691827)

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 2.3.0-5
- Rebuilt to change main python from 3.4 to 3.6

* Fri Sep 28 2018 Raphael Groner <projects.rg@smart.ms> - 2.3.0-4
- add python3 subpackages
- use same macro names as in Fedora
- use binary suffix and individual symlinks for python default version

* Thu Jan 14 2016 Orion Poplwski <orion@cora.nwra.com> - 2.3.0-3
- Drop group, use new macros

* Wed Jan 13 2016 Orion Poplwski <orion@cora.nwra.com> - 2.3.0-2
- Remove unneeded shebang

* Tue Dec 29 2015 Orion Poplwski <orion@cora.nwra.com> - 2.3.0-1
- Initial EPEL7 package
