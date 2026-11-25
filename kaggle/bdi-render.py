# BDI renderer on a Kaggle CPU notebook (free; 12-hour sessions). Pushed and started by GitHub Actions
# (.github/workflows/render-cloud.yml), which writes the machine token into TOKEN below before pushing.
# The notebook is private. GPU is left off so the 30 free GPU hours a week stay for clip generation.
import os, subprocess
TOKEN = "__BDI_MACHINE_TOKEN__"
env = dict(os.environ, BDI_MACHINE_TOKEN=TOKEN, BDI_MACHINE_NAME="kaggle", MAX_MINUTES="680", BDI_WORK="/kaggle/working/bdi")
subprocess.run("curl -fsSL https://firstreceive.com/empire/dl/run.sh -o /tmp/run.sh", shell=True, check=True)
subprocess.run(["bash", "/tmp/run.sh"], env=env, check=False)
