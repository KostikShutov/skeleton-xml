import os


def listing(directory: str) -> None:
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.py') or filename.endswith('test.xml'):
                filepath: str = os.path.join(root, filename)

                if os.path.isfile(filepath) and filename != os.path.basename(__file__):
                    print(f"# {replace(filepath)}")

                    if os.path.getsize(filepath) > 0:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            print(replace(f.read()))
                    else:
                        print(f"# Empty file")
                        print()

                    print()


def replace(string: str) -> str:
    return (string
            .replace('skeleton-xml', 'config-xml')
            .replace('skeleton_xml', 'config_xml'))


if __name__ == "__main__":
    listing(directory='.')
