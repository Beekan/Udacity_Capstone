#!/usr/bin/env python3

from jinja2 import Template

with open("cluster_raw.yml") as fd:     
      deployment_raw = fd.read()
with open("version") as fd:     
      current_version= fd.read()
tm = Template(deployment_raw)
cluster_modified = tm.render(tag=current_version)
with open("cluster.yml", "w") as fd:     
      fd.write(cluster_modified)