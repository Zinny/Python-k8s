from kubernetes import client,config

config.load_kube_config()

v1=client.CoreV1Api()
print("Listing services with their Resource Versions:")
ret = v1.list_service_for_all_namespaces(watch=False)
for i in ret.items:
     print("{:<30} {:<30}".format (i.metadata.name, i.metadata.resource_version))