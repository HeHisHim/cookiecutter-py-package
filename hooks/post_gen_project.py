import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def organize_files(package_dir):
    os.system(f"mv -f {package_dir}/* ../")
    os.system(f"mv -f {package_dir}/.[^.]* ../")
    os.system(f"rm -rf {package_dir}/")


if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    organize_files(package_dir="{{cookiecutter.project_slug}}")
