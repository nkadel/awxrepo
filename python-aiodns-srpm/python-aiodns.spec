# set upstream name variable
%global srcname aiodns



Name:           python-aiodns
Version:        2.0.0
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        Simple DNS resolver for asyncio

License:        MIT
URL:            https://github.com/saghul/aiodns
Source0:        https://github.com/saghul/%{srcname}/archive/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
aiodns provides a simple way for doing asynchronous DNS resolutions
with a synchronous looking interface by using pycares.


%package     -n python%{python3_pkgversion}-%{srcname}
Summary:        Simple DNS resolver for asyncio
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pycares
Requires:       python%{python3_pkgversion}-pycares
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
aiodns provides a simple way for doing asynchronous DNS resolutions
with a synchronous looking interface by using pycares.



%prep
%autosetup -n %{srcname}-%{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
# Unit tests perform DNS resolution and requires active Internet
# connection: disabling
##%{__python3} setup.py test



%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst ChangeLog
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info/
%{python3_sitelib}/%{srcname}/



%changelog
* Sun Aug 25 2019 Matthieu Saulnier <fantom@fedoraproject.org> - 2.0.0-1
- Bump version to 2.0.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.1-5
- Subpackage python2-aiodns has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.7

* Wed Apr 18 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 1.1.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Apr  4 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.1.1-1
- Initial package
