%global pypi_name sortedcontainers

Name:           python-%{pypi_name}
Version:        2.1.0
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        Pure Python sorted container types

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
# PyPI tarball does not include docs or tests.
Source0:        %pypi_source

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%global _description \
SortedContainers is an Apache2 licensed sorted collections library, written in \
pure-Python, and fast as C-extensions.

%description %{_description}

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-matplotlib
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-scipy
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  dvipng
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(bm.sty)

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}


%package -n python-%{pypi_name}-doc
Summary:        %{summary}

%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name} package.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

# Apparently discarded in more recent versions
#pushd docs
#make SPHINXBUILD=sphinx-build-%{python3_version} html
#rm _build/html/.buildinfo
#popd

%install
%py3_install


#%check
# Apparently discarded in more recent versions
#PYTHONPATH="%{buildroot}%{python3_sitelib}" \
#    pytest-%{python3_version}

# standard format, not available for this module
#%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%files -n python-%{pypi_name}-doc
%license LICENSE
%doc README.rst

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- Update to latest version

* Sat Oct 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.5-1
- Update to latest version

* Wed Oct 03 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.4-2
- Drop Python 2 subpackage.

* Thu Aug 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.4-1
- Update to latest version.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.7

* Sat May 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Update to latest version.

* Sun Apr 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.10-1
- Update to latest version.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.9-1
- Update to latest version.

* Sun Sep 03 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.7-3
- Split out documentation subpackage.

* Sat Sep 02 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.7-2
- Shorten summary and description.
- Standardize spec a bit more.

* Mon Feb 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.7-1
- Initial package release.
