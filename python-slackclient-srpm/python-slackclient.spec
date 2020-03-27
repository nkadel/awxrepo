%global pypi_name slackclient

Name:               python-%{pypi_name}
Version:            2.1.0
#Release:            2%%{?dist}
Release:            0%{?dist}
Summary:            Slack Developer Kit for Python

License:            MIT
URL:                https://github.com/slackapi/python-%{pypi_name}
Source0:            https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:          noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-websocket-client
BuildRequires:      python%{python3_pkgversion}-six
BuildRequires:      python%{python3_pkgversion}-requests
BuildRequires:      python%{python3_pkgversion}-pytest-runner
BuildRequires:      python%{python3_pkgversion}-aiodns
BuildRequires:      python%{python3_pkgversion}-aiohttp
BuildRequires:      python%{python3_pkgversion}-black
BuildRequires:      python%{python3_pkgversion}-flake8
Requires:           python%{python3_pkgversion}-websocket-client
Requires:           python%{python3_pkgversion}-six
Requires:           python%{python3_pkgversion}-requests

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}.

Python %{python3_pkgversion} version.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

# re-enable once we have python%%{python3_pkgversion}-codecov
#%check
#%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md docs/
%license LICENSE
%{python3_sitelib}/slack/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.1.0-1
- 2.1.0

* Mon May 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.0.1-1
- 2.0.1

* Fri Mar 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.1-1
- 1.3.1

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 1.3.0-1
- 1.3.0

* Mon Sep 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.1-4
- Drop Python 2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.7

* Tue Mar 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.1-1
- 1.2.1

* Thu Mar 22 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.0-1
- 1.2.0

* Fri Mar 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.1.3-1
- 1.1.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.1.2-1
- 1.1.2

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Nov 27 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.1.0-1
- 1.1.0

* Fri Sep 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.9-1
- 1.0.9

* Thu Aug 03 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.7-1
- 1.0.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.6-2
- Require python-requests.

* Wed Jul 05 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.6-1
- Initial package.
