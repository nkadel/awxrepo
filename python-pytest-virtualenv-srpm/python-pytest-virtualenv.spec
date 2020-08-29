%global pypi_name pytest-virtualenv
%global sum Virtualenv fixture for py.test

Name:           python-%{pypi_name}
Version:        1.7.0
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-setuptools_git
# needed for tests
BuildRequires:  python%{python3_pkgversion}-pytest-shutil
BuildRequires:  python%{python3_pkgversion}-pytest-fixture-config
BuildRequires:  python%{python3_pkgversion}-path
BuildRequires:  python%{python3_pkgversion}-execnet
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-contextlib2
BuildRequires:  python%{python3_pkgversion}-virtualenv

%description
Create a Python virtual environment in your test that cleans up on teardown.
The fixture has utility methods to install packages and list what's installed.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires: python%{python3_pkgversion}-contextlib2
Requires: python%{python3_pkgversion}-execnet
Requires: python%{python3_pkgversion}-path
Requires: python%{python3_pkgversion}-pytest
Requires: python%{python3_pkgversion}-pytest-fixture-config
Requires: python%{python3_pkgversion}-pytest-shutil
Requires: python%{python3_pkgversion}-virtualenv

%description -n python%{python3_pkgversion}-%{pypi_name}
Create a Python virtual environment in your test that cleans up on teardown.
The fixture has utility methods to install packages and list what's installed.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
# Upstream pins pytest to older than 4.0.0 until they finish cleaning up deprecications. 
# However, we have no choice and all the tests do pass fine, so we unpin here.
sed -i -e 's|pytest<4.0.0|pytest|' setup.py
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md CHANGES.md
%{python3_sitelib}/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-2
- Drop python2. Fixes bug #1723591

* Sun Jun 16 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-1
- Update to 1.7.0. Fixes bug #1714450

* Sun Apr 14 2019 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Update to 1.6.0. Fixes bug #1697357

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.11-9
- Use sys.executable -m virtualenv (fixup repeated usage)

* Thu Aug 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.11-8
- Use sys.executable -m virtualenv

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.11-6
- Rebuilt for Python 3.7

* Wed Mar 14 2018 Tomas Orsava <torsava@redhat.com> - 1.2.11-5
- Add detection of the virtualenv-3 and virtualenv-X.Y executables

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.11-3
- Fix up Requires to pull in things it needs to function

* Sun Sep 10 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.11-2
- Added BuildRequires for tests

* Tue Aug 15 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.11-1
- Initial version. 
