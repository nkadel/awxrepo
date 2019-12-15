%global pypi_name testtools

%global with_python3 1

 # Skip rhel 7 because of EPEL published python2 version
%if 0%{?fedora} > 30 || 0%{?rhel} > 8
%global with_python2 0
%else
%global with_python2 1
%endif

Name:           python-%{pypi_name}
Version:        1.1.0
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        Extensions to the Python unit testing framework

%if 0%{?rhel}
Group:          Development/Tools
%endif
License:        MIT
URL:            https://launchpad.net/testtools
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         testtools-0.9.30-py3.patch

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires: epel-rpm-macros
%endif

%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-extras
BuildRequires:  python2-python-mimeparse >= 0.1.4
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
%endif
%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-extras
BuildRequires:  python%{python3_pkgversion}-python-mimeparse >= 0.1.4
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%description
testtools is a set of extensions to the Python standard library's unit testing
framework.

%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary:        Extensions to the Python unit testing framework

Requires:       python2-extras
Requires:       python2-mimeparse

%description -n python2-%{pypi_name}
testtools is a set of extensions to the Python standard library's unit testing
framework.

%endif # with_python2

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Extensions to the Python unit testing framework

Requires:       python%{python3_pkgversion}-extras
Requires:       python%{python3_pkgversion}-mimeparse

%description -n python%{python3_pkgversion}-%{pypi_name}
testtools is a set of extensions to the Python standard library's unit testing
framework.

%endif # with_python3

%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}

# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_temporary_exceptions
Provides:       bundled(jquery)

%description doc
testtools is a set of extensions to the Python standard library's unit testing
framework.

%prep
%setup -q -n %{pypi_name}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}

# make the Python 3 build load the Python 3.x compatibility library directly
pushd %{py3dir}
%patch0 -p1 -b.py3
popd

find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
rm %{py3dir}/testtools/_compat2x.py
rm testtools/_compat3x.py
%endif # with_python3


%build
%if %{with_python2}
%{__python2} setup.py build
%endif

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%if %{with_python2}
%{__python2} setup.py build
%endif

# Build docs distinctly
PYTHONPATH=$PWD make -C doc html

%install
# do python3 install first in case python-testtools ever install scripts in
# _bindir -- the one installed last should be Python 2.x's as that's the
# current default
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif # with_python3

%if %{with_python2}
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%endif

%check
%if %{with_python2}
make PYTHON=%{__python2} check || :
%endif

%if 0%{?with_python3}
pushd %{py3dir}
make PYTHON=%{__python3} check || :
popd
%endif # with_python3

%files
%if %{with_python2}
%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%doc NEWS README.rst
%license LICENSE
%{python2_sitelib}/*
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc NEWS README.rst
%license LICENSE
%{python3_sitelib}/*
%endif

%files doc
%defattr(-,root,root,-)
%doc doc/_build/html/*

%changelog
* Fri Sep 19 2014 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- Update to 1.1.0 (bz 1132881)
- Fix license handling
- Note bundling exception for jquery in -doc

* Mon Feb  3 2014 Michel Salim <salimma@fedoraproject.org> - 0.9.35-1
- Update to 0.9.35

* Thu Jul  4 2013 Michel Salim <salimma@fedoraproject.org> - 0.9.32-2
- Add new runtime dep on -extras to Python3 variant as well

* Thu Jul  4 2013 Michel Salim <salimma@fedoraproject.org> - 0.9.32-1
- Update to 0.9.32
- Switch to using split-off extras package

* Sat May 18 2013 Pádraig Brady <pbrady@redhat.com> - 0.9.30-1
- Update to 0.9.30

* Thu Feb 07 2013 Pádraig Brady <pbrady@redhat.com> - 0.9.29-1
- Update to 0.9.29

* Sat Oct 27 2012 Michel Alexandre Salim <michel@sojourner> - 0.9.21-1
- Update to 0.9.21

* Sat Oct 20 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.19-1
- Update to 0.9.19
- On Fedora, also build for Python 3.x

* Wed Sep  5 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.16-1
- Update to 0.9.16
- Remove deprecated sections

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.15-1
- Update to 0.9.15

* Thu Apr  5 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.14-1
- Update to 0.9.14
- Enable unit tests

* Tue Feb  7 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.13-1
- Update to 0.9.13

* Tue Jan 31 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.12-1
- Update to 0.9.12

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.11-1
- Update to 0.9.11
- Enable documentation generation

* Thu Apr  7 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.8-2
- Add definitions needed by older RPM versions

* Thu Apr  7 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.8-1
- Initial package
