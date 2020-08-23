# what it's called on pypi
%global srcname asgiref
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global _description \
ASGI is a standard for Python asynchronous web apps and servers to communicate\
with each other, and positioned as an asynchronous successor to WSGI.  This\
package includes ASGI base libraries, such as:\
\
* Sync-to-async and async-to-sync function wrappers, asgiref.sync\
* Server base classes, asgiref.server\
* A WSGI-to-ASGI adapter, in asgiref.wsgi

%bcond_without tests


Name:           python-%{pkgname}
Version:        3.2.5
#Release:        3%{?dist}
Release:        0%{?dist}
Summary:        ASGI specs, helper code, and adapters
License:        BSD
URL:            https://github.com/django/asgiref
# PyPI tarball doesn't have tests
#Source0:        %pypi_source
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif
%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest >= 3.3
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
BuildRequires:  python%{python3_pkgversion}-async-timeout >= 2.0
%endif
# For RHEL
Requires:       python%{python3_pkgversion}-async-timeout >= 2.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose tests
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Carl George <carl@george.computer> - 2.3.2-1
- Initial package
