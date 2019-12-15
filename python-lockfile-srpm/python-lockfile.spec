%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define upstream_name lockfile

Name:           python-%{upstream_name}
Version:        0.9.1
Release:        4%{?dist}
Epoch:          1
Summary:        A platform-independent file locking module

Group:          Development/Languages
License:        MIT
URL:            http://code.google.com/p/pylockfile
Source0:        http://pylockfile.googlecode.com/files/%{upstream_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
The lockfile module exports a FileLock class which provides a simple API for
locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms. The
lock mechanism relies on the atomic nature of the link (on Unix) and mkdir (on
Windows) system calls.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ACKS LICENSE MANIFEST PKG-INFO README RELEASE-NOTES doc/
%{python_sitelib}/%{upstream_name}
%{python_sitelib}/%{upstream_name}-%{version}-*.egg-info

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Silas Sewell <silas@sewell.org> - 1:0.9.1-1
- Update to 0.9.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 03 2010 Silas Sewell <silas@sewell.ch> - 1:0.8-1
- Update to 0.8, increase epoch

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 06 2010 Silas Sewell <silas@sewell.ch> - 0.9-1
- Update to 0.9

* Tue Jul 06 2010 Silas Sewell <silas@sewell.ch> - 0.8-2
- Bump for EL6 build

* Thu Jul 23 2009 Silas Sewell <silas@sewell.ch> - 0.8-1
- Initial build
