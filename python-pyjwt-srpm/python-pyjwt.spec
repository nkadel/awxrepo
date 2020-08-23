#
# spec file for package python-PyJWT
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Fedora >= 38 no longer publishes python2 by default
%if 0%{?fedora} >= 30
%global with_python2 0
%else
%global with_python2 1
%endif

%global pypi_name PyJWT

# Common SRPM package, renamed to pyjwt for RHEL convention
#Name:           python-%%{pypi_name}
Name:           python-pyjwt
Version:        1.7.1
Release:        0%{?dist}
Url:            http://github.com/jpadilla/pyjwt
Summary:        JSON Web Token implementation in Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
A Python implementation of `RFC 7519 <https://tools.ietf.org/html/rfc7519>`_. Original implementation was written by `@progrium <https://github.com/progrium>`_.

%if %{with_python2}
#%package -n python2-%%{pypi_name}
%package -n python2-pyjwt
Version:        1.7.1
Release:        0%{?dist}
Url:            http://github.com/jpadilla/pyjwt
Summary:        JSON Web Token implementation in Python
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}
# Add hooks for mismatched package name
%{?python_provide:%python_provide python2-pyjwt}
Conflicts: python2-%{pypi_name}
Obsoletes: python2-%{pypi_name} >= %{version}-%{release}
Provides:  python2-jwt = %{version}-%{release}
Obsoletes: python2-jwt <= %{version}-%{release}

#%description -n python2-%%{pypi_name}
%description -n python2-pyjwt
A Python implementation of `RFC 7519 <https://tools.ietf.org/html/rfc7519>`_. Original implementation was written by `@progrium <https://github.com/progrium>`_.

%endif # with_python2

%if %{with_python3}
#%package -n python%%{python3_pkgversion}-%%{pypi_name}
%package -n python%{python3_pkgversion}-pyjwt
Version:        1.7.1
Release:        0%{?dist}
Url:            http://github.com/jpadilla/pyjwt
Summary:        JSON Web Token implementation in Python
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
# Add hooks for mismatched package name
%{?python_provide:%python_provide python%{python3_pkgversion}-pyjwt}
# Added for mismatched capitalization of PyJTW
Conflicts: python%{python3_pkgversion}-%{pypi_name}
Obsoletes: python%{python3_pkgversion}-%{pypi_name} >= %{version}-%{release}
Provides:  python%{python3_pkgversion}-jwt = %{version}-%{release}
Obsoletes: python%{python3_pkgversion}-jwt <= %{version}-%{release}


#%description -n python%%{python3_pkgversion}-%%{pypi_name}
%description -n python%{python3_pkgversion}-pyjwt
A Python implementation of `RFC 7519 <https://tools.ietf.org/html/rfc7519>`_. Original implementation was written by `@progrium <https://github.com/progrium>`_.

%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with_python2}
%py2_build
%endif # with_python2

%if %{with_python3}
%py3_build
%endif # with_python3

%install
%if %{with_python2}
%py2_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/pyjwt $RPM_BUILD_ROOT%{_bindir}/pyjwt2
%{__ln_s} pyjwt2 $RPM_BUILD_ROOT%{_bindir}/pyjwt
%endif # with_python2

%if %{with_python3}
%py3_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/pyjwt $RPM_BUILD_ROOT%{_bindir}/pyjwt%{python3_pkgversion}
%{__ln_s} pyjwt%{python3_pkgversion} $RPM_BUILD_ROOT%{_bindir}/pyjwt
%endif # with_python3

%clean
rm -rf %{buildroot}

%if %{with_python2}
#%files -n python2-%{pypi_name}
%files -n python2-pyjwt
%defattr(-,root,root,-)
%{python2_sitelib}/*
%{_bindir}/pyjwt2
%if ! %{with_python3}
%{_bindir}/pyjwt
%endif
%endif # with_python2

%if %{with_python3}
#%files -n python%%{python3_pkgversion}-%%{pypi_name}
%files -n python%{python3_pkgversion}-pyjwt
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/pyjwt%{python3_pkgversion}
%{_bindir}/pyjwt
%endif # with_python3

%changelog
