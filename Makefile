pass:
	true

setup:
	pip install -r site/build-requirements.txt

CHECK_UNCOMMITTED = --check_uncommitted
OUT_HTML = index.html

build:
	python site/build.py \
		--in_md README.md \
		--html_template site/templates/index.html \
		--images_dir site/img/ \
		--out_html $(OUT_HTML) $(CHECK_UNCOMMITTED)

lint: OUT_HTML=/tmp/index.html
lint: CHECK_UNCOMMITTED=
lint: build
	diff -q /tmp/index.html index.html


.PHONY: \
	setup \
	build \
	lint
