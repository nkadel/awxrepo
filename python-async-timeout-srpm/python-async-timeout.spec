%global pypi_name async-timeout
%global common_desc asyncio-compatible timeout context manager\
The context manager is useful in cases when you want to apply timeout\
logic around block of code or in cases when asyncio.wait_for() is not \
suitable. Also it's much faster than asyncio.wait_for() because timeout\
doesn't create a new task.

Name:           python-%{pypi_name}
Version:        3.0.1
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        An asyncio-compatible timeout context manager

License:        ASL 2.0
URL:            https://github.com/aio-libs/async-timeout
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
%{common_desc}

# This module is Python 3 only
%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-pytest-runner
# Excluded for circular dependency
#BuildRequires: python%%{python3_pkgversion}-pytest-aiohttp
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst CHANGES.rst
%{python3_sitelib}/async_timeout/
%{python3_sitelib}/async_timeout-*.egg-info/

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.1-2
- Enable tests

* Mon May 06 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.1-1
- Update to latest upstream release 3.0.1 (rhbz#1707011)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.7

* Sat May 05 2018 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-1
- Update to latest upstream release 3.0.0 (rhbz#1575247)

* Thu Mar 15 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.1-1
- Update to latest upstream release 2.0.1 (rhbz#1554798)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 17 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (rhbz #1484848)

* Fri Aug 25 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0 (rhbz#1484848)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sun Mar 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuild for Python 3.6

* Thu Nov 17 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.0-3
- Add missing BR
- Rename the pkg

* Sun Nov 13 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.0-2
- Update files section and the description

* Fri Nov 11 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.0-1
- Initial spec

