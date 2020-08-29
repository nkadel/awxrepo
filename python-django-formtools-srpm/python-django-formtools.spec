%global pypi_name django-formtools

%global with_python3 1
%global with_python2 0

# skip test until test suite supports later django
%global skip_tests 1

Name:           python-%{pypi_name}
Version:        2.1
Release:        1%{?dist}
Summary:        A set of high-level abstractions for Django forms

License:        BSD
URL:            http://django-formtools.readthedocs.org/en/latest/
Source0:        %pypi_source
BuildArch:      noarch
 
%description
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%if %{with_python2}
%package -n python2-%{pypi_name}
Summary:        A set of high-level abstractions for Django forms
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-sphinx
BuildRequires:  python2-django >= 1.7
# Required for testing
BuildRequires:  python2-flake8
BuildRequires:  python2-coverage

Requires:       python2-django >= 1.7

%description -n python2-%{pypi_name}
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%package -n python2-%{pypi_name}-doc
Summary:        A set of high-level abstractions for Django forms - documentation
%{?python_provide:%python_provide python2-%{pypi_name}-doc}

Requires:       python2-%{pypi_name} = %{version}-%{release}

%description -n python2-%{pypi_name}-doc
Django's "formtools" is a set of high-level abstractions for Django forms.

This is the associated documentation.
%endif

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        A set of high-level abstractions for Django forms
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-django >= 1.7
# Required for testing
BuildRequires:  python%{python3_pkgversion}-flake8
BuildRequires:  python%{python3_pkgversion}-coverage

Requires:       python%{python3_pkgversion}-django >= 1.7

%description -n python%{python3_pkgversion}-%{pypi_name}
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%package -n python%{python3_pkgversion}-%{pypi_name}-doc
Summary:        A set of high-level abstractions for Django forms - documentation
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}-doc}

Requires:       python%{python3_pkgversion}-%{pypi_name} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{pypi_name}-doc
Django's "formtools" is a set of high-level abstractions for Django forms.

This is the associated documentation.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with_python2}
%{py2_build}
%endif

%if %{with_python3}
%{py3_build}
%endif

%if 0%{?skip_tests} == 0
%check
%if %{with_python2}
PYTHONPATH=. DJANGO_SETTINGS_MODULE=tests.settings python-coverage run %{python2_sitelib}/django/bin/django-admin.py test tests
%endif

%if %{with_python3}
PYTHONPATH=. DJANGO_SETTINGS_MODULE=tests.settings python%{python3_pkgversion}-coverage run %{python3_sitelib}/django/bin/django-admin.py test tests
%endif
%endif

%install
%if %{with_python2}
%{py2_install}
%find_lang django py2lang
# generate html docs 
sphinx-build-%{python3_version} docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%if %{with_python3}
%{py3_install} 
%find_lang django py3lang
%endif

%if %{with_python2}
%files -n python2-%{pypi_name} -f py2lang
%doc README.rst
%license LICENSE
%{python2_sitelib}/formtools
%{python2_sitelib}/django_formtools-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name} -f py3lang
%doc README.rst
%license LICENSE
%{python3_sitelib}/formtools
%{python3_sitelib}/django_formtools-%{version}-py?.?.egg-info
# find_lang will find both python2 and python3 locale files
%exclude %{python2_sitelib}/formtools/locale

%files -n python%{python3_pkgversion}-%{pypi_name}-doc
%if %{with_python2}
doc html
%endif
%license LICENSE
%endif


%changelog
* Fri Oct 20 2017 Javier Peña <jpena@redhat.com> - 2.1-1
- Updated to upstream release 2.1
- Fixed Source0 URL

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 jpena <jpena@redhat.com> - 1.0-6
- Fixed tests

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 10 2015 jpena <jpena@redhat.com> - 1.0-4
- Moved documentation into a subpackage
* Wed Sep 09 2015 jpena <jpena@redhat.com> - 1.0-3
- Handle locale files properly
* Wed Sep 09 2015 jpena <jpena@redhat.com> - 1.0-2
- Fixed python3 conditional in files section
- Added checks
- Moved sphinx-build to install section
* Tue Sep 08 2015 jpena <jpena@redhat.com> - 1.0-1
- Initial package.
