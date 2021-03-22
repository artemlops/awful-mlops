import sys
import markdown
import argparse
from pathlib import Path
from jinja2 import Template
from subprocess import run
from shlex import split

def get_parser():
    p = argparse.ArgumentParser()
    p.add_argument("--in_md", type=Path, required=True)
    p.add_argument("--html_template", type=Path, required=True)
    p.add_argument("--images_dir", type=Path, default=Path("./img"))
    p.add_argument("--out_html", type=Path, required=True)
    p.add_argument("--check_uncommitted", action="store_true")
    return p
    

if __name__ == "__main__":
    args = get_parser().parse_args()
    in_md = args.in_md
    html_template = args.html_template
    images_dir = args.images_dir
    out_html = args.out_html
    check_uncommitted = args.check_uncommitted

    assert in_md.is_file(), in_md
    assert html_template.is_file(), html_template
    assert images_dir.is_dir, images_dir
    if check_uncommitted:
        print(f"Checking that output html file has no uncommitted changes")
        for cached in ["--cached", ""]:
            run(split(f"git diff {cached} --exit-code --name-only -- {out_html}"), check=True)

    template = Template(html_template.read_text())

    inner_html = markdown.markdown(in_md.read_text())
    result_html = template.render(content=inner_html, images_dir=images_dir)
    out_html.write_text(result_html)
    print(f"[+] Success: {in_md} + {html_template} -> {out_html}")
