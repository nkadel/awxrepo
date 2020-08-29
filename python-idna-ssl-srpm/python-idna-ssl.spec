%{?python_enable_dependency_generator}
%global pypi_name idna-ssl

# Circular dependency with aiohttp
%bcond_with check

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        4%{?dist}
Summary:        Patch ssl.match_hostname for Unicode(idna) domains support

License:        MIT
URL:            https://github.com/aio-libs/idna_ssl
Source0:        %pypi_source

BuildArch:      noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with check}
BuildRequires:  python%{python3_pkgversion}-pytest-runner
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
BuildRequires:  python%{python3_pkgversion}-pytest-cov
BuildRequires:  python%{python3_pkgversion}-aiohttp > 2.3
BuildRequires:  python%{python3_pkgversion}-idna >= 2
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modanme}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
%{__python3} setup.py pytest
%endif

%files
%license LICENSE
%doc README.rst example.py
%{python3_sitelib}/idna_ssl-*.egg-info/
%{python3_sitelib}/idna_ssl.py
%{python3_sitelib}/__pycache__/idna_ssl.*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.7

* Sat Feb 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package
