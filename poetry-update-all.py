import subprocess

from typing import List


def run_subprocess(command: List[str]) -> str:
    return subprocess.run(command, capture_output=True).stdout.decode()


def _get_package_name(command: List[str]) -> List[str]:
    output = run_subprocess(command) 
    return [line.split()[0] for line in output.split("\n") if len(line.split()) > 0]


def get_package_names():
    poetry_show_outdated = ["poetry", "show", "--outdated"]
    all_packages = _get_package_name(poetry_show_outdated)
    no_dev_packages = _get_package_name(poetry_show_outdated + ["--no-dev"])
    dev_packages = list(set(all_packages) - set(no_dev_packages))
    return no_dev_packages, dev_packages


def update_all_packages():
    no_dev_packages, dev_packages = get_package_names()

    for package in no_dev_packages:
        subprocess.run(
                ["poetry", "add", f"{package}@latest"],
        )

    for package in dev_packages:
        subprocess.run(
                ["poetry", "add", "--dev", f"{package}@latest"]
        )


if __name__ == "__main__":
    update_all_packages()
