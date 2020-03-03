#
# Makefile - build wrapper for awx
#
#	git clone RHEL 6 SRPM building tools from
#	https://github.com/nkadel/[package] into designated
#	AWXPKGS below
#
#	Set up local

#REPOBASE=http://localhost
REPOBASE=file://$(PWD)

# Dependency metapackage
#EPELPKGS+=PyYAML-srpm

EPELPKGS+=Cython-srpm
EPELPKGS+=meson-srpm
EPELPKGS+=http-parser-srpm

# RHEL name funkiness for python-pythlakes
EPELPKGS+=pyflakes-srpm

EPELPKGS+=python2-lockfile-srpm
EPELPKGS+=python2-sphinx-srpm

# python3 only update modules for version sensitive python-six
EPELPKGS+=python3-six-srpm

EPELPKGS+=python-adal-srpm
EPELPKGS+=python-async-generator-srpm
EPELPKGS+=python-attrs-srpm
EPELPKGS+=python-azure-common-srpm
EPELPKGS+=python-azure-core-srpm
EPELPKGS+=python-azure-keyvault-keys-srpm
EPELPKGS+=python-azure-keyvault-secrets-srpm
EPELPKGS+=python-azure-keyvault-srpm
EPELPKGS+=python-azure-nspkg-srpm
EPELPKGS+=python-billiard-srpm
EPELPKGS+=python-build-srpm
EPELPKGS+=python-celery-srpm
EPELPKGS+=python-channels-srpm
EPELPKGS+=python-coverage-srpm
EPELPKGS+=python-daphne-srpm
EPELPKGS+=python-django-auth-ldap-srpm
EPELPKGS+=python-django-cors-headers-srpm
EPELPKGS+=python-django-crum-srpm
EPELPKGS+=python-django-extensions-srpm
EPELPKGS+=python-django-solo-srpm
EPELPKGS+=python-entrypoints-srpm
EPELPKGS+=python-extras-srpm
EPELPKGS+=python-func_timeout-srpm
EPELPKGS+=python-gitdb-srpm
EPELPKGS+=python-idna-ssl-srpm
EPELPKGS+=python-inflect-srpm
EPELPKGS+=python-irc-srpm
EPELPKGS+=python-isodate-srpm
EPELPKGS+=python-jaraco-packaging-srpm
EPELPKGS+=python-kombu-srpm
EPELPKGS+=python-lockfile-srpm
EPELPKGS+=python-memcached-srpm
EPELPKGS+=python-more-itertools-srpm
EPELPKGS+=python-pluggy-srpm
EPELPKGS+=python-ptyprocess-srpm
EPELPKGS+=python-py-srpm
EPELPKGS+=python-pyasn1-srpm
EPELPKGS+=python-pycares-srpm
EPELPKGS+=python-pyjwt-srpm
EPELPKGS+=python-pytest-aiohttp-srpm
EPELPKGS+=python-pytest-param-srpm
EPELPKGS+=python-python-mimeparse-srpm
EPELPKGS+=python-selenium-srpm
EPELPKGS+=python-setuptools_scm-srpm
EPELPKGS+=python-smmap-srpm
EPELPKGS+=python-typing-extensions-srpm
EPELPKGS+=python-unittest2-srpm
EPELPKGS+=python-vine-srpm
EPELPKGS+=python-websocket_client-srpm
EPELPKGS+=python-zope-interface-srpm

# Depends on pycares
AWXPKGS+=python-aiodns-srpm

# Depends on pytest
AWXPKGS+=python-sqlparse-srpm

# Depends on http-parser and Cython
AWXPKGS+=python-aiohttp-srpm

# Depends on ptyprocess and pluggy
AWXPKGS+=python-pexpect-srpm

# Depndes on unittest2
AWXPKGS+=python-case-srpm

# Depnds on isodate
AWXPKGS+=python-rdflib-srpm

# Depends on pyjwt
AWXPKGS+=python-twilio-srpm

# Depends on memcached
AWXPKGS+=python-django-srpm

# python3 only update for pytest modules of misnmed source package
# Depends on more-itertools and pluggy and py
AWXPKGS+=pytest-srpm

# Depends on pytest and more-itertools
AWXPKGS+=python-multidict-srpm

# Depends on pytest and Cython and multidict and more-itertools
AWXPKGS+=python-yarl-srpm

# Depends on pytest and entrypoints
AWXPKGS+=python-flake8-srpm
AWXPKGS+=python-pytest-flake8-srpm

# Depends on flake8 and pytest-flake8
AWXPKGS+=python-tempora-srpm

# Depends on aio-http and pyttest-aiohttp
AWXPKGS+=python-async-timeout-srpm

# Depends on jaraco-packaging and setuptools_scm
AWXPKGS+=python-jaraco-itertools-srpm

# Depends on jaraco-packaging and setuptools_scm and jaraco-itertools and toml
AWXPKGS+=python-zipp-srpm

# Depends on zipp
AWXPKGS+=python-importlib_metadata-srpm

# Depends on pytest and pytest-flake8 and setuptools_scm and more-itertools
AWXPKGS+=python-jaraco-classes-srpm

# Depends on jaraco-packaging and jaraco-classes and pytest-flske8
AWXPKGS+=python-jaraco-functools-srpm

AWXPKGS+=python-testtools-srpm
AWXPKGS+=python-fixtures-srpm
AWXPKGS+=python-testscenario-srpm
AWXPKGS+=python-daemon-srpm

# Depends on django-extensions and coverage and flake8
AWXPKGS+=python-django-formtools-srpm

# Depends on coverage and async-generator and hypothesis
AWXPKGS+=python-pytest-asyncio-srpm

# Depends on pytest and and pytest-asyncio and async-timeout
AWXPKGS+=python-asgiref-srpm

# Depends on django and django-formtools
AWXPKGS+=python-django-jsonfield-srpm

AWXPKGS+=python-service-identity-srpm

# Depends on pytest and service-identity
AWXPKGS+=python-ansible-runner-srpm

# Depends on pytest
AWXPKGS+=python-trustme-srpm

# Depends on attrs and pytest and pytest-asyncio and more-itertools and 
AWXPKGS+=python-outcome-srpm

# Depends on trustme and outcome
AWXPKGS+=python-trio-srpm

# Depends on trio and pytest
AWXPKGS+=python-msrest-srpm

AWXPKGS+=ansible-awx-srpm

REPOS+=awxrepo/el/7
REPOS+=awxrepo/el/8
#REPOS+=awxrepo/fedora/31

REPODIRS := $(patsubst %,%/x86_64/repodata,$(REPOS)) $(patsubst %,%/SRPMS/repodata,$(REPOS))

CFGS+=awxrepo-7-x86_64.cfg
CFGS+=awxrepo-8-x86_64.cfg
#CFGS+=awxrepo-f31-x86_64.cfg

# Link from /etc/mock
MOCKCFGS+=epel-7-x86_64.cfg
MOCKCFGS+=epel-8-x86_64.cfg
#MOCKCFGS+=fedora-31-x86_64.cfg

install:: $(CFGS)
install:: $(MOCKCFGS)
install:: $(REPODIRS)
install:: $(EPELPKGS)
install:: $(AWXPKGS)

.PHONY: all
all:: install

.PHONY: install clean getsrc build
install clean getsrc build::
	@for name in $(EPELPKGS) $(AWXPKGS); do \
	     (cd $$name && $(MAKE) $(MFLAGS) $@); \
	done

# Actually build in directories
.PHONY: $(EPELPKGS) $(AWXPKGS)
$(EPELPKGS) $(AWXPKGS)::
	(cd $@ && $(MAKE) $(MLAGS) install)

repos: $(REPOS) $(REPODIRS)
$(REPOS):
	install -d -m 755 $@

.PHONY: $(REPODIRS)
$(REPODIRS): $(REPOS)
	@install -d -m 755 `dirname $@`
	/usr/bin/createrepo -q `dirname $@`


epelpkgs: epel
.PHONY: epel
epel:: $(EPELPKGS)

# awx pkgs depend on epelpkgs
awxpkgs: awx
.PHONY: awx
#awx:: epel %(AWXPKGS)
awx: $(AWXPKGS)

.PHONY: cfg
cfg:: cfgs

.PHONY: cfgs
cfgs: $(CFGS) $(MOCKCFGS)

awxrepo-7-x86_64.cfg: /etc/mock/epel-7-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/epel-7-x86_64/awxrepo-7-x86_64/g' $@
	@echo >> $@
	@echo "Disabling 'best=' for $@"
	@sed -i '/^best=/d' $@
	@echo "best=0" >> $@
	@echo "config_opts['yum.conf'] += \"\"\"" >> $@
	@echo '[awxrepo]' >> $@
	@echo 'name=awxrepo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/awxrepo/el/7/x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=0' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@

awxrepo-8-x86_64.cfg: /etc/mock/epel-8-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/epel-8-x86_64/awxrepo-8-x86_64/g' $@
	@echo >> $@
	@echo "Disabling 'best=' for $@"
	@sed -i '/^best=/d' $@
	@echo "best=0" >> $@
	@echo "config_opts['yum.conf'] += \"\"\"" >> $@
	@echo '[awxrepo]' >> $@
	@echo 'name=awxrepo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/awxrepo/el/8/x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=0' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@

#awxrepo-f31-x86_64.cfg: /etc/mock/fedora-31-x86_64.cfg
#	@echo Generating $@ from $?
#	@cat $? > $@
#	@sed -i 's/fedora-31-x86_64/awxrepo-f31-x86_64/g' $@
#	@echo >> $@
#	@echo "Disabling 'best=' for $@"
#	@sed -i '/^best=/d' $@
#	@echo "best=0" >> $@
#	@echo "config_opts['yum.conf'] += \"\"\"" >> $@
#	@echo '[awxrepo]' >> $@
#	@echo 'name=awxrepo' >> $@
#	@echo 'enabled=1' >> $@
#	@echo 'baseurl=$(REPOBASE)/awxrepo/fedora/31/x86_64/' >> $@
#	@echo 'failovermethod=priority' >> $@
#	@echo 'skip_if_unavailable=False' >> $@
#	@echo 'metadata_expire=0' >> $@
#	@echo 'gpgcheck=0' >> $@
#	@echo '#cost=2000' >> $@
#	@echo '"""' >> $@

$(MOCKCFGS)::
	ln -sf /etc/mock/$@ $@

repo: awxrepo.repo
awxrepo.repo:: Makefile awxrepo.repo.in
	@if [ -s /etc/fedora-release ]; then \
		cat $@.in | \
			sed "s|@REPOBASEDIR@/|$(PWD)/|g" | \
			sed "s|/@RELEASEDIR@/|/fedora/|g" > $@; \
	elif [ -s /etc/redhat-release ]; then \
		cat $@.in | \
			sed "s|@REPOBASEDIR@/|$(PWD)/|g" | \
			sed "s|/@RELEASEDIR@/|/el/|g" > $@; \
	else \
		echo Error: unknown release, check /etc/*-release; \
		exit 1; \
	fi

awxrepo.repo::
	@cmp -s $@ /etc/yum.repos.d/$@ || \
	    diff -u $@ /etc/yum.repos.d/$@

clean::
	find . -name \*~ -exec rm -f {} \;
	rm -f *.cfg
	rm -f *.out
	@for name in $(EPELPKGS) $(AWXPKGS); do \
	    $(MAKE) -C $$name $@; \
	done

distclean: clean
	rm -rf awxrepo
	@for name in $(EPELPKGS) $(AWXPKGS); do \
	    $(MAKE) -C $$name $@; \
	done

maintainer-clean: distclean
	git clean -x -d -f .
	@for name in $(EPELPKGS) $(AWXPKGS); do \
	    $(MAKE) -C $$name $@; \
	done
