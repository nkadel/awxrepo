%global with_python3 1
%if 0%{?fedora} > 30 || 0%{?rhel} > 8
%global with_python2 0
%else
%global with_python2 1
%endif

Name:           python-extras
Version:        0.0.3
#Release:        2%%{?dist}
Release:        0%{?dist}
Summary:        Useful extra bits for Python

License:        MIT
URL:            https://github.com/testing-cabal/extras
Source0:        https://pypi.python.org/packages/source/e/extras/extras-%{version}.tar.gz

BuildArch:      noarch
%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif
%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%description
extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.

%if 0%{?with_python2}
%package -n python2-extras
Summary:        Useful extra bits for Python
%{?python_provide:%python_provide python2-%{pypi_name}}
# EPEL 7 has unqualified packages
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} = %{version}-%{release}

%description -n python2-extras
extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.
%endif # with_python2

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-extras
Summary:        Useful extra bits for Python
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-extras
extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.
%endif # with_python3


%prep
%setup -q -n extras-%{version}
# Remove bundled egg-info
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}

find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

%if %{?with_python2}
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif

%build
%if %{?with_python2}
%{__python2} setup.py build
%endif

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3


%install

# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif # with_python3

%if %{?with_python2}
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%endif


%if 0%{?with_python2}
%files -n python2-extras
%doc LICENSE NEWS README.rst
# For noarch packages: sitelib
%{python2_sitelib}/*
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-extras
%doc LICENSE NEWS README.rst
%{python3_sitelib}/*
%endif # with_python3


%changelog
* Sun Dec 13 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.0.3-0
- Port to RHEL 8
- Split python2 and python3 packages
- Obsolete python-extras package

* Wed May 29 2013 Matthias Runge <mrunge@redhat.com> - 0.0.3-2
- spec cleanup and enable tests

* Wed May  1 2013 Michel Salim <salimma@fedoraproject.org> - 0.0.3-1
- Initial package
