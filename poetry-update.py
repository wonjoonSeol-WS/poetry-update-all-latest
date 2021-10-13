import subprocess


def get_outdated_packages() -> str:
    output = subprocess.run(
        ["poetry", "show", "--outdated"],
        capture_output=True
    ).stdout.decode()

    return [line.split()[0] for line in output.split("\n") if len(line.split()) > 0]


def update_all_packages():
    packages = get_outdated_packages()
    for package in packages:
        subprocess.run(
            ["poetry", "add", f"{package}@latest"],
        )


if __name__ == "__main__":
    update_all_packages()
