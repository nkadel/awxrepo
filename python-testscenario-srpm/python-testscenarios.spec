# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

%global with_python3 1

%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python2 0
%else
%global with_python2 1
%endif

%global pypi_name testscenarios

Name:           python-%{pypi_name}
Version:        0.5.0
#Release:        14%%{?dist}
Release:        0%{?dist}
Summary:        Testscenarios, a pyunit extension for dependency injection

License:        ASL 2.0 and BSD
URL:            https://launchpad.net/testscenarios
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-fixtures
BuildRequires:  python2-setuptools
BuildRequires:  python2-pbr
BuildRequires:  python2-testtools
%endif

%if %{with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-fixtures
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pbr
BuildRequires:  python%{python3_pkgversion}-testtools
%endif # with_python3

%global _description\
testscenarios provides clean dependency injection for python unittest style\
tests. This can be used for interface testing (testing many implementations via\
a single test suite) or for classic dependency injection (provide tests with\
dependencies externally to the test code itself, allowing easy testing in\
different situations).

%description %_description

%if %{with_python2}
%package -n python2-%{pypi_name}
Summary: %summary
Requires:       python2-pbr
Requires:       python2-testtools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name} %_description
%endif

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Testscenarios, a pyunit extension for dependency injection
Requires:       python%{python3_pkgversion}-pbr
Requires:       python%{python3_pkgversion}-testtools

%description -n python%{python3_pkgversion}-%{pypi_name}
testscenarios provides clean dependency injection for python unittest style
tests. This can be used for interface testing (testing many implementations via
a single test suite) or for classic dependency injection (provide tests with
dependencies externally to the test code itself, allowing easy testing in
different situations).
%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove unknown test options from setup.py
sed -i '/^buffer = 1$/d' setup.cfg
sed -i '/^catch = 1$/d' setup.cfg

%build
%if %{with_python2}
%py2_build
%endif

%if %{with_python3}
%py3_build
%endif # with_python3


%install
%if %{with_python2}
%py2_install
%endif

%if %{with_python3}
%py3_install
%endif # with_python3

%check
%if %{with_python2}
%{__python2} setup.py test
%endif

%if %{with_python3}
%{__python3} setup.py test
%endif # with_python3

%if %{with_python2}
%files -n python2-%{pypi_name}
%doc GOALS HACKING NEWS README doc/
%license Apache-2.0 BSD
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%license Apache-2.0 BSD
%doc GOALS HACKING NEWS README doc/
%{python3_sitelib}/*
%endif # with_python3

%changelog
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Lumír Balhar <lbalhar@redhat.com> - 0.5.0-12
- Added tests
- Fixed dependencies
- Improved and modernized specfile

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-11
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 0.5.0-8
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-7
- Python 2 binary package renamed to python2-testscenarios
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Matthias Runge <mrunge@redhat.com> - 0.5.0-1
- update to 0.5.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 03 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4-5
- Add python3 support (RHBZ #1208889)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Matthias Runge <mrunge@redhat.com> - 0.4-2
- correct License: ASL 2.0 and BSD
- include doc files

* Fri May 17 2013 Matthias Runge <mrunge@redhat.com> - 0.4-1
- Initial package.
