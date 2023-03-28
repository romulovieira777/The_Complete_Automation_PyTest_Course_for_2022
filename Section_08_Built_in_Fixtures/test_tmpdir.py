"""
Created on March 03, 2023

@author: Romulo
"""


def test_tmpdir(tmpdir):
    a_file = tmpdir.join("something.txt")
    a_sub_dir = tmpdir.mkdir("anything")
    another_file = a_sub_dir.join("other_file.txt")

    a_file.write("Hello everyone, how are you doing")
    another_file.write("Hi no one")

    assert a_file.read() == "Hello everyone, how are you doing"
    assert another_file.read() == "Hi no one"


def test_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp("mydir")

    base_temp = tmpdir_factory.getbasetemp()
    print('Base: ', base_temp)

    a_file = a_dir.join("something.txt")
    a_sub_dir = a_dir.mkdir("anything")
    another_file = a_sub_dir.join("something_else.txt")

    a_file.write("Hello everyone, how are you doing")
    another_file.write("Hi no one")

    assert a_file.read() == "Hello everyone, how are you doing"
    assert another_file.read() == "Hi no one"
