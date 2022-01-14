name = "hello_world"

version = "1.0.4"

authors = [
    "ajohns"
]

description = \
    """
    Python-based hello world example package.
    """

tools = [
    "hello"
]

requires = [
    "python"
]

uuid = "examples.hello_world_py"

build_command = 'python {root}/build.py {install}'


def commands():
    env.PYTHONPATH.append("{root}/python")
    env.PATH.append("{root}/bin")
    env.PATH.append(
        "C:/Program Files/Side Effects Software/Houdini 18.5.618/bin")
