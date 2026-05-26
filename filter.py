# filter.py

def rule_based_filter(files: list):

    ignored_folders = [
        "node_modules/",
        "dist/",
        ".git/",
        "__pycache__/",
        "build/"
    ]

    ignored_extensions = [
        ".log",
        ".lock",
        ".env",
        ".DS_Store"
    ]

    ignored = []
    remaining = []

    for file in files:

        skip = False

        for folder in ignored_folders:

            if file.startswith(folder):
                ignored.append(file)
                skip = True
                break

        if skip:
            continue

        for ext in ignored_extensions:

            if file.endswith(ext):
                ignored.append(file)
                skip = True
                break

        if not skip:
            remaining.append(file)

    return ignored, remaining