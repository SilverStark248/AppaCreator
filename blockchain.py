import subprocess

def deploy_contract(contract_path: str):
    try:
        result = subprocess.run(
            ["seid", "tx", "wasm", "store", contract_path, "--from", "mywallet", "--chain-id", "atlantic-2", "--gas", "auto", "--gas-adjustment", "1.3", "--yes"],
            capture_output=True,
            text=True
        )
        return {"status": "success", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "details": str(e)}
