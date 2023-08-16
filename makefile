PORT ?= 8099

# documentation ################################################################

.PHONY: doc serve
doc:
	sphinx-build -E -b dirhtml docs dist/docs
serve: doc
	@cd dist/docs && \
	( python -m http.server $(PORT) --bind 127.0.0.1 & ) && \
	open http://127.0.0.1:$(PORT) && \
	wait

################################################################################

.PHONY: clean
clean:
	rm -rf dist
