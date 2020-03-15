%global pypi_name pytest-asyncio
%global srcname pytest_asyncio
%global project_owner pytest-dev
%global github_name pytest-asyncio

%bcond_without  tests

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.10.0
Release:        1%{?dist}.2
Summary:        Pytest support for asyncio

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/v%{version}/%{github_name}-%{version}.tar.gz

%if 0%{rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildArch:      noarch

%description
pytest-asyncio is an Apache2 licensed library, written in Python, for testing
asyncio code with pytest.

asyncio code is usually written in the form of coroutines, which makes it
slightly more difficult to test using normal testing tools. pytest-asyncio
provides useful fixtures and markers to make testing easier.

%package -n python%{python3_pkgversion}
Summary:        Pytest support for asyncio


BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest >= 3.0.6
#BuildRequires:  %py3_dist coverage
BuildRequires:  python%{python3_pkgversion}-coverage
BuildRequires:  python%{python3_pkgversion}-async-generator >= 1.3
# RHEL8.0 has 3.44.24, but we really need 3.64
BuildRequires:  python%{python3_pkgversion}-hypothesis
# For checks
BuildRequires:  python%{python3_pkgversion}-more-itertools >= 4.0.0
%endif
Requires:       python%{python3_pkgversion}-pytest >= 3.0.6
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}
pytest-asyncio is an Apache2 licensed library, written in Python, for testing
asyncio code with pytest.

asyncio code is usually written in the form of coroutines, which makes it
slightly more difficult to test using normal testing tools. pytest-asyncio
provides useful fixtures and markers to make testing easier.

%prep
%setup -qn %{github_name}-%{version}

# Don't treat all warnings as errors, there are DeprecationWarnings on 3.8
sed -i '/filterwarnings = error/d' setup.cfg

# Support pytest 3.4.2 in EL8
sed -i -e 's/get_closest_marker/get_marker/' pytest_asyncio/plugin.py
# Allow older hypothesis in EL8
sed -i -e '/hypothesis/s/ >= 3.64//' setup.py



%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
# Skip tests that require a newer hypothesis
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} --verbose -k 'not test_mark_inner and not test_mark_outer and not test_mark_and_parametrize'
%endif


%files -n python%{python3_pkgversion}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Sun Oct 13 2019 Orion Poplawski <orion@nwra.com> - 0.10.0-1.2
- Support pytest 3.4.2 in EL8 (bugz#1761169)
- Re-enable tests for EPEL8
- Avoid issues with older hypothesis for now

* Wed Jun 19 2019 Troy Dawson <tdawson@redhat.com> - 0.10.0-1.1
- Turn off tests for EPEL8

* Thu Apr 18 2019 Carl George <carl@george.computer> - 0.10.0-1
- Latest upstream
- Run test suite

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Julien Enselme <jujens@jujens.eu> - 0.9.0-1
- Update to 0.9.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4.git18535c3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3.git18535c3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2.git18535c3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 <jujens@jujens.eu> - 0.8.0-1.git18535c3
- Update to 0.8.0

* Thu Sep 14 2017 <jujens@jujens.eu> - 0.7.0-1.git2407487
- Update to 0.7.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2.git72a6c2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Julien Enselme <jujens@jujens.eu> - 0.6.0-1.git72a6c2b
- Update to 0.6.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4.git917d8a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3.git917d8a8
- Rebuild for Python 3.6

* Mon Oct 10 2016 Julien Enselme <jujens@jujens.eu> - 0.5.0-2.git917d8a8
- Bump version

* Wed Sep 07 2016 Julien Enselme <jujens@jujens.eu> - 0.5.0-1.git917d8a8
- Update to 0.5.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2.git64b79e1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jun 05 2016 Julien Enselme <jujens@jujens.eu> - 0.4.1-1.git64b79e1
- Update to 0.4.1

* Wed Jun 01 2016 Julien Enselme <jujens@jujens.eu> - 0.4.0-1.gitb4a4bf8
- Update to 0.4.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2.gitae9b430
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Julien Enselme <jujens@jujens.eu> - 0.3.0-1.gitae9b430
- Update to 0.3.0 (bz:1293083)

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.1.3-3.git2a4c7e6
- Rebuilt for python 3.5

* Sun Aug 2 2015 Julien Enselme <jujens@jujens.eu> - 0.1.3-2.git2a4c7e6
- Add %%python_provide

* Sat Aug 1 2015 Julien Enselme <jujens@jujens.eu> - 0.1.3-1.git2a4c7e6
- Initial package
