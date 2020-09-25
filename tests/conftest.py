import subprocess

import pytest


@pytest.fixture
def script(tmpdir):
    class Script:
        path = None

        def set_content(self, content):
            self.path.write(content)

        def run(self):
            args = [
                "python3",
                "bin/markdown-to-confluence.py",
                "--confluence-url",
                "https://confluence.example.com",
                "--confluence-space",
                "SOME_SPACE",
                "--root",
                tmpdir,
                "--path",
                ".",
                "--dry-run",
            ]

            with subprocess.Popen(args, stderr=subprocess.PIPE) as p:
                out = p.stderr.read().decode()
                print(out)
                return out

    script = Script()
    script.path = tmpdir / "test.md"
    return script
