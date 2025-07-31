import json
import sys


def generate_versions(template):
    parts = template.split('.')
    versions = []
    for i in range(2):  # Генерируем две версии для каждого ключа
        version_parts = []
        for part in parts:
            if part == '*':
                version_parts.append(str(i))
            else:
                version_parts.append(part)
        versions.append('.'.join(version_parts))
    return versions


def read_config_file(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config


def main():
    if len(sys.argv) != 3:
        print("Usage: python task3.py <version> <config_file>")
        sys.exit(1)

    version = sys.argv[1]
    config_file = sys.argv[2]

    config = read_config_file(config_file)
    all_versions = []

    for template in config.values():
        all_versions.extend(generate_versions(template))

    sorted_versions = sorted(
        all_versions, key=lambda x: list(map(int, x.split('.'))))

    print("All generated versions:")
    for v in sorted_versions:
        print(v)

    print("\nVersions older than", version)
    for v in sorted_versions:
        if list(map(int, v.split('.'))) < list(map(int, version.split('.'))):
            print(v)


if __name__ == "__main__":
    main()
