%global pypi_name case

# docs depend on package sphinx_celery
# https://github.com/celery/sphinx_celery
%global with_docs 0

Name:           python-%{pypi_name}
Version:        1.5.3
#Release:        2%%{?dist}
Release:        0%{?dist}
Summary:        Python unittest Utilities

License:        BSD
URL:            http://github.com/celery/case
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Python unittest Utilities
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-setuptools >= 0.7
Requires:       python%{python3_pkgversion}-nose >= 1.3.7
Requires:       python%{python3_pkgversion}-setuptools

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-coverage >= 3.0
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-unittest2
BuildRequires:  python%{python3_pkgversion}-nose

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%if 0%{?with_docs} > 0
%package -n python-%{pypi_name}-doc
Summary:        case documentation
%description -n python-%{pypi_name}-doc
Documentation for case
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%if 0%{?with_docs} > 0
# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install


%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc docs/templates/readme.txt README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_docs} > 0
%files -n python-%{pypi_name}-doc
%doc html
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Matthias Runge <mrunge@redhat.com> - 1.5.3-1
- drop python2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.2-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Matthias Runge <mrunge@redhat.com> - 1.5.2-2
- add missing builddeps: python[23]-unittest2, python[23]-nose

* Tue Dec 27 2016 Matthias Runge <mrunge@redhat.com> - 1.5.2-1
- Initial package. (rhbz#1408868)
