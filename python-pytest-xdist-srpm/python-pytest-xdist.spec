%global pypi_name pytest-xdist
%global desc The pytest-xdist plugin extends py.test with some unique test execution modes:\
* test run parallelization: if you have multiple CPUs or hosts you can use\
  those for a combined test run. This allows to speed up development or to use\
  special resources of remote machines.\
* --boxed: run each test in a boxed subprocess to survive SEGFAULTS or\
  otherwise dying processes\
* --looponfail: run your tests repeatedly in a subprocess. After each run\
  py.test waits until a file in your project changes and then re-runs the\
  previously failing tests. This is repeated until all tests pass after which\
  again a full run is performed.\
* Multi-Platform coverage: you can specify different Python interpreters or\
  different platforms and run tests in parallel on all of them.

Name:           python-%{pypi_name}
Version:        1.29.0
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        py.test plugin for distributed testing and loop-on-failing modes

License:        MIT
URL:            https://github.com/pytest-dev/pytest-xdist
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-execnet
BuildRequires:  python%{python3_pkgversion}-filelock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-forked
BuildRequires:  python%{python3_pkgversion}-py
BuildRequires:  python%{python3_pkgversion}-setuptools_scm

%description
%{desc}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-execnet
Requires:       python%{python3_pkgversion}-pytest
Requires:       python%{python3_pkgversion}-pytest-forked
Requires:       python%{python3_pkgversion}-py
%description -n python%{python3_pkgversion}-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 py.test-%{python3_version} testing


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc OVERVIEW.md README.rst
%license LICENSE
%{python3_sitelib}/pytest_xdist*
%{python3_sitelib}/xdist/

%changelog
* Thu Aug 08 2019 Scott Talbert <swt@techie.net> - 1.29.0-3
- Remove Python 2 subpackages (#1737399)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Scott Talbert <swt@techie.net> - 1.29.0-1
- Update to new upstream release 1.29.0 (#1720870)

* Thu Apr 18 2019 Scott Talbert <swt@techie.net> - 1.28.0-1
- New upstream release 1.28.0

* Fri Mar 22 2019 Scott Talbert <swt@techie.net> - 1.27.0-1
- New upstream release 1.27.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Scott Talbert <swt@techie.net> - 1.26.1-1
- New upstream release 1.26.1

* Tue Jan 22 2019 Scott Talbert <swt@techie.net> - 1.26.0-1
- New upstream release 1.26.0

* Sat Dec 15 2018 Scott Talbert <swt@techie.net> - 1.25.0-1
- New upstream release 1.25.0

* Sun Nov 11 2018 Scott Talbert <swt@techie.net> - 1.24.1-1
- New upstream release 1.24.1

* Wed Oct 31 2018 Scott Talbert <swt@techie.net> - 1.24.0-1
- New upstream release 1.24.0

* Fri Oct 19 2018 Scott Talbert <swt@techie.net> - 1.23.2-1
- New upstream release 1.23.2

* Sat Jul 28 2018 Scott Talbert <swt@techie.net> - 1.22.5-1
- New upstream release 1.22.5

* Tue Jul 24 2018 Scott Talbert <swt@techie.net> - 1.22.3-1
- New upstream release 1.22.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.22.2-2
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Scott Talbert <swt@techie.net> - 1.22.2-1
- New upstream release 1.22.2

* Wed Feb 21 2018 Scott Talbert <swt@techie.net> - 1.22.1-1
- New upstream release 1.22.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Scott Talbert <swt@techie.net> - 1.22.0-1
- New upstream release 1.22.0

* Fri Dec 29 2017 Scott Talbert <swt@techie.net> - 1.21.0-1
- New upstream release 1.21.0

* Mon Nov 20 2017 Scott Talbert <swt@techie.net> - 1.20.1-2
- Avoid packaging -PYTEST.pyc files which are problematic (#1507299)

* Tue Oct 24 2017 Scott Talbert <swt@techie.net> - 1.20.1-1
- New upstream release 1.20.1

* Thu Aug 24 2017 Scott Talbert <swt@techie.net> - 1.20.0-1
- New upstream release 1.20.0

* Sat Jul 29 2017 Scott Talbert <swt@techie.net> - 1.18.2-1
- New upstream release 1.18.2

* Fri Jul 28 2017 Scott Talbert <swt@techie.net> - 1.18.1-1
- New upstream release 1.18.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Scott Talbert <swt@techie.net> - 1.18.0-1
- New upstream release 1.18.0

* Wed Jun 14 2017 Scott Talbert <swt@techie.net> - 1.17.1-1
- New upstream release 1.17.1

* Sat Jun 10 2017 Scott Talbert - 1.17.0-1
- New upstream release 1.17.0

* Tue May 09 2017 Scott Talbert <swt@techie.net> - 1.16.0-1
- New upstream release 1.16.0
- Enable tests

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-2
- Rebuild for Python 3.6

* Mon Oct 03 2016 Scott Talbert <swt@techie.net> - 1.15.0-1
- New upstream release 1.15.0

* Thu Aug 11 2016 Scott Talbert <swt@techie.net> - 1.14-1
- Initial package.
