%global pypi_name requests-futures
%bcond_with network

Name:           python-%{pypi_name}
Version:        1.0.0
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        Asynchronous Python HTTP Requests

License:        ASL 2.0
URL:            https://github.com/ross/requests-futures
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
Small add-on for the Python requests http library. Makes use of Python 3.2’s
concurrent.futures or the back-port for prior versions of Python.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Small add-on for the Python requests http library. Makes use of Python 3.2’s
concurrent.futures or the backport for prior versions of Python.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%if %{with network}
pytest-%{python3_version} -v test_requests_futures.py
%else
pytest-%{python3_version} test_requests_futures.py::RequestsTestCase::test_adapter_kwargs \
  test_requests_futures.py::RequestsTestCase::test_max_workers
%endif


%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/requests_futures/
%{python3_sitelib}/requests_futures*.egg-info

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-2
- Condition for test with network

* Sat Dec 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Initial package for Fedora
