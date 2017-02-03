PLATFORM = $(shell uname)
TRAVIS_REPO_SLUG = gutomaia/gutomaia.github.com
GH_TOKEN ?= secret

BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/site/output
GITHUB_PAGES_BRANCH=master

PYTHON_MODULES=site

OK=\033[32m[OK]\033[39m
FAIL=\033[31m[FAIL]\033[39m
CHECK=@if [ $$? -eq 0 ]; then echo "${OK}"; else echo "${FAIL}" ; fi

WGET = wget -q

default: python.mk
	@$(MAKE) -C . build

ifeq "true" "${shell test -f python.mk && echo true}"
include python.mk
endif

python.mk:
	@${WGET} https://raw.githubusercontent.com/gutomaia/makery/master/python.mk && \
		touch $@

clean: python_clean

purge: python_purge
	@rm python.mk
	@rm -rf .tox
	@git submodule deinit -f Flex

Flex/templates/index.html:
	git submodule init
	git submodule update --remote

.checkpoint/flex_branch: Flex/templates/index.html
	cd Flex && git checkout v2.1.0 && touch ../$@

html: .checkpoint/flex_branch
	${VIRTUALENV} $(MAKE) -C site html

build: python_build ${REQUIREMENTS} html

serve: build
	${VIRTUALENV} $(MAKE) -C site serve

publish: .checkpoint/flex_branch
	${VIRTUALENV} $(MAKE) -C site publish

github: publish
	${VIRTUALENV} ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	@git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git master > /dev/null
