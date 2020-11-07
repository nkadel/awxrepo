%global  debug_package %{nil}
%global _prefix /opt/awx
%global _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%global service_user awx
%global service_group awx
%global service_homedir /var/lib/awx
%global service_logdir /var/log/tower
%global service_configdir /etc/tower

%global awx_mainversion 15.0.1.1
%global awx_subversion %{nil}

Summary: Ansible AWX
Name: ansible-awx
Version: %{awx_mainversion}%{awx_subversion}
Release: 0%{?dist}
# Pulled from git repo tag
Source0: awx-%{version}.tar.gz
Source1: settings.py.dist
%if 0%{?el7}
Source2: awx-cbreceiver.service
Source3: awx-dispatcher.service
Source5: awx-channels-worker.service
Source6: awx-daphne.service
Source7: awx-web.service
%endif
Source8: nginx.conf.example
Source9: awx-create-venv.sh
Source10: awx-rpm-logo.svg
Source11: awx.service
License: GPLv3
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: git
BuildRequires: libcurl-devel
BuildRequires: libffi-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: libxslt-devel
BuildRequires: openldap-devel
BuildRequires: postgresql-server >= 10
BuildRequires: postgresql-server-devel >= 10
BuildRequires: xmlsec1-devel
BuildRequires: xmlsec1-openssl-devel

BuildRequires: python%{python3_pkgversion}-asgiref
BuildRequires: python%{python3_pkgversion}-oauth2_provider
BuildRequires: python%{python3_pkgversion}-pytz
BuildRequires: python%{python3_pkgversion}-sqlparse


#BuildRequires: python%%{python3_pkgversion}-adal = 1.2.2               # via msrestazure
#BuildRequires: python%%{python3_pkgversion}-aiohttp = 3.6.2            # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-aioredis = 1.3.1           # via channels-redis
#BuildRequires: python%%{python3_pkgversion}-ansible-runner = 1.4.6     # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-ansiconv = 1.0.0           # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-asgiref = 3.2.5            # via channels, channels-redis, daphne
#BuildRequires: python%%{python3_pkgversion}-async-timeout = 3.0.1      # via aiohttp, aioredis
#BuildRequires: python%%{python3_pkgversion}-attrs = 19.3.0             # via aiohttp, automat, jsonschema, service-identity, twisted
#BuildRequires: python%%{python3_pkgversion}-autobahn = 20.3.1          # via daphne
#BuildRequires: python%%{python3_pkgversion}-automat = 20.2.0           # via twisted
#BuildRequires: python%%{python3_pkgversion}-azure-common = 1.1.25      # via azure-keyvault
#BuildRequires: python%%{python3_pkgversion}-azure-keyvault = 1.1.0     # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-azure-nspkg = 3.0.2        # via azure-keyvault
#BuildRequires: python%%{python3_pkgversion}-boto = 2.49.0              # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-cachetools = 4.0.0         # via google-auth
#BuildRequires: python%%{python3_pkgversion}-certifi = 2019.11.28       # via kubernetes, msrest, requests
#BuildRequires: python%%{python3_pkgversion}-cffi = 1.14.0              # via cryptography
#BuildRequires: python%%{python3_pkgversion}-channels-redis = 2.4.2     # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-channels = 2.4.0           # via -r /awx_devel/requirements/requirements.in, channels-redis
#BuildRequires: python%%{python3_pkgversion}-chardet = 3.0.4            # via aiohttp, requests
#BuildRequires: python%%{python3_pkgversion}-constantly = 15.1.0        # via twisted
#BuildRequires: python%%{python3_pkgversion}-cryptography = 2.8         # via adal, autobahn, azure-keyvault, pyopenssl, service-identity, social-auth-core
#BuildRequires: python%%{python3_pkgversion}-daphne = 2.4.1             # via -r /awx_devel/requirements/requirements.in, channels
#BuildRequires: python%%{python3_pkgversion}-defusedxml = 0.6.0         # via python3-openid, python3-saml, social-auth-core
#BuildRequires: python%%{python3_pkgversion}-dictdiffer = 0.8.1         # via openshift
#BuildRequires: python%%{python3_pkgversion}-django-auth-ldap = 2.1.0   # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-cors-headers = 3.2.1  # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-crum = 0.7.5        # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-extensions = 2.2.9  # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-jsonfield = 1.2.0   # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-oauth-toolkit = 1.1.3  # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-pglocks = 1.0.4     # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-polymorphic = 2.1.2  # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-qsstats-magic = 1.1.0  # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-radius = 1.3.3      # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-redis = 4.5.0       # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-solo = 1.1.3        # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-split-settings = 1.0.0  # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django-taggit = 1.2.0      # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-django = 2.2.11            # via -r /awx_devel/requirements/requirements.in, channels, django-auth-ldap, django-cors-headers, django-crum, django-jsonfield, django-oauth-toolkit, django-polymorphic, django-taggit, djangorestframework
#BuildRequires: python%%{python3_pkgversion}-djangorestframework-yaml = 1.0.3  # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-djangorestframework = 3.11.0  # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-docutils = 0.16            # via python-daemon
#BuildRequires: python%%{python3_pkgversion}-future = 0.16.0            # via django-radius
#BuildRequires: python%%{python3_pkgversion}-gitdb = 4.0.2              # via gitpython
#BuildRequires: python%%{python3_pkgversion}-gitpython = 3.1.0          # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-google-auth = 1.11.3       # via kubernetes
#BuildRequires: python%%{python3_pkgversion}-hiredis = 1.0.1            # via aioredis
#BuildRequires: python%%{python3_pkgversion}-hyperlink = 19.0.0         # via twisted
#BuildRequires: python%%{python3_pkgversion}-idna-ssl = 1.1.0           # via aiohttp
#BuildRequires: python%%{python3_pkgversion}-idna = 2.9                 # via hyperlink, idna-ssl, requests, twisted, yarl
#BuildRequires: python%%{python3_pkgversion}-importlib-metadata = 1.5.0  # via importlib-resources, irc, jsonschema
#BuildRequires: python%%{python3_pkgversion}-importlib-resources = 1.4.0  # via jaraco.text
#BuildRequires: python%%{python3_pkgversion}-incremental = 17.5.0       # via twisted
#BuildRequires: python%%{python3_pkgversion}-irc = 18.0.0               # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-isodate = 0.6.0            # via msrest, python3-saml
#BuildRequires: python%%{python3_pkgversion}-jaraco.classes = 3.1.0     # via jaraco.collections
#BuildRequires: python%%{python3_pkgversion}-jaraco.collections = 3.0.0  # via irc
#BuildRequires: python%%{python3_pkgversion}-jaraco.functools = 3.0.0   # via irc, jaraco.text, tempora
#BuildRequires: python%%{python3_pkgversion}-jaraco.logging = 3.0.0     # via irc
#BuildRequires: python%%{python3_pkgversion}-jaraco.stream = 3.0.0      # via irc
#BuildRequires: python%%{python3_pkgversion}-jaraco.text = 3.2.0        # via irc, jaraco.collections
#BuildRequires: python%%{python3_pkgversion}-jinja2 = 2.11.2            # via -r /awx_devel/requirements/requirements.in, openshift
#BuildRequires: python%%{python3_pkgversion}-jsonschema = 3.2.0         # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-kubernetes = 11.0.0        # via openshift
#BuildRequires: python%%{python3_pkgversion}-lockfile = 0.12.2          # via python-daemon
#BuildRequires: python%%{python3_pkgversion}-lxml = 4.5.0               # via xmlsec
#BuildRequires: python%%{python3_pkgversion}-markdown = 3.2.1           # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-markupsafe = 1.1.1         # via jinja2
#BuildRequires: python%%{python3_pkgversion}-more-itertools = 8.2.0     # via irc, jaraco.classes, jaraco.functools
#BuildRequires: python%%{python3_pkgversion}-msgpack = 0.6.2            # via channels-redis
#BuildRequires: python%%{python3_pkgversion}-msrest = 0.6.11            # via azure-keyvault, msrestazure
#BuildRequires: python%%{python3_pkgversion}-msrestazure = 0.6.3        # via azure-keyvault
#BuildRequires: python%%{python3_pkgversion}-multidict = 4.7.5          # via aiohttp, yarl
#BuildRequires: python%%{python3_pkgversion}-netaddr = 0.7.19           # via pyrad
#BuildRequires: python%%{python3_pkgversion}-oauthlib = 3.1.0           # via django-oauth-toolkit, requests-oauthlib, social-auth-core
#BuildRequires: python%%{python3_pkgversion}-openshift = 0.11.0         # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-pexpect = 4.7.0            # via -r /awx_devel/requirements/requirements.in, ansible-runner
#BuildRequires: python%%{python3_pkgversion}-pkgconfig = 1.5.1          # via xmlsec
#BuildRequires: python%%{python3_pkgversion}-prometheus-client = 0.7.1  # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-psutil = 5.7.0             # via ansible-runner
#BuildRequires: python%%{python3_pkgversion}-psycopg2 = 2.8.4           # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-ptyprocess = 0.6.0         # via pexpect
#BuildRequires: python%%{python3_pkgversion}-pyasn1-modules = 0.2.8     # via google-auth, python-ldap, service-identity
#BuildRequires: python%%{python3_pkgversion}-pyasn1 = 0.4.8             # via pyasn1-modules, python-ldap, rsa, service-identity
#BuildRequires: python%%{python3_pkgversion}-pycparser = 2.20           # via cffi
#BuildRequires: python%%{python3_pkgversion}-pygerduty = 0.38.2         # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-pyhamcrest = 2.0.2         # via twisted
#BuildRequires: python%%{python3_pkgversion}-pyjwt = 1.7.1              # via adal, social-auth-core, twilio
#BuildRequires: python%%{python3_pkgversion}-pyopenssl = 19.1.0         # via twisted
#BuildRequires: python%%{python3_pkgversion}-pyparsing = 2.4.6          # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-pyrad = 2.3                # via django-radius
#BuildRequires: python%%{python3_pkgversion}-pyrsistent = 0.15.7        # via jsonschema
#BuildRequires: python%%{python3_pkgversion}-python-daemon = 2.2.4      # via ansible-runner
#BuildRequires: python%%{python3_pkgversion}-python-dateutil = 2.8.1    # via adal, kubernetes
#BuildRequires: python%%{python3_pkgversion}-python-ldap = 3.2.0        # via django-auth-ldap
#BuildRequires: python%%{python3_pkgversion}-python-radius = 1.0        # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-python-string-utils = 1.0.0  # via openshift
#BuildRequires: python%%{python3_pkgversion}-python3-openid = 3.1.0     # via social-auth-core
#BuildRequires: python%%{python3_pkgversion}-python3-saml = 1.9.0       # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-pytz = 2019.3              # via django, irc, tempora, twilio
#BuildRequires: python%%{python3_pkgversion}-pyyaml = 5.3.1             # via -r /awx_devel/requirements/requirements.in, ansible-runner, djangorestframework-yaml, kubernetes
#BuildRequires: python%%{python3_pkgversion}-redis = 3.4.1              # via -r /awx_devel/requirements/requirements.in, django-redis
#BuildRequires: python%%{python3_pkgversion}-requests-oauthlib = 1.3.0  # via kubernetes, msrest, social-auth-core
#BuildRequires: python%%{python3_pkgversion}-requests = 2.23.0          # via -r /awx_devel/requirements/requirements.in, adal, azure-keyvault, django-oauth-toolkit, kubernetes, msrest, requests-oauthlib, slackclient, social-auth-core, twilio
#BuildRequires: python%%{python3_pkgversion}-rsa = 4.0                  # via google-auth
#BuildRequires: python%%{python3_pkgversion}-ruamel.yaml.clib = 0.2.0   # via ruamel.yaml
#BuildRequires: python%%{python3_pkgversion}-ruamel.yaml = 0.16.10      # via openshift
#BuildRequires: python%%{python3_pkgversion}-schedule = 0.6.0           # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-service-identity = 18.1.0  # via twisted
#BuildRequires: python%%{python3_pkgversion}-six = 1.14.0               # via ansible-runner, automat, cryptography, django-extensions, django-pglocks, google-auth, isodate, jaraco.collections, jaraco.logging, jaraco.text, jsonschema, kubernetes, openshift, pygerduty, pyopenssl, pyrad, pyrsistent, python-dateutil, slackclient, social-auth-app-django, social-auth-core, tacacs-plus, twilio, txaio, websocket-client
#BuildRequires: python%%{python3_pkgversion}-slackclient = 1.1.2        # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-smmap = 3.0.1              # via gitdb
#BuildRequires: python%%{python3_pkgversion}-social-auth-app-django = 3.1.0  # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-social-auth-core = 3.3.1   # via -r /awx_devel/requirements/requirements.in, social-auth-app-django
#BuildRequires: python%%{python3_pkgversion}-sqlparse = 0.3.1           # via django
#BuildRequires: python%%{python3_pkgversion}-tacacs_plus = 1.0          # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-tempora = 2.1.0            # via irc, jaraco.logging
#BuildRequires: python%%{python3_pkgversion}-twilio = 6.37.0            # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-twisted[tls] = 20.3.0      # via -r /awx_devel/requirements/requirements.in, daphne
#BuildRequires: python%%{python3_pkgversion}-txaio = 20.1.1             # via autobahn
#BuildRequires: python%%{python3_pkgversion}-typing-extensions = 3.7.4.1  # via aiohttp
#BuildRequires: python%%{python3_pkgversion}-urllib3 = 1.25.8           # via kubernetes, requests
#BuildRequires: python%%{python3_pkgversion}-uwsgi = 2.0.18             # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-uwsgitop = 0.11            # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-websocket-client = 0.57.0  # via kubernetes, slackclient
#BuildRequires: python%%{python3_pkgversion}-xmlsec = 1.3.3             # via python3-saml
#BuildRequires: python%%{python3_pkgversion}-yarl = 1.4.2               # via aiohttp
#BuildRequires: python%%{python3_pkgversion}-zipp = 3.1.0               # via importlib-metadata, importlib-resources
#BuildRequires: python%%{python3_pkgversion}-zope.interface = 5.0.0     # via twisted

## The following packages are considered to be unsafe in a requirements file:
#BuildRequires: python%%{python3_pkgversion}-#pip = 19.3.1               # via -r /awx_devel/requirements/requirements.in
#BuildRequires: python%%{python3_pkgversion}-#setuptools = 41.6.0        # via -r /awx_devel/requirements/requirements.in, google-auth, jsonschema, kubernetes, markdown, python-daemon, zope.interface


Requires: bubblewrap
Requires: curl
Requires: git
Requires: libcurl-devel
Requires: libffi-devel
Requires: libtool-ltdl-devel
Requires: libxslt-devel
Requires: openldap-devel
Requires: postgresql-devel >= 10
Requires: sshpass
Requires: subversion
Requires: xmlsec1-devel
Requires: xmlsec1-openssl-devel

#Required: python%%{python3_pkgversion}-GitPython
#Requires: python%%{python3_pkgversion}-PyHamcrest
#Requires: python%%{python3_pkgversion}-adal
##Requires: python%%{python3_pkgversion}-adal = 1.2.2
#Requires: python%%{python3_pkgversion}-aiohttp
#Requires: python%%{python3_pkgversion}-ansible-runner
#Requires: python%%{python3_pkgversion}-attrs
#Requires: python%%{python3_pkgversion}-autobahn
#Requires: python%%{python3_pkgversion}-azure-common
#Requires: python%%{python3_pkgversion}-azure-keyvault
#Requires: python%%{python3_pkgversion}-azure-nspkg
##Requires: python%%{python3_pkgversion}-build
#Requires: python%%{python3_pkgversion}-celery
#Requires: python%%{python3_pkgversion}-certifi
#Requires: python%%{python3_pkgversion}-cffi
#Requires: python%%{python3_pkgversion}-channels
#Requires: python%%{python3_pkgversion}-chardet
#Requires: python%%{python3_pkgversion}-constantly
#Requires: python%%{python3_pkgversion}-cryptography
#Requires: python%%{python3_pkgversion}-daphne
#Requires: python%%{python3_pkgversion}-dateutil
#Requires: python%%{python3_pkgversion}-devel
#Requires: python%%{python3_pkgversion}-django
#Requires: python%%{python3_pkgversion}-django-auth-ldap
#Requires: python%%{python3_pkgversion}-django-cors-headers
#Requires: python%%{python3_pkgversion}-django-crum
#Requires: python%%{python3_pkgversion}-django-extensions
#Requires: python%%{python3_pkgversion}-django-jsonbfield
#Requires: python%%{python3_pkgversion}-django-jsonfield
#Requires: python%%{python3_pkgversion}-django-oauth-toolkit
#Requires: python%%{python3_pkgversion}-django-pglocks
#Requires: python%%{python3_pkgversion}-django-polymorphic
#Requires: python%%{python3_pkgversion}-django-solo
#Requires: python%%{python3_pkgversion}-django-taggit
#Requires: python%%{python3_pkgversion}-djangorestframework
#Requires: python%%{python3_pkgversion}-djangorestframework-yaml
#Requires: python%%{python3_pkgversion}-gitdb
#Requires: python%%{python3_pkgversion}-google-auth
#Requires: python%%{python3_pkgversion}-idna
#Requires: python%%{python3_pkgversion}-importlib-metadata
#Requires: python%%{python3_pkgversion}-incremental
#Requires: python%%{python3_pkgversion}-inflect
#Requires: python%%{python3_pkgversion}-irc
#Requires: python%%{python3_pkgversion}-isodate
#Requires: python%%{python3_pkgversion}-jaraco-classes
#Requires: python%%{python3_pkgversion}-jaraco-collections
#Requires: python%%{python3_pkgversion}-jaraco-functools
#Requires: python%%{python3_pkgversion}-jaraco-itertools
#Requires: python%%{python3_pkgversion}-jaraco-logging
#Requires: python%%{python3_pkgversion}-jaraco-stream
#Requires: python%%{python3_pkgversion}-jaraco-text
#Requires: python%%{python3_pkgversion}-jinja2
#Requires: python%%{python3_pkgversion}-jsonschema
#Requires: python%%{python3_pkgversion}-kombu
#Requires: python%%{python3_pkgversion}-kubernetes
#Requires: python%%{python3_pkgversion}-ldap
#Requires: python%%{python3_pkgversion}-markupsafe
#Requires: python%%{python3_pkgversion}-more-itertools
#Requires: python%%{python3_pkgversion}-msrest
#Requires: python%%{python3_pkgversion}-msrestazure
#Requires: python%%{python3_pkgversion}-oauthlib
#Requires: python%%{python3_pkgversion}-openid
#Requires: python%%{python3_pkgversion}-pexpect
#Requires: python%%{python3_pkgversion}-pip
#Requires: python%%{python3_pkgversion}-psutil
#Requires: python%%{python3_pkgversion}-psycopg2
#Requires: python%%{python3_pkgversion}-ptyprocess
#Requires: python%%{python3_pkgversion}-pyasn1
#Requires: python%%{python3_pkgversion}-pyasn1-modules
#Requires: python%%{python3_pkgversion}-pygerduty
##Requires: python%%{python3_pkgversion}-pygments
#Requires: python%%{python3_pkgversion}-pyjwt >= 1.7.1
#Requires: python%%{python3_pkgversion}-pyparsing
#Requires: python%%{python3_pkgversion}-pyrsistent
#Requires: python%%{python3_pkgversion}-python-logstash
#Requires: python%%{python3_pkgversion}-pytz
#Requires: python%%{python3_pkgversion}-pyyaml
#Requires: python%%{python3_pkgversion}-requests
#Requires: python%%{python3_pkgversion}-requests-futures
#Requires: python%%{python3_pkgversion}-requests-oauthlib
#Requires: python%%{python3_pkgversion}-runtime
#Requires: python%%{python3_pkgversion}-six >= 1.13.0
#Requires: python%%{python3_pkgversion}-slackclient
#Requires: python%%{python3_pkgversion}-smmap
#Requires: python%%{python3_pkgversion}-social-auth-app-django
#Requires: python%%{python3_pkgversion}-social-auth-core
#Requires: python%%{python3_pkgversion}-tempora
#Requires: python%%{python3_pkgversion}-twilio
#Requires: python%%{python3_pkgversion}-twisted >= 19.1.0
#Requires: python%%{python3_pkgversion}-txaio
#Requires: python%%{python3_pkgversion}-urllib3
#Requires: python%%{python3_pkgversion}-websocket-client
#Requires: python%%{python3_pkgversion}-wheel >= 0.33.6
#Requires: python%%{python3_pkgversion}-zipp >= 0.6.0
#Requires: python%%{python3_pkgversion}-zope-interface >= 4.7.1

# Simplified list from running aws-manage
Requires:  python%{python3_pkgversion}-asgiref
Requires:  python%{python3_pkgversion}-django
Requires:  python%{python3_pkgversion}-django-split-settings
Requires:  python%{python3_pkgversion}-oauth2_provider
Requires:  python%{python3_pkgversion}-pip
Requires:  python%{python3_pkgversion}-sqlparse


Requires(pre): /usr/sbin/useradd, /usr/bin/getent
%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx-%{awx_mainversion}

%install
# Setup build environment
echo py3_install: %{py3_install}
sleep 30
%{py3_install}

# Collect django static
cat > _awx_rpmbuild_collectstatic_settings.py <<EOF
from awx.settings.defaults import *
DEFAULTS_SNAPSHOT = {}
CLUSTER_HOST_ID = "awx-static"
STATIC_ROOT = "static/"
LOG_AGGREGATOR_AUDIT = False
EOF

export DJANGO_SETTINGS_MODULE="_awx_rpmbuild_collectstatic_settings"
export PYTHONPATH="$PYTHONPATH:."
%{__install} -d -m755 static/

# Transfer scripts
%{__sed} -i 's$/usr/bin/awx-python$%{python3}$g' %{buildroot}/usr/bin/awx-manage

PYTHONPATH=$PYTHONPATH:%{buildROOT}%{python3_sitelib} %{python3} %{buildroot}/usr/bin/awx-manage collectstatic --noinput --clear

# Cleanup
unset PYTHONPATH
unset DJANGO_SETTINGS_MODULE

%{__install} -d %{buildroot}%{service_homedir}
%{__install} -d %{buildroot}%{service_logdir}
%{__install} -d %{buildroot}%{_prefix}/bin
%{__install} -d %{buildroot}%{service_configdir}
%{__install} -d %{buildroot}/var/lib/awx/
echo %{aws_mainversion} > %{buildroot}%{service_homedir}/.tower_version

%{__install} %{_sourcedir}/settings.py.dist %{buildroot}%{service_configdir}/settings.py
%{__mv} static %{buildroot}%{_prefix}/static

%if 0%{?el7}
# Install systemd configuration
%{__install} -d %{buildroot}%{_unitdir}
for service in awx-cbreceiver awx-dispatcher awx-channels-worker awx-daphne awx-web awx; do
    %{__install} %{_sourcedir}/${service}.service %{buildroot}%{_unitdir}/
done
%endif

# Create fake python executable
%{__install} -d -m755 %{_bindir}
cat > %{buildroot}%{_bindir}/python <<"EOF"
#!/bin/sh
export AWX_SETTINGS_FILE=/etc/tower/settings.py
%{python3} \"$@\""
EOF

# Create Virtualenv folder
%{__install} -d -m755 %{buildroot}/var/lib/awx/venv

# Install docs
%{__install} %{_sourcedir}/nginx.conf.example ./

# Install VENV Script
%{__install} -m755 %{_sourcedir}/awx-create-venv %{buildroot}/usr/bin/
%{__sed} -i 's|#!/usr/bin/python$|#!%{__python3}|g' "%{buildroot}/usr/bin//awx-create-venv"
%{__install} -d -m755 %{buildroot}%{service_homedir}/venv

%{__install} %{_sourcedir}/awx-rpm-logo.svg %{buildroot}/opt/awx/static/assets/awx-rpm-logo.svg
%{__mv} %{buildroot}/opt/awx/static/assets/logo-header.svg %{buildroot}/opt/awx/static/assets/logo-header.svg.orig
%{__mv} %{buildroot}/opt/awx/static/assets/logo-login.svg %{buildroot}/opt/awx/static/assets/logo-login.svg.orig
%{__ln_s} /opt/awx/static/assets/awx-rpm-logo.svg %{buildroot}/opt/awx/static/assets/logo-header.svg
%{__ln_s} /opt/awx/static/assets/awx-rpm-logo.svg %{buildroot}/opt/awx/static/assets/logo-login.svg

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%post
%if 0%{?el7}
%systemd_post awx-cbreceiver
%systemd_post awx-dispatcher
%systemd_post awx-channels-worker
%systemd_post awx-daphne
%systemd_post awx-web
%endif
# Create symlink to /var/lib/awx/venv/awx as needed

%preun
%if 0%{?el7}
%systemd_preun awx-cbreceiver
%systemd_preun awx-dispatcher
%systemd_preun awx-channels-worker
%systemd_preun awx-daphne
%systemd_preun awx-web
%endif

%postun
%if 0%{?el7}
%systemd_postun awx-cbreceiver
%systemd_postun awx-dispatcher
%systemd_postun awx-channels-worker
%systemd_postun awx-daphne
%systemd_postun awx-web
%endif

%clean

%files
%defattr(0644, awx, awx, 0755)
%doc nginx.conf.example
%attr(0755, root, root) /usr/bin/awx-manage
%attr(0755, root, root) /usr/bin/awx-create-venv
/usr/bin/awx-create-venv
%{python3_sitelib}/awx
%attr(0755, root, root) %{python3_sitelib}/awx/plugins/*/*.py
%attr(0755, awx, awx) %{_prefix}/static
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}/venv
%{service_homedir}/.tower_version
%dir %attr(0770, %{service_user}, %{service_group}) %{service_logdir}
%config %{service_configdir}/settings.py
%{python3_sitelib}/awx-*.egg-info/
/usr/share/doc/awx/
/opt/awx/bin/python
# Not in _bindir, in /usr/bin
/usr/bin/ansible-tower-service
/usr/bin/ansible-tower-setup
/usr/bin/awx-python
/usr/bin/failure-event-handler
/usr/share/awx
/usr/share/sosreport/sos/plugins/tower.py
/var/lib/awx/favicon.ico
/var/lib/awx/wsgi.py

%if 0%{?el7}
%attr(0644, root, root) %{_unitdir}/awx-cbreceiver.service
%attr(0644, root, root) %{_unitdir}/awx-dispatcher.service
%attr(0644, root, root) %{_unitdir}/awx-channels-worker.service
%attr(0644, root, root) %{_unitdir}/awx-daphne.service
%attr(0644, root, root) %{_unitdir}/awx-web.service
%attr(0644, root, root) %{_unitdir}/awx.service
%endif

%changelog
