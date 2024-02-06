"""
 # @ Author: Adam Zhang
 # @ Create Time: 2024-02-05 16:41:35
 # @ Modified by: Adam Zhang
 # @ Modified time: 2024-02-05 16:41:39
 # @ Description: to generate the navigation bar automatically
 like 
 
nav:
  - Home: 
    - index.md
  - Leetcode:
      - leetcode/index.md
      - 1 two sum: leetcode/1-two-sum/index.md
      - 2 add two numbers: leetcode/2-add-two-numbers/index.md
"""

import os


def main(basedir, output):
    # get all directories in leetcode folder
    directories = []
    for entry in os.listdir(basedir):
        entry_path = os.path.join(basedir, entry)
        if os.path.isdir(entry_path):
            directories.append(entry)
    # sort them by number
    directories.sort(key=lambda x: int(x.split("-")[0]))

    # populate the res
    items = []
    prefix = "- "
    for directory in directories:
        entry = directory.replace("-", " ")
        temp = prefix + entry + ": leetcode/" + directory + "/index.md"
        items.append(temp)

    with open(output, "w") as f:
        for item in items:
            f.write(item + "\n")


if __name__ == "__main__":
    main(
        basedir="/Users/adamzhang/Documents/personal/Leetcode/leetcode_with_adam/docs/leetcode",
        output="/Users/adamzhang/Documents/personal/Leetcode/src/autogen_nav.yml",
    )
