%global desc An open source asynchronous task queue/job queue based on\
distributed message passing. It is focused on real-time\
operation, but supports scheduling as well.\
\
The execution units, called tasks, are executed concurrently\
on one or more worker nodes using multiprocessing, Eventlet\
or gevent. Tasks can execute asynchronously (in the background)\
or synchronously (wait until ready).\
\
Celery is used in production systems to process millions of\
tasks a day.\
\
Celery is written in Python, but the protocol can be implemented\
in any language. It can also operate with other languages using\
web hooks.\
\
The recommended message broker is RabbitMQ, but limited support\
for Redis, Beanstalk, MongoDB, CouchDB and databases\
(using SQLAlchemy or the Django ORM) is also available.\

# Enable python3 by default
%bcond_without python3

Name:           python-celery
Version:        4.2.1
#Release:        3%%{?dist}
Release:        0%{?dist}
BuildArch:      noarch

License:        BSD
URL:            http://celeryproject.org
Source0:        https://github.com/celery/celery/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:        Distributed Task Queue

Patch0:         https://github.com/celery/celery/pull/4852.patch#/python37.patch
BuildRequires:  git-core

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
%{desc}


%package doc
Summary: Documentation for python-celery
License: CC-BY-SA

%description doc
Documentation for python-celery.


%package -n python2-celery
Summary:        Distributed Task Queue

%{?python_provide:%python_provide python2-celery}

Requires:       python2-amqp
Requires:       python2-billiard >= 1:3.5.0.2
Requires:       python2-kombu >= 1:4.2.0
Requires:       python2-pytz
Requires:       python2-setuptools

BuildRequires:  python2-devel
BuildRequires:  python2-rpm-macros
BuildRequires:  python2-setuptools
# Not used since we don't have sphinx_celery
#BuildRequires:  python2-sphinx



%description -n python2-celery
%{desc}

%if %{with python3}
%package -n python3-celery
Summary:        Distributed Task Queue

%{?python_provide:%python_provide python3-celery}

Requires:       python3-amqp
Requires:       python3-billiard >= 1:3.5.0.2
Requires:       python3-kombu >= 1:4.2.0
Requires:       python3-pytz
Requires:       python3-setuptools

BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools


%description -n python3-celery
%{desc}

%endif


%prep
%autosetup -n celery-%{version} -p1 -S git

%if 0%{?rhel} && 0%{?rhel} < 8
# Fix setup.py for EL7 setuptools
sed -e "/python_requires=.*/d" -i setup.py
sed -e "/extras_require=.*/d" -i setup.py
%endif

%build
%py2_build
%if %{with python3}
%py3_build
%endif

pushd docs
# missing python-sphinx_celery (for the moment)
#make %{?_smp_mflags} html
popd


%install
%py2_install
pushd %{buildroot}%{_bindir}
mv celery celery-%{python2_version}
ln -s celery-%{python2_version} celery-2
popd

%if %{with python3}
%py3_install
pushd %{buildroot}%{_bindir}
mv celery celery-%{python3_version}
ln -s celery-%{python3_version} celery-3
popd
%endif

# Switch celery to Python 3 by default in F30+
pushd %{buildroot}%{_bindir}
%if 0%{?fedora} >= 30
ln -s celery-3 celery
%else
ln -s celery-2 celery
%endif
popd


%files doc
%license LICENSE


%files -n python2-celery
%license LICENSE
%doc README.rst TODO CONTRIBUTORS.txt examples
%if ! (0%{?fedora} >= 30)
%{_bindir}/celery
%endif
%{_bindir}/celery-2*
%{python2_sitelib}/celery-*.egg-info
%{python2_sitelib}/celery


%if %{with python3}
%files -n python3-celery
%license LICENSE
%doc README.rst TODO CONTRIBUTORS.txt examples
%if 0%{?fedora} >= 30
%{_bindir}/celery
%endif
%{_bindir}/celery-3*
%{python3_sitelib}/celery-*.egg-info
%{python3_sitelib}/celery
%endif


%changelog
* Mon Jan 28 2019 Neal Gompa <ngompa13@gmail.com> - 4.2.1-3
- Drop old, unused dependencies from Python 2 subpackage

* Mon Jan 28 2019 Neal Gompa <ngompa13@gmail.com> - 4.2.1-2
- Switch celery binary to Python 3 in F30+
- Switch to bconds for controlling the build
- Drop unused macro

* Wed Sep 19 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1 (#1602746).
- https://github.com/celery/celery/blob/v4.2.1/Changelog
- Correct documentation license to CC-BY-SA.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Matthias Runge <mrunge@redhat.com> - 4.2.0-2
- rebuild for python 3.7

* Mon Jun 25 2018 Carl George <carl@george.computer> - 4.2.0-1
- Latest upstream

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.1-2
- Rebuilt for Python 3.7

* Tue May 22 2018 Matthias Runge <mrunge@redhat.com> - 4.1.1-1
- update to 4.1.1 (rhbz#1474545)

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0.2-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Matthias Runge <mrunge@redhat.com> - 4.0.2-4
- clean up specfile

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Matthias Runge <mrunge@redhat.com> - 4.0.2-1
- upgrade to 4.0.x (rhbz#1400270, rhbz#1410864)
