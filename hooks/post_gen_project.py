#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == "__main__":
    if "{{ cookiecutter.json4s_version }}" == '-':
        remove_file("src/test/scala/TestJson.scala")

    if "{{ cookiecutter.scalapb_compilerplugin_version }}" == '-':
        remove_file("src/test/scala/TestProtobuf.scala")
        remove_file("project/scalapb.sbt")
        remove_dir("src/main/protobuf")
