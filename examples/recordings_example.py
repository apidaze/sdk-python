from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET)


def getRecording(filename: str):
    response = apidaze.recordings.get(filename)
    data = response['body']
    file = open(filename, 'wb')
    file.write(data)
    file.close()


def removeRecording(filename: str):
    response = apidaze.recordings.remove(filename)
    print(response)


def listRecordings():
    response = apidaze.recordings.list()
    print(response)


listRecordings()

# recordings = ['1a852934-aa09-43a4-b239-12e6e41eb271', '1bba83df-7657-46fb-bc1d-a7e11f962043', '1e11b3bd-ca56-4c3b-b99c-b5864c909cbb', '20b4675e-9b2c-43b5-bdea-7cf04e11cdc0', '225eaccc-01a6-4209-8fd3-0b8d508643dc', '25f82d84-c820-43b1-8e28-a83429ec6070', '29c492ad-4679-48a0-9516-1841b7422811', '2c9f0b7f-b99e-4a49-ac1f-f9f090b3d2f1', '2d0cd292-cc4a-4b50-ab62-dd86e8eef51a', '2d192743-7e29-4b79-ac9a-ec2e27bd6ea8', '3ac2e5b5-9b23-4b1a-8cdf-09a7c312057a', '3d8fb06b-faa9-49c4-be5d-e592efd3453d', '46dd16d9-1ce0-46cd-af5f-ffccc7c00051', '51c6660d-3ae5-4c13-bbf4-2e7c35897f3d', '561ec656-aa82-42ad-90d2-14ee552d4352', '603a8df1-326e-45eb-b475-cfa56eb680e8', '68814dab-e6bc-448c-8dad-2c7665866970', '68ba7f95-3320-4621-a751-2446b25c4191', '6a6ee4fd-2bd9-41a4-bd26-c3994df638ea', '74581a73-fa38-4755-b5ad-fddce75e0e8b', '7e4a5b20-74c9-4b2e-9169-60ffc431cb05', '8341c907-29ee-4ff5-bc9c-69b5723a9815', '862627cf-bee5-4e7d-86f6-df984bd5c66a', '8b238878-97f0-4518-919a-c42830a995b5', '8c69e2d2-f8ff-4499-9348-3424a180949d', '9a25d803-b048-402f-8c20-fd963e583383', '9d0956fe-8d46-4434-a94c-8e2f54661746', 'a1a9e1dc-fb73-4a49-9c93-794e54c40067', 'a25a7075-b48c-4b66-8aa7-c63219a3d975', 'a3386739-464d-4f06-897f-0c3c0758d430', 'a40716f9-e565-4048-91cb-bac697cdae0e', 'a6720d87-f782-48e2-8927-f58336ee0a81', 'aa245253-622e-4e31-911e-507b61775e1d', 'aab07c82-542c-4101-9c47-f084edd987f3', 'ac0e30f6-ca75-45ac-ab04-a140b5fa4103', 'ad77614d-d40c-491b-8afd-01a20a87786e', 'af7a2d65-72cd-4cba-8908-dcdedb407a68', 'b00b6e00-9e8d-4d36-82fb-f3319c76bde4', 'b3e52719-7d8c-453b-99ff-e9aaf3524e96', 'b5547213-4d96-402b-bab3-9fbe171123b9', 'b7e616af-0fc4-4fc7-b768-a517bdded7d4', 'b7eadda0-0506-46bc-8aa1-2a2725f8e65d', 'b807261a-5b90-46a7-88b1-cef72019aea5', 'bartosz_recording1', 'be6fbac5-a960-4a7b-b4d0-36479cc981fc', 'be8ec994-aa79-4a17-8072-d948d26ecbc0', 'c55e6bd8-10e6-4b90-b2dc-652fc5fc79e4', 'c9824032-153e-4531-9b4b-5329a91fbd2a', 'cc64d966-87e8-453e-94d3-ea1e14174abc', 'cee6709c-da0f-46b7-8e50-93e669a75f9f', 'd62e251d-1ad6-4471-a789-a067f2abec83', 'daf6cba9-2cab-4c2a-81dd-f98038424a61', 'db304411-27d9-41bb-9058-a75b20920b53', 'e1d15e12-7d60-4e1d-b8f3-6d9a0363556c', 'e704bd37-b0cf-400c-bfbd-315e2e169917', 'e7d5c9e3-48cc-414c-a606-1b2101e3a169', 'ea3ec6a7-2a62-498e-90c6-1bb45165f6f8', 'example_recording', 'fba911c6-2f68-45a3-bd99-d6a8f9e21427', 'ff9ac74b-a622-4699-90b5-9dea837f7994', 'my_recording']
# for recording in recordings:
#     print(f"Removing recording {recording}")
#     removeRecording(recording)

