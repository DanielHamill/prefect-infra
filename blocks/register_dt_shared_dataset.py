"""Registers the "dt-shared-dataset" LocalFileSystem block.

The decision_tree flows in sl-report (flows/decision_tree.py) reference this
block by name via Prefect's ResultStore to share a prepared dataset across
the three experiment deployments triggered concurrently on the kube-test
work pool, without hardcoding a filesystem path in flow code. basepath below
must be a directory shared across every kube-test job pod — currently the
hostPath volume mounted at /mnt/prefect-flows (see helm/k8s-template.json).

Run once against whichever Prefect server flows are pointed at (uses the
active PREFECT_API_URL / profile, same as any other prefect command):

    python blocks/register_dt_shared_dataset.py

Safe to re-run — overwrites the existing block if the path ever changes.
"""

from prefect.filesystems import LocalFileSystem

BLOCK_NAME = "dt-shared-dataset"
BASEPATH = "/mnt/prefect-flows/data/processed"

if __name__ == "__main__":
    LocalFileSystem(basepath=BASEPATH).save(BLOCK_NAME, overwrite=True)
    print(f"Registered LocalFileSystem block '{BLOCK_NAME}' -> {BASEPATH}")
