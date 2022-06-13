# -*- coding: utf-8 -*-


def is_env_notebook():
    """Determine wheather is the environment Jupyter Notebook"""
    try:
        env_name = get_ipython().__class__.__name__
    except NameError:
        return False

    if env_name == "TerminalInteractiveShell":
        # IPython shell
        return False
    else:
        # Jupyter Notebook
        return True
