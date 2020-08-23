%global with_python3 1
%global with_python2 0

%{!?_licensedir: %global license %%doc}

%global pypi_name django-cors-headers

Name:           python-django-cors-headers
Version:        2.0.2
Release:        9%{?dist}
Summary:        A Django application for handling CORS headers

License:        MIT
URL:            https://pypi.io/project/django-cors-headers
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:      epel-rpm-macros
%endif
%if 0%{?with_python2}
BuildRequires:      python2-devel
BuildRequires:      python2-setuptools
BuildRequires:      python2-mock
%endif

%if 0%{?with_python3}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-mock
%endif

%description
django-cors-headers is a Django application for handling the server headers
required for Cross-Origin Resource Sharing (CORS).

%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary:            A Django application for handling CORS headers
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
django-cors-headers is a Django application for handling the server headers
required for Cross-Origin Resource Sharing (CORS).
%endif

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:            A Django application for handling CORS headers
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
django-cors-headers is a Django application for handling the server headers
required for Cross-Origin Resource Sharing (CORS).
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%doc README.rst HISTORY.rst
%license LICENSE.txt
%{python2_sitelib}/corsheaders/
%{python2_sitelib}/django_cors_headers-%{version}*
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst HISTORY.rst
%license LICENSE.txt
%{python3_sitelib}/corsheaders/
%{python3_sitelib}/django_cors_headers-%{version}*
%endif

%changelog
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-7
- Rebuilt for Python 3.7

* Tue Mar 06 2018 Ralph Bean <rbean@redhat.com> - 2.0.2-6
- Make py3 package provide the old py2 name.

* Mon Mar 05 2018 Ralph Bean <rbean@redhat.com> - 2.0.2-5
- Disable python2 for https://fedoraproject.org/wiki/Changes/Django20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Ralph Bean <rbean@redhat.com> - 2.0.2-2
- Add missing doc and license declarations.

* Fri Feb 10 2017 Ralph Bean <rbean@redhat.com> - 2.0.2-1
- Latest upstream.

* Mon Jan 18 2016 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Initial packaging for Fedora.
