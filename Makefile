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

# RHEL name funkiness for python-pythlakes
EPELPKGS+=pyflakes-srpm

EPELPKGS+=python2-lockfile-srpm
EPELPKGS+=python2-sphinx-srpm

# python3 only update modules for version sensitive python-six
EPELPKGS+=python3-six-srpm

EPELPKGS+=python-adal-srpm
EPELPKGS+=python-azure-common-srpm
EPELPKGS+=python-azure-keyvault-keys-srpm
EPELPKGS+=python-azure-keyvault-srpm
EPELPKGS+=python-azure-nspkg-srpm
EPELPKGS+=python-build-srpm
EPELPKGS+=python-celery-srpm
EPELPKGS+=python-coverage-srpm
EPELPKGS+=python-django-auth-ldap-srpm
EPELPKGS+=python-django-cors-headers-srpm
EPELPKGS+=python-django-crum-srpm
EPELPKGS+=python-django-extensions-srpm
EPELPKGS+=python-entrypoints-srpm
EPELPKGS+=python-extras-srpm
EPELPKGS+=python-gitdb-srpm
EPELPKGS+=python-gitdb2-srpm
EPELPKGS+=python-inflect-srpm
EPELPKGS+=python-irc-srpm
EPELPKGS+=python-jaraco-packaging-srpm
EPELPKGS+=python-kombu-srpm
EPELPKGS+=python-lockfile-srpm
EPELPKGS+=python-more-itertools-srpm
EPELPKGS+=python-py-srpm
EPELPKGS+=python-pyjwt-srpm
EPELPKGS+=python-python-mimeparse-srpm
EPELPKGS+=python-setuptools_scm-srpm
EPELPKGS+=python-vine-srpm

AWXPKGS+=python-amqp-srpm

# Depends on pyjwt
AWXPKGS+=python-twilio-srpm

# python3 only update for pytest modules of misnmed source package
# Depends on more-itertools and pluggy and py
AWXPKGS+=pytest-srpm

# Depends on pytest and entrypoints
AWXPKGS+=python-flake8-srpm
AWXPKGS+=python-pytest-flake8-srpm

# Depends on jaraco-packaging and setuptools_scm
AWXPKGS+=python-jaraco-itertools-srpm

# Depends on jaraco-packaging and setuptools_scm and jaraco-itertools and toml
AWXPKGS+=python-zipp-srpm

# Depends on zipp
AWXPKGS+=python-importlib_metadata-srpm

# Depends on jaraco-packaging and jaraco-classes and pytest-flske8
AWXPKGS+=python-jaraco-functools-srpm

AWXPKGS+=python-django-coverage-srpm

AWXPKGS+=python-testtools-srpm
AWXPKGS+=python-fixtures-srpm
AWXPKGS+=python-testscenario-srpm
AWXPKGS+=python-daemon-srpm
# Depends on django-extensions and django-coverage
AWXPKGS+=python-django-formtools-srpm

AWXPKGS+=python-ansible-runner-srpm

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


.PHONY: epel epelpkgs
epel epelpkgs:: $(EPELPKGS)

# awx pkgs depend on epelpkgs
.PHONY: awx awxpkgs
awx awxpkgs:: $(EPELPKGS) $(AWXPKGS)

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
