%global pypi_name msrestazure
%global common_description %{summary}.

%global _with_python2 0
%global _with_python3 1

# Tests require a more recent version of requests library than the one available
# in EL
%global _with_tests 0%{?fedora}
# EL is missing recommonmark library to build documentation
%global _with_doc 0%{?fedora}
%global pydoc_prefix %{?rhel:python}%{?fedora:python%{python3_pkgversion}}
%global sphinxbuild sphinx-build%{?fedora:-%{python3_version}}

# Ignore bytecode compilation errors with Python 2 (since the library provides
# some Python 3-only files)
%global _python_bytecompile_errors_terminate_build 0

%global adal_min_version 0.6.0
%global msrest_min_version 0.4.28

Name:           python-%{pypi_name}
Version:        0.6.1
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        The runtime library "msrestazure" for AutoRest generated Python clients

License:        MIT
URL:            https://github.com/Azure/msrestazure-for-python
Source0:        %pypi_source
#Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

%if 0%{?_with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if 0%{?_with_tests}
BuildRequires:  python2-adal >= %{adal_min_version}
BuildRequires:  python2-mock
BuildRequires:  python2-msrest >= %{msrest_min_version}
BuildRequires:  %{?!rhel:python2-}pytest
BuildRequires:  python2-httpretty
%endif
%endif

%if 0%{?_with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{?_with_tests}
BuildRequires:  python%{python3_pkgversion}-adal >= %{adal_min_version}
BuildRequires:  python%{python3_pkgversion}-httpretty
BuildRequires:  python%{python3_pkgversion}-msrest >= %{msrest_min_version}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif
%endif
%if 0%{?_with_doc}
BuildRequires:  %{pydoc_prefix}-pip
BuildRequires:  %{pydoc_prefix}-recommonmark
BuildRequires:  %{pydoc_prefix}-sphinx
BuildRequires:  %{pydoc_prefix}-sphinx_rtd_theme
%endif
BuildArch:      noarch

%description
%{common_description}


%if 0%{?_with_python2}
%package -n python2-%{pypi_name}
Summary:        %{summary}
Requires:       python2-adal >= %{adal_min_version}
Requires:       python2-msrest >= %{msrest_min_version}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%{common_description}
%endif


%if 0%{?_with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-adal >= %{adal_min_version}
Requires:       python%{python3_pkgversion}-msrest >= %{msrest_min_version}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%{common_description}
%endif


%if 0%{?_with_doc}
%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.
%endif


%prep
%autosetup -n %{pypi_name}-for-python-%{version}


%build
%if 0%{?_with_python2}
%py2_build
%endif
%if 0%{?_with_python3}
%py3_build
%endif

%if 0%{?_with_doc}
pushd doc/
%{sphinxbuild} -b html -d _build/doctrees/ . _build/html/
rm _build/html/.buildinfo
popd
%endif


%install
%if 0%{?_with_python2}
%py2_install
%endif
%if 0%{?_with_python3}
%py3_install
%endif


%check
%if 0%{_with_tests}
%if 0%{?_with_python2}
py.test-%{python2_version}
%endif
%if 0%{?_with_python3}
py.test-%{python3_version}
%endif
%endif


%if 0%{?_with_python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE.md
%{python2_sitelib}/%{pypi_name}/
%{python2_sitelib}/%{pypi_name}-*.egg-info/
%endif


%if 0%{?_with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%license LICENSE.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%endif


%if 0%{?_with_doc}
%files doc
%doc doc/_build/html/
%license LICENSE.md
%endif


%changelog
* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.0-2
- Fix Python 3-only file deployment

* Mon Feb 04 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.1-2
- Rebuild for python-msrest dependency fix update

* Sun Nov 11 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1
- Build documentation
