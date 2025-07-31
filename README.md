# python-check-version
A script to generate and compare version numbers based on templates provided in a JSON configuration file.

Usage:
    python python-check-version.py <version> <config_file>

Arguments:
    version: The version number to compare against (e.g., 3.7.1).
    config_file: Path to the JSON configuration file containing version templates.

Description:
    This script reads a JSON configuration file containing version templates.
    It generates version numbers based on these templates, sorts them, and then
    outputs a list of all generated versions. Additionally, it lists versions that are older than
    the specified version number.

Example:
    python python-check-version.py 3.7.1 myconf.json
