# Created by pyp2rpm-3.3.10
%global pypi_name awx
%global pypi_version 24.6.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        AWX Satellite Data Reader

License:        None
URL:            https://github.com/ansible/awx
# AWX at pypi.org is wrong tool
#Source0:        %%{pypi_source}
Source0:        https://github.com/ansible/awx/archive/refs/tags/24.6.1.zip
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:	python3dist(adal)
BuildRequires:	python3dist(aiohttp-retry)
BuildRequires:	python3dist(aiohttp)
BuildRequires:	python3dist(aioredis)
BuildRequires:	python3dist(aiosignal)
BuildRequires:	python3dist(alabaster)
BuildRequires:	python3dist(annotated-types)
BuildRequires:	python3dist(ansible-pygments)
BuildRequires:	python3dist(ansiconv)
BuildRequires:	python3dist(asciichartpy)
BuildRequires:	python3dist(asgiref)
BuildRequires:	python3dist(asn1)
BuildRequires:	python3dist(async-timeout)
BuildRequires:	python3dist(attrs)
BuildRequires:	python3dist(autobahn)
BuildRequires:	python3dist(autocommand)
BuildRequires:	python3dist(automat)
BuildRequires:	python3dist(awxkit)
BuildRequires:	python3dist(azure-common)
BuildRequires:	python3dist(azure-core)
BuildRequires:	python3dist(azure-identity)
BuildRequires:	python3dist(azure-keyvault-certificates)
BuildRequires:	python3dist(azure-keyvault-keys)
BuildRequires:	python3dist(azure-keyvault-secrets)
BuildRequires:	python3dist(azure-keyvault)
BuildRequires:	python3dist(babel)
BuildRequires:	python3dist(boto3)
BuildRequires:	python3dist(botocore)
BuildRequires:	python3dist(cachetools)
BuildRequires:	python3dist(certifi)
BuildRequires:	python3dist(cffi)
BuildRequires:	python3dist(channels-redis)
BuildRequires:	python3dist(channels)
BuildRequires:	python3dist(charset-normalizer)
BuildRequires:	python3dist(charset-normalizer)
BuildRequires:	python3dist(click)
BuildRequires:	python3dist(constantly)
BuildRequires:	python3dist(cryptography)
BuildRequires:	python3dist(cython)
BuildRequires:	python3dist(daphne)
BuildRequires:	python3dist(defusedxml)
BuildRequires:	python3dist(deprecated)
BuildRequires:	python3dist(distro)
BuildRequires:	python3dist(django-auth-ldap)
BuildRequires:	python3dist(django-cors-headers)
BuildRequires:	python3dist(django-crum)
BuildRequires:	python3dist(django-extensions)
BuildRequires:	python3dist(django-guid)
BuildRequires:	python3dist(django-oauth-toolkit)
BuildRequires:	python3dist(django-pglocks)
BuildRequires:	python3dist(django-polymorphic)
BuildRequires:	python3dist(django-radius)
BuildRequires:	python3dist(django-solo)
BuildRequires:	python3dist(django-split-settings)
BuildRequires:	python3dist(django)
BuildRequires:	python3dist(djangorestframework-yaml)
BuildRequires:	python3dist(djangorestframework)
BuildRequires:	python3dist(docutils)
BuildRequires:	python3dist(docutils)
BuildRequires:	python3dist(ecdsa)
BuildRequires:	python3dist(enum-compat)
BuildRequires:	python3dist(filelock)
BuildRequires:	python3dist(frozenlist)
BuildRequires:	python3dist(gitdb)
BuildRequires:	python3dist(gitpython)
BuildRequires:	python3dist(google-auth)
BuildRequires:	python3dist(googleapis-common-protos)
BuildRequires:	python3dist(grpcio)
BuildRequires:	python3dist(hiredis)
BuildRequires:	python3dist(hyperlink)
BuildRequires:	python3dist(idna)
BuildRequires:	python3dist(idna)
BuildRequires:	python3dist(imagesize)
BuildRequires:	python3dist(importlib-metadata)
BuildRequires:	python3dist(incremental)
BuildRequires:	python3dist(inflect)
BuildRequires:	python3dist(inflection)
BuildRequires:	python3dist(irc)
BuildRequires:	python3dist(isodate)
BuildRequires:	python3dist(jaraco-collections)
BuildRequires:	python3dist(jaraco-context)
BuildRequires:	python3dist(jaraco-functools)
BuildRequires:	python3dist(jaraco-logging)
BuildRequires:	python3dist(jaraco-stream)
BuildRequires:	python3dist(jaraco-text)
BuildRequires:	python3dist(jinja2)
BuildRequires:	python3dist(jinja2)
BuildRequires:	python3dist(jmespath)
BuildRequires:	python3dist(json-log-formatter)
BuildRequires:	python3dist(jsonschema-specifications)
BuildRequires:	python3dist(jsonschema)
BuildRequires:	python3dist(jwcrypto)
BuildRequires:	python3dist(kubernetes)
BuildRequires:	python3dist(lockfile)
BuildRequires:	python3dist(lxml)
BuildRequires:	python3dist(markdown)
BuildRequires:	python3dist(markupsafe)
BuildRequires:	python3dist(markupsafe)
BuildRequires:	python3dist(maturin)
BuildRequires:	python3dist(more-itertools)
BuildRequires:	python3dist(msal-extensions)
BuildRequires:	python3dist(msal)
BuildRequires:	python3dist(msgpack)
BuildRequires:	python3dist(msrest)
BuildRequires:	python3dist(msrestazure)
BuildRequires:	python3dist(multidict)
BuildRequires:	python3dist(netaddr)
BuildRequires:	python3dist(oauthlib)
BuildRequires:	python3dist(openshift)
BuildRequires:	python3dist(opentelemetry-api)
BuildRequires:	python3dist(opentelemetry-exporter-otlp-proto-common)
BuildRequires:	python3dist(opentelemetry-exporter-otlp-proto-grpc)
BuildRequires:	python3dist(opentelemetry-exporter-otlp-proto-http)
BuildRequires:	python3dist(opentelemetry-exporter-otlp)
BuildRequires:	python3dist(opentelemetry-instrumentation-logging)
BuildRequires:	python3dist(opentelemetry-instrumentation)
BuildRequires:	python3dist(opentelemetry-proto)
BuildRequires:	python3dist(opentelemetry-sdk)
BuildRequires:	python3dist(opentelemetry-semantic-conventions)
BuildRequires:	python3dist(packaging)
BuildRequires:	python3dist(packaging)
BuildRequires:	python3dist(pbr)
BuildRequires:	python3dist(pexpect)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(pkgconfig)
BuildRequires:	python3dist(portalocker)
BuildRequires:	python3dist(prometheus-client)
BuildRequires:	python3dist(protobuf)
BuildRequires:	python3dist(psutil)
BuildRequires:	python3dist(psycopg)
BuildRequires:	python3dist(ptyprocess)
BuildRequires:	python3dist(pyasn1-modules)
BuildRequires:	python3dist(pyasn1)
BuildRequires:	python3dist(pycparser)
BuildRequires:	python3dist(pydantic-core)
BuildRequires:	python3dist(pydantic)
BuildRequires:	python3dist(pygerduty)
BuildRequires:	python3dist(pygments)
BuildRequires:	python3dist(pyjwt[crypto])
BuildRequires:	python3dist(pyopenssl)
BuildRequires:	python3dist(pyparsing)
BuildRequires:	python3dist(pyrad)
BuildRequires:	python3dist(python-daemon)
BuildRequires:	python3dist(python-dateutil)
BuildRequires:	python3dist(python-dateutil)
BuildRequires:	python3dist(python-dsv-sdk)
BuildRequires:	python3dist(python-jose)
BuildRequires:	python3dist(python-ldap)
BuildRequires:	python3dist(python-string-utils)
BuildRequires:	python3dist(python-tss-sdk)
BuildRequires:	python3dist(python3-openid)
BuildRequires:	python3dist(pytz)
BuildRequires:	python3dist(pytz)
BuildRequires:	python3dist(pyyaml)
BuildRequires:	python3dist(pyyaml)
BuildRequires:	python3dist(pyzstd)
BuildRequires:	python3dist(receptorctl)
BuildRequires:	python3dist(redis)
BuildRequires:	python3dist(referencing)
BuildRequires:	python3dist(requests-oauthlib)
BuildRequires:	python3dist(requests)
BuildRequires:	python3dist(requests)
BuildRequires:	python3dist(rpds-py)
BuildRequires:	python3dist(rsa)
BuildRequires:	python3dist(s3transfer)
BuildRequires:	python3dist(semantic-version)
BuildRequires:	python3dist(service-identity)
BuildRequires:	python3dist(setuptools-rust)
BuildRequires:	python3dist(setuptools-scm[toml])
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(six)
BuildRequires:	python3dist(slack-sdk)
BuildRequires:	python3dist(smmap)
BuildRequires:	python3dist(snowballstemmer)
BuildRequires:	python3dist(social-auth-app-django)
BuildRequires:	python3dist(social-auth-core[openidconnect])
BuildRequires:	python3dist(sphinx-ansible-theme)
BuildRequires:	python3dist(sphinx-rtd-theme)
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3dist(sphinxcontrib-applehelp)
BuildRequires:	python3dist(sphinxcontrib-devhelp)
BuildRequires:	python3dist(sphinxcontrib-htmlhelp)
BuildRequires:	python3dist(sphinxcontrib-jquery)
BuildRequires:	python3dist(sphinxcontrib-jsmath)
BuildRequires:	python3dist(sphinxcontrib-qthelp)
BuildRequires:	python3dist(sphinxcontrib-serializinghtml)
BuildRequires:	python3dist(sqlparse)
BuildRequires:	python3dist(tacacs-plus)
BuildRequires:	python3dist(tempora)
BuildRequires:	python3dist(tomli)
BuildRequires:	python3dist(twilio)
BuildRequires:	python3dist(twisted[tls])
BuildRequires:	python3dist(txaio)
BuildRequires:	python3dist(typing-extensions)
BuildRequires:	python3dist(urllib3)
BuildRequires:	python3dist(urllib3)
BuildRequires:	python3dist(uwsgi)
BuildRequires:	python3dist(uwsgitop)
BuildRequires:	python3dist(websocket-client)
BuildRequires:	python3dist(wheel)
BuildRequires:	python3dist(wrapt)
BuildRequires:	python3dist(xmlsec)
BuildRequires:	python3dist(yarl)
BuildRequires:	python3dist(zipp)
BuildRequires:	python3dist(zope-interface)

%description
AWX provides a web-based user interface, REST API, and task engine built on top of [Ansible](https://github.com/ansible/ansible). It is one of the upstream projects for [Red Hat Ansible Automation Platform](https://www.ansible.com/products/automation-platform).

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?py3_provide:%py3_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
AWX provides a web-based user interface, REST API, and task engine built on top of [Ansible](https://github.com/ansible/ansible). It is one of the upstream projects for [Red Hat Ansible Automation Platform](https://www.ansible.com/products/automation-platform).

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.md
%doc README.md
%{_bindir}/awx_info
%{_bindir}/awx_to_nc
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Thu Sep 19 2024 Nico Kadel-Garcia <nkadel@gmail.com> - 0.1.1-1
- Initial package.
