%global pypi_name pytest-fixture-config
%global sum Simple configuration objects for Py.test fixtures

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

%description
Simple configuration objects for Py.test fixtures.
Allows you to skip tests when their required config variables aren't set.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Simple configuration objects for Py.test fixtures.
Allows you to skip tests when their required config variables aren't set.

%prep
%autosetup -n %{pypi_name}-%{version}

# https://bugzilla.redhat.com/show_bug.cgi?id=1694205
# https://github.com/manahl/pytest-plugins/pull/134
sed -i "s/'pytest<4.0.0'/'pytest'/" setup.py

%build
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
- Drop python2. Fixes bug #1723589

* Sun Jun 16 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-1
- Update to 1.7.0. Fixes bug #1714448

* Fri Apr 12 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Make the package installable with pytest 4

* Sun Mar 10 2019 Kevin Fenzi <kevin@scrye.com> - 1.4.0-1
- Update to 1.4.0. 
- Fix FTBFS, bug #1675781

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.11-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.11-2
- Add Requires for pytest

* Wed Jul 26 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.11-1
- Initial version. 
