doc:
	sphinx-build -E -b dirhtml docs dist/docs
serve: doc
	open http://127.0.0.1:8099
	cd dist/docs; python -m http.server 8099 --bind 127.0.0.1
clean:
	rm -rf dist
