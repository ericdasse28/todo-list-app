"""Entrypoint script to run the app from the package using the
python -m edtodo command"""

from edtodo import __app_name__, cli


def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
