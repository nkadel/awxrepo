%global pypi_name pyrsistent

%global common_description %{expand:
Pyrsistent is a number of persistent collections (by some referred to as
functional data structures). Persistent in the sense that they are
immutable.

All methods on a data structure that would normally mutate it instead
return a new copy of the structure containing the requested updates. The
original structure is left untouched.}

%{?python_enable_dependency_generator}

Name:           python-%{pypi_name}
Summary:        Persistent/Functional/Immutable data structures
Version:        0.15.4
#Release:        1%%{?dist}
Release:        0%{?dist}
License:        MIT

URL:            http://github.com/tobgu/pyrsistent/
Source0:        %{pypi_source}

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-devel

BuildRequires:  python%{python3_pkgversion}-hypothesis
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-runner
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six

%description %{common_description}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%if ! 0%{?el7}
%check
%{__python3} setup.py test
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%license LICENCE.mit

%{python3_sitearch}/_pyrsistent_version.py
%{python3_sitearch}/__pycache__/*

%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/pvectorc.cpython-3*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info/


%changelog
* Fri Aug 02 2019 Fabio Valentini <decathorpe@gmail.com> - 0.15.4-1
- Update to version 0.15.4.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Fabio Valentini <decathorpe@gmail.com> - 0.15.3-1
- Update to version 0.15.3.

* Fri May 17 2019 Fabio Valentini <decathorpe@gmail.com> - 0.15.2-1
- Update to version 0.15.2.

* Fri Apr 26 2019 Fabio Valentini <decathorpe@gmail.com> - 0.15.1-1
- Update to version 0.15.1.

* Fri Feb 22 2019 Fabio Valentini <decathorpe@gmail.com> - 0.14.11-1
- Update to version 0.14.11.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 0.14.9-1
- Update to version 0.14.9.
- Enable the test suite.

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.2-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-4
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.2-3
- add missing dist-tag

* Fri Apr 13 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.2-2
- disable tests for now

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.2-1
- new version 0.14.2

* Wed Sep 14 2016 Devrim Gündüz <devrim@gunduz.org> 0.11.13-2
- Fix packaging errors, that would own /usr/lib64 or so.

* Tue Sep 13 2016 Devrim Gündüz <devrim@gunduz.org> 0.11.13-1
- Initial packaging for PostgreSQL YUM repository, to satisfy
  pgadmin4 dependency.

