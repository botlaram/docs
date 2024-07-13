"""nox to create init workspace"""

import os
import pathlib
import nox

TOOL_NAME="docs"
THIS_DIRECTORY=pathlib.Path(__file__).parent.resolve()
LOCAL_FOLDER=os.getenv("LOCAL_WORKSPACE_FOLDER",str(THIS_DIRECTORY))

@nox.session(python=False)  #this session will not be run in a virtual environment
def init_workspace(session: nox.Session) -> None :
    """update git config"""
    
    session.run(
        "git", "config", "--global", "credential.useHttpPath", "true" ,external=True
    )    
    
    # to clear out any directories that have been marked as safe in the Git global configuration
    session.run(
        "git",
        "config",
        "--global",
        "--unset-all",
        "safe.directory",
        external=True,
        success_codes=[0,5],
    )
    
    session.run(
        "git",
        "config",
        "--global",
        "--add",
        "safe.directory",
        str(THIS_DIRECTORY),
        external=True,
    )
    
    # this command is to configure Git to recognize each submodule directory (and nested submodules, if any) as a safe directory. 
    session.run(
        "git",
        "submodule",
        "foreach",
        "--recursive",
        "git config --global --add safe.directory $PWD",
        external=True,
    )
    
    session.run(
        "pip",
        "install",
        "--no-cache-dir",
        "-r",
        "requirements.txt"
    )
