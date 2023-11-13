SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = dist/docs

# for bump2version, valid options are: major, minor, patch
PART ?= patch

PORT ?= 8099
DOC_DEP = $(shell find docs -type f \( -name '*.md' -o -name '*.rst' \)) $(shell find src -type f -name '*.py')

# documentation ################################################################

.PHONY: all doc epub
all: doc epub pdf man html
doc: dist/docs/.sentinel
epub: dist/docs/SOUKDataCentre.epub
pdf: dist/docs/latex/soukdatacentre.pdf
man: dist/docs/soukdatacentre.1
html: dist/docs/index.html

dist/docs/.sentinel: $(DOC_DEP)
	@$(SPHINXBUILD) -b dirhtml "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	touch $@
dist/docs/SOUKDataCentre.epub: $(DOC_DEP)
	@$(SPHINXBUILD) -b epub "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
dist/docs/latex/soukdatacentre.pdf: $(DOC_DEP)
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
dist/docs/soukdatacentre.1: $(DOC_DEP)
	@$(SPHINXBUILD) -b man "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
dist/docs/index.html: $(DOC_DEP)
	@$(SPHINXBUILD) -b singlehtml "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

.PHONY: serve
serve: doc
	sphinx-autobuild \
		-b dirhtml $(SPHINXOPTS) \
		--port $(PORT) \
		--open-browser \
		--delay 0 \
		"$(SOURCEDIR)" "$(BUILDDIR)"

# releasing ####################################################################

.PHONY: bump opt
bump:
	bump2version $(PART)
	git push --follow-tags

# to be run on vm77 for sharing to other users
opt:
	cp -f bin/xrootdfs.sh /opt/simonsobservatory

################################################################################

.PHONY: clean
clean:
	rm -rf dist

print-%:
	$(info $* = $($*))
