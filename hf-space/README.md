---
title: BDI Render
emoji: 🎬
colorFrom: indigo
colorTo: gray
sdk: docker
app_port: 7860
pinned: false
---
BDI Empire render machine (free CPU Space). Takes scripts from firstreceive.com/empire, renders them and hands
them back for quality control. Needs the Space secret `BDI_MACHINE_TOKEN`. Deployed by GitHub Actions
(TriangleOS/bdi-empire, `render-cloud.yml`).
