import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

def on_chain_abi(contract_address):
    token = os.environ.get(f"{network}_API_TOKEN", "")
    endpoint = os.environ.get(f"{network}_API_ENDPOINT")
    api_url = f"{endpoint}?module=contract&action=getabi&address={contract_address}&apikey={token}"
    # Note AVAX uses routescan as API
    if token != "":
        api_url += f"&apikey={token}"

    response = requests.get(api_url)

    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        return None

    data = response.json()

    if data.get("status") == "0":
        print(data.get("result"))  # error message
        return None

    try:
        contract_abi = json.loads(data.get("result"))
        return contract_abi
    except Exception as e:
        print(e)
        return None

def process_contracts(network):
    csv_file = f"data/{network.lower()}/contracts.csv"
    if not os.path.isfile(csv_file):
        print(f"File {csv_file} not found")
        return

    df = pd.read_csv(csv_file)
    df2 = df[0:2]
    contracts = df2["ContractAddress"].tolist()

    data_state = []
    for contract in contracts:
        contract_abi = on_chain_abi(contract)
        if contract_abi:
            print(f"Processing {contract}")
            for abi in contract_abi:
                if "stateMutability" in abi:
                    stateMutability = abi["stateMutability"]
                    del abi["stateMutability"]
                    data_state.append([abi, stateMutability])
        else:
            print(f"Skipping {contract}")

    df_state = pd.DataFrame(data_state, columns=['text', 'target'])
    df_state.to_csv(f"{network.lower()}-{df2.shape[0]}.csv", encoding='utf-8', index=False)

if __name__ == "__main__":
    load_dotenv()

    # network = ETHERSCAN, POLYGONSCAN, OPTIMISTIC_ETHERSCAN
    network = "ETHERSCAN"
    process_contracts(network)
