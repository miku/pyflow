import subprocess

def ls():
    subprocess.run(["ls"], shell=True)


def test_ls(capsys):
    ls()
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""

def test_ls_fd(capfd):
    ls()
    out, err = capfd.readouterr()
    assert "test_ls" in out
    assert err == ""