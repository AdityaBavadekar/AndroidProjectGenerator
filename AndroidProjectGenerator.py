import os
from datetime import date

PROJECTS_DIR = "C:\\Users\\Administrator\\AndroidStudioProjectsStub\\"
author_name = "Author"
application_name = "Application"
package_name = "com.example.application"
build_src = False
WORKING_DIR = PROJECTS_DIR + application_name.strip() + "\\"
BUILD_SRC_JAVA_DIR = "buildSrc\\src\\main\\java"
FILE_BUILD_GRADLE_KTS = "build.gradle.kts"
FILE_VERSIONS = "Versions.kt"
FILE_DEPENDENCIES = "Dependencies.kt"
FILE_LIBS = "Libs.kt"
FILE_MAIN_ACTIVITY = "MainActivity.kt"
FILE_BUILD_GRADLE = "build.gradle"
FILE_SETTINGS_GRADLE = "settings.gradle"
FILE_LOCAL_PROPERTIES = "local.properties"
FILE_GRADLE_PROPERTIES = "gradle.properties"
FILE_GRADLE_WRAPPER_PROPERTIES = "gradle-wrapper.properties"
FILE_GRADLE_WRAPPER_JAR = "gradle-wrapper.jar"
FILE_GRADLE_SETTINGS = "settings.gradle"
FILE_README = "README.md"
FILE_LICENSE = "LICENSE.md"
FILE_ANDROID_MANIFEST = "AndroidManifest.xml"
FILE_PROGAURD = "proguard-rules.pro"
FILE_GIT_IGNORE = ".gitignore"


def create_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        pass
    return


def create_dirs(path):
    try:
        os.makedirs(path)
    except OSError:
        pass
    return


def create_file(path):
    open(path, "w+").close()
    return


def get_file(path, mode="a"):
    return open(path, mode)


def read_file(path):
    return open(path, "r")


def copy_file(path1, path2):
    file = read_file(path1)
    text = file.readlines()
    file.close()
    with get_file(path2) as f:
        for line in text:
            f.write(line)
    return


def write_lines_to(lines, path):
    with get_file(path) as f:
        for line in lines:
            f.write(line)
    return


def create_build_src_dirs():
    dir_build_src = WORKING_DIR + "buildSrc" + "\\"
    dir_build_src_source = WORKING_DIR + BUILD_SRC_JAVA_DIR+"\\"

    create_dirs(dir_build_src)
    create_dirs(dir_build_src_source)
    create_file(dir_build_src + FILE_BUILD_GRADLE_KTS)
    create_file(dir_build_src_source + FILE_LIBS)
    create_file(dir_build_src_source + FILE_DEPENDENCIES)
    create_file(dir_build_src_source + FILE_VERSIONS)
    return


def create_project_dirs():
    app_dir = WORKING_DIR + "app\\"
    wrapper_dir = WORKING_DIR + "gradle\\wrapper\\"
    main_src_dir = WORKING_DIR + "app\\src\\main"
    main_java_src_dir = main_src_dir + "\\java"
    for p in package_name.split("."):
        main_java_src_dir += "\\" + p

    create_dirs(wrapper_dir)
    create_dirs(main_java_src_dir)
    create_dirs(main_java_src_dir + "\\ui\\")
    create_dirs(main_java_src_dir + "\\utils\\")
    create_dirs(main_java_src_dir + "\\models\\")
    create_dirs(main_java_src_dir)
    create_dirs(main_src_dir + "\\res\\layout\\")
    create_dirs(main_src_dir + "\\res\\values\\")

    create_file(WORKING_DIR + FILE_GRADLE_PROPERTIES)
    create_file(WORKING_DIR + FILE_BUILD_GRADLE)
    create_file(WORKING_DIR + FILE_GIT_IGNORE)
    create_file(WORKING_DIR + FILE_GRADLE_SETTINGS)
    create_file(WORKING_DIR + FILE_README)
    create_file(WORKING_DIR + FILE_LICENSE)
    create_file(WORKING_DIR + FILE_LOCAL_PROPERTIES)

    create_file(app_dir + FILE_BUILD_GRADLE)
    create_file(app_dir + FILE_PROGAURD)
    create_file(app_dir + FILE_GIT_IGNORE)

    create_file(main_src_dir + "\\" + FILE_ANDROID_MANIFEST)
    create_file(main_src_dir + "\\res\\layout\\activity_main.xml")
    create_file(main_src_dir + "\\res\\values\\strings.xml")
    create_file(main_src_dir + "\\res\\values\\themes.xml")

    create_file(main_java_src_dir + "\\" + FILE_MAIN_ACTIVITY)
    return


def get_file_formatted_text(path):
    text = ""
    lines = []
    with read_file(path) as f:
        lines = f.readlines()
    for line in lines:
        line = line.replace("%APPLICATION_NAME_SPACE%", application_name.strip(), -1)
        line = line.replace("%APPLICATION_NAME_DASHED%", application_name.strip().replace(" ", "-"), -1)
        line = line.replace("%APPLICATION_NAME%", application_name.strip().replace(" ", ""), -1)
        line = line.replace("%PACKAGE_NAME%", package_name, -1)
        line = line.replace("%AUTHOR%", author_name, -1)
        line = line.replace("%YEAR%", str(date.today().year), -1)
        text += line
    return text


def write_to_files():
    # README.md [START]
    license = []
    with read_file("AndroidProjectGenerator/LICENSE_SAMPLE.txt") as f:
        license = f.readlines()
    license[1] = license[1].replace("%YEAR%", str(date.today().year)).replace("%AUTHOR%", author_name)
    license_text = ""
    for line in license:
        license_text += line
    with get_file(WORKING_DIR + FILE_README) as f:
        text = f"# {application_name}\n" \
               f"\n" \
               f"## Author\n" \
               f"- {author_name}\n" \
               f"\n" \
               f"## License\n" \
               f"```\n" + license_text + "\n```\n"
        f.write(text)
        print("Wrote README.md.")
    # README.md [END]

    # LICENSE.md [START]
    copy_file("AndroidProjectGenerator/LICENSE.txt", WORKING_DIR + FILE_LICENSE)
    print("Wrote LICENSE.md")
    # LICENSE.md [END]

    # gradlew [START]
    copy_file("AndroidProjectGenerator/gradlew", WORKING_DIR + "gradlew")
    print("Wrote gradlew")
    # gradlew [END]

    # gradlew.bat [START]
    copy_file("AndroidProjectGenerator/gradlew.bat", WORKING_DIR + "gradlew.bat")
    print("Wrote gradlew.bat")
    # gradlew.bat [END]

    # local.properties [START]
    copy_file("AndroidProjectGenerator/local.properties", WORKING_DIR + FILE_LOCAL_PROPERTIES)
    print("Wrote local.properties")
    # local.properties [END]

    # .gitignore [START]
    copy_file("AndroidProjectGenerator/template_gitignore.txt", WORKING_DIR + FILE_GIT_IGNORE)
    copy_file("AndroidProjectGenerator/template_gitignore.txt", WORKING_DIR + "app\\" + FILE_GIT_IGNORE)
    print("Wrote .gitignore")
    # .gitignore [END]

    # build.gradle [START]
    write_lines_to(get_file_formatted_text("AndroidProjectGenerator/settings_gradle.txt"),
                   WORKING_DIR + FILE_SETTINGS_GRADLE)
    print("Wrote settings.gradle")

    write_lines_to(get_file_formatted_text("AndroidProjectGenerator/gradle_properties.txt"),
                   WORKING_DIR + FILE_GRADLE_PROPERTIES)
    print("Wrote gradle.properties")

    bytes = get_file("AndroidProjectGenerator/gradle-wrapper.jar", "rb").read()
    with open(WORKING_DIR + "gradle\\wrapper\\" + FILE_GRADLE_WRAPPER_JAR, "ab") as f:
        f.write(bytes)

    print("Wrote gradle-wrapper.jar")
    write_lines_to(get_file_formatted_text("AndroidProjectGenerator/gradle-wrapper.properties"),
                   WORKING_DIR + "gradle\\wrapper\\" + FILE_GRADLE_WRAPPER_PROPERTIES)
    print("Wrote gradle-wrapper.properties")

    write_lines_to(get_file_formatted_text("AndroidProjectGenerator/root_build_gradle.txt"),
                   WORKING_DIR + FILE_BUILD_GRADLE)
    print("Wrote build.gradle")
    write_lines_to(get_file_formatted_text("AndroidProjectGenerator/app_build_gradle.txt"),
                   WORKING_DIR + "app\\" + FILE_BUILD_GRADLE)
    print("Wrote app level build.gradle")
    # build.gradle [END]

    # Versions.kt , Dependencies.kt, Libs.kt
    write_lines_to(get_file_formatted_text("AndroidProjectGenerator/buil_gradle_kts.txt"),
                   WORKING_DIR + "buildSrc\\" + FILE_BUILD_GRADLE_KTS)
    write_lines_to(get_file_formatted_text("AndroidProjectGenerator/versions_kt.txt"),
                   WORKING_DIR + BUILD_SRC_JAVA_DIR + "\\Versions.kt")
    write_lines_to(get_file_formatted_text("AndroidProjectGenerator/libs_kt.txt"),
                   WORKING_DIR + BUILD_SRC_JAVA_DIR + "\\Libs.kt")
    write_lines_to(get_file_formatted_text("AndroidProjectGenerator/dependencies_kt.txt"),
                   WORKING_DIR + BUILD_SRC_JAVA_DIR + "\\Dependencies.kt")

    main_src_dir = WORKING_DIR + "app\\src\\main\\"
    main_java_src_dir = main_src_dir + "java"
    for p in package_name.split("."):
        main_java_src_dir += "\\" + p

    # MainActivity.kt [START]
    write_lines_to(get_file_formatted_text("AndroidProjectGenerator/MainActivity.kt"),
                   main_java_src_dir + "\\" + FILE_MAIN_ACTIVITY)
    print("Wrote MainActivity.kt")
    # MainActivity.kt [END]

    # activity_main.xml [START]
    copy_file("AndroidProjectGenerator/activity_main_xml.txt", main_src_dir + "res\\layout\\activity_main.xml")
    print("Wrote activity_main.xml")
    text = get_file_formatted_text("AndroidProjectGenerator/android_manifest_xml.txt")
    with get_file(main_src_dir + FILE_ANDROID_MANIFEST) as f:
        f.write(text)
        print("Wrote AndroidManifest.xml")
    # activity_main.xml [END]

    # string.xml [START]
    text = get_file_formatted_text("AndroidProjectGenerator/strings.txt")
    with get_file(main_src_dir + "res\\values\\strings.xml") as f:
        f.write(text)
        print("Wrote strings.xml")
    # string.xml [END]

    # themes.xml [START]
    lines = []
    with read_file("AndroidProjectGenerator/themes_xml.txt") as f:
        lines = f.readlines()
    text = ""
    for line in lines:
        if line.__contains__("%APPLICATION_NAME%"):
            line = line.replace("%APPLICATION_NAME%", application_name.strip())
        text += line
    with get_file(main_src_dir + "\\res\\values\\themes.xml") as f:
        f.write(text)
        print("Wrote themes.xml")
    # themes.xml [END]


if __name__ == "__main__":
    create_dir(PROJECTS_DIR)
    author_name = input("Enter your name (For license): ")
    application_name = input("Enter application name : ")
    # Setup Variables
    WORKING_DIR = PROJECTS_DIR + application_name.strip().replace(" ", "-") + "\\"
    try:
        os.mkdir(WORKING_DIR)
    except OSError:
        print("~~~~~")
        print(WORKING_DIR)
        print("Directory with same name already exists.")
        overwrite = input("Do you want to overwrite ? (Y/N) : ")
        if overwrite == "N":
            exit(0)
        print("~~~~~")
        pass
    print()
    package_name = input("Enter package name : ").strip()
    prev_char = package_name[0]
    for char in package_name:
        if char == "." and prev_char == ".":
            print(f"Invalid trailing dot sequence in package name {package_name}")
            exit(-1)
        if char.isdigit() or char.isalpha() or char == ".":
            pass
        else:
            print(f"Invalid character \"{char}\" in package name {package_name}")
            exit(-1)
        prev_char = char

    add_build_src = input("Add buildSrc module ?(Y/N)")
    if add_build_src == "Y":
        build_src = True
    print("Creating directories ...")

    print("Creating Project directories ...")

    if build_src:
        create_build_src_dirs()
        print("Created buildSrc.")

    create_project_dirs()
    print("Created project directories.")

    print("Writing to files...")
    write_to_files()
