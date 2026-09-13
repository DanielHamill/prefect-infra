"""Registers the "dt-shared-dataset" LocalFileSystem block.

The decision_tree flows in sl-report (flows/decision_tree.py) reference this
block by name via Prefect's ResultStore to share a prepared dataset across
the three experiment deployments triggered concurrently on the kube-test
work pool, without hardcoding a filesystem path in flow code. basepath below
must be a directory shared across every kube-test job pod — currently the
hostPath volume mounted at /mnt/prefect-flows (see helm/k8s-template.json).

Self-contained: targets the cluster's Prefect server directly (see
helm/server-values.yaml) regardless of the caller's PREFECT_API_URL/profile.

    python blocks/register_dt_shared_dataset.py

Safe to re-run — overwrites the existing block if the path ever changes.
"""

from prefect.filesystems import LocalFileSystem
from prefect.settings import PREFECT_API_URL, temporary_settings

PREFECT_SERVER_API_URL = "http://danielhamill.me:30200/api"
BLOCK_NAME = "dt-shared-dataset"
BASEPATH = "/mnt/prefect-flows/data/processed"

if __name__ == "__main__":
    with temporary_settings({PREFECT_API_URL: PREFECT_SERVER_API_URL}):
        LocalFileSystem(basepath=BASEPATH).save(BLOCK_NAME, overwrite=True)
        print(f"Registered LocalFileSystem block '{BLOCK_NAME}' -> {BASEPATH}")
