import re
import subprocess
from pprint import pprint

def get_git_logs():
    r = subprocess.run(["git", "log", "--name-status", "HEAD~20..HEAD", "--pretty=format:", "."], stdout=subprocess.PIPE, text=True)
    r = [i.split("\t") for i in r.stdout.split("\n") if i != ""]
    r = [i for i in r if i[0] in ("A", "M")]
    r = [i for i in r if (i[1] not in ("README.md", "SUMMARY.md")) and (not i[1].startswith(".")) and i[1].endswith(".md")]

    return r


def remove_duplicate(logs):
    already_changed_files = set()
    clean_logs = list()

    for log in logs:
        if log[1] in already_changed_files:
            continue
        already_changed_files.add(log[1])
        clean_logs.append(log)

    return clean_logs


def get_titles(logs):
    logs_with_names = list()

    for log in logs:
        try:
            with open(log[1], "r") as f:
                titles = [f.readline() for _ in range(10)]
                title = [t.replace("# ", "").replace("\n", "") for t in titles if t.startswith("# ")][0]
                logs_with_names.append([*log, title])
        except FileNotFoundError:
            pass

    return logs_with_names[:20]


def generate_readme(logs):
    content = ""

    for log in logs:
        # annotation = "- *New File*" if log[0] == "A" else ""
        file_path = log[1]
        title = log[2]

        content += f"* [**{title}** - {file_path}]({file_path})\n"

    with open("README.md.template", "r") as template:
        template = ''.join(template.readlines())
        filled_readme = re.sub(r"{{CHANGES}}", content, template)

    return filled_readme


def write_readme(readme):
    with open("README.md", "w") as f:
        f.writelines(readme)


if __name__ == "__main__":
    v = get_git_logs()
    v = remove_duplicate(v)
    v = get_titles(v)
    v = generate_readme(v)
    write_readme(v)
