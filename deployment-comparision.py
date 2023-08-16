import subprocess
import yaml
import sys

def get_remote_deployments():
    remote_deployments = []
    try:
        remote_output = subprocess.check_output(['kubectl', 'get', 'deployments', '-o', 'yaml'])
        remote_data = yaml.safe_load(remote_output)
        remote_deployments = remote_data.get('items', [])
    except subprocess.CalledProcessError as e:
        print("Error getting remote deployments:", e)
    return remote_deployments

def load_local_deployments(file_path):
    try:
        with open(file_path, 'r') as file:
            local_data = yaml.safe_load(file)
            local_deployments = local_data.get('items', [])
            return local_deployments
    except FileNotFoundError:
        print("Local deployments file not found.")
        return []

def compare_deployments(remote_deployments, local_deployments):
    remote_names = {deployment['metadata']['name'] for deployment in remote_deployments}
    local_names = {deployment['metadata']['name'] for deployment in local_deployments}

    missing_in_remote = local_names - remote_names
    missing_in_local = remote_names - local_names

    return missing_in_remote, missing_in_local

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python deployment_checker.py <path_to_local_deployments_file>")
        sys.exit(1)

    local_deployments_file = sys.argv[1]
    remote_deployments = get_remote_deployments()
    local_deployments = load_local_deployments(local_deployments_file)

    missing_in_remote, missing_in_local = compare_deployments(remote_deployments, local_deployments)

    if missing_in_remote:
        print("Deployments missing in the remote cluster:", missing_in_remote)
    else:
        print("No deployments missing in the remote cluster.")

    if missing_in_local:
        print("Deployments missing locally:", missing_in_local)
    else:
        print("No deployments missing locally.")

