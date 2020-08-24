%global pypi_name sphinxcontrib-spelling
%global sum  A spelling checker for Sphinx-based documentation
%global desc This package contains sphinxcontrib.spelling, a spelling checker for \
Sphinx-based documentation. It uses PyEnchant to produce a report showing \
misspelled words.

# Disable dependency generator
%{?python_disable_dependency_generator}

# Can't build python3 on EL6/7 because no packages for pbr, fixtures, enchant, and sphinx
%if (0%{?rhel} && 0%{?rhel} < 8)
  %bcond_with python3
%else
%bcond_without python3
%endif

# Drop Python 2 with Fedora 30 and EL8
%if (0%{?fedora} && 0%{?fedora} < 30) || (0%{?rhel} && 0%{?rhel} < 8)
  %bcond_without python2
%else
  %bcond_with python2
%endif

Name:           python-%{pypi_name}
Version:        4.3.0
#Release:        4%%{?dist}
Release:        0%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://github.com/sphinx-contrib/spelling
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
BuildRequires:  python2-six
BuildRequires:  python2-sphinx
BuildRequires:  hunspell-en
BuildRequires:  hunspell-de
Requires:       python2-six
Requires:       python2-sphinx

%if 0%{?fedora}
BuildRequires:  python2-enchant
BuildRequires:  python2-fixtures
%else
BuildRequires:  python-enchant
BuildRequires:  python-fixtures
Patch1:         debug-unsupported.patch
%endif

%if 0%{?el6}
BuildRequires:  python-pbr
BuildRequires:  python-nose
Patch0:         el6-compat.patch
%else
BuildRequires:  python2-pbr
BuildRequires:  python2-nose
%endif

%endif

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pbr
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-fixtures
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-enchant
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-pbr
BuildRequires:  python%{python3_other_pkgversion}-nose
BuildRequires:  python%{python3_other_pkgversion}-fixtures
BuildRequires:  python%{python3_other_pkgversion}-six
BuildRequires:  python%{python3_other_pkgversion}-enchant
BuildRequires:  python%{python3_other_pkgversion}-sphinx
%endif


%description
%{desc}

# Python 2 package
%if %{with python2}
%package -n     python2-%{pypi_name}

Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:       python2-six
Requires:       python2-sphinx

%if 0%{?fedora}
Requires:       python2-enchant
%else
Requires:       python-enchant
%endif

%description -n python2-%{pypi_name}
%{desc}
%endif

# Python 3 package
%if %{with python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-enchant
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-sphinx

%description -n python%{python3_pkgversion}-%{pypi_name}
%{desc}
%endif

# Python 3 other package
%if 0%{?with_python3_other}
%package -n     python%{python3_other_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}}
Requires:       python%{python3_other_pkgversion}-enchant
Requires:       python%{python3_other_pkgversion}-six
Requires:       python%{python3_other_pkgversion}-sphinx

%description -n python%{python3_other_pkgversion}-%{pypi_name}
%{desc}
%endif


%prep
%autosetup -p0 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%if 0%{?with_python3_other}
%py3_other_build
%endif


%install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py2_install
%endif


%check
%if %{with python2}
%if 0%{?el6}
nosetests
%else
%{__python2} -m nose
%endif
%endif

%if %{with python3}
%{__python3} -m nose
%endif

%if 0%{?with_python3_other}
%{__python3_other} -m nose
%endif


%if %{with python2}
%files -n python2-%{pypi_name}
%doc README
%license LICENSE
%{python2_sitelib}/sphinxcontrib
%{python2_sitelib}/sphinxcontrib_spelling*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README
%license LICENSE
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_spelling*
%endif

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%doc README
%license LICENSE
%{python3_other_sitelib}/sphinxcontrib
%{python3_other_sitelib}/sphinxcontrib_spelling*
%endif


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Avram Lubkin <aviso@rockhopper.net> - 4.3.0-3
- Fix changelog

* Wed Nov 27 2019 Avram Lubkin <aviso@rockhopper.net> - 4.3.0-2
- Disable python dependency generator

* Mon Oct 28 2019 Avram Lubkin <aviso@rockhopper.net> - 4.3.0-1
- Updated to 4.3.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Avram Lubkin <aviso@rockhopper.net> - 4.2.1-1
- Updated to 4.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Avram Lubkin <aviso@rockhopper.net> - 4.2.0-1
- Updated to 4.2.0
- Remove Python 2 from Fedora 30+ and EL8+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-4
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018  Avram Lubkin <aviso@rockhopper.net> - 4.0.1-1
- Updated to 4.0.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017  Avram Lubkin <aviso@rockhopper.net> - 2.3.0-1
- Update to 2.3.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-3
- Rebuild for Python 3.6

* Wed Jul 20 2016 Avram Lubkin <aviso@rockhopper.net> - 2.1.2-2
- Added build support for EPEL 6 and 7

* Wed Jun 15 2016 Avram Lubkin <aviso@rockhopper.net> - 2.1.2-1
- Initial package.
