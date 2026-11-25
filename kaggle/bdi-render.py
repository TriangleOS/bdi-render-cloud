# BDI renderer on a Kaggle CPU notebook (free; 12-hour sessions). Pushed and started by GitHub Actions
# (.github/workflows/render-cloud.yml), which writes the machine token into TOKEN below before pushing.
# The notebooks are private. The two CPU notebooks render; the GPU notebook (bdi-render-gpu, BDI_GPU=1) also draws
# the scene pictures itself and makes motion clips with Wan2GP (TriangleOS/deepbeepmeep_Wan2GP) on its second T4,
# about 4 hours a day so the 30 free GPU hours a week are not exceeded.
import os, subprocess
TOKEN = "__BDI_MACHINE_TOKEN__"
env = dict(os.environ, BDI_MACHINE_TOKEN=TOKEN, BDI_MACHINE_NAME="kaggle", BDI_GPU="0", MAX_MINUTES="680", BDI_WORK="/kaggle/working/bdi")
subprocess.run("curl -fsSL https://firstreceive.com/empire/dl/run.sh -o /tmp/run.sh", shell=True, check=True)
subprocess.run(["bash", "/tmp/run.sh"], env=env, check=False)
