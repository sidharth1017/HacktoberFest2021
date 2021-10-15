import os

def detectVirus(filename):
    with open(filename, "r") as f:
        lines = f.read()

    if "virus" in lines.lower():
        return True

    else:
        return False

if __name__ == '__main__':

    contents_list = os.listdir()
    count = 0

    for content in contents_list:
        if content.endswith("txt"):
            print(f"Detecting Virus In {content}")

            flag = detectVirus(content)

            if flag:
                print(f"Virus Found in {content}")
                count += 1

            else:
                print(f"Virus Not Found in {content}")

    print(f"\n{count} Files Have Virus Hidden in Them")
