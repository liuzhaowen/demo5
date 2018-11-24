import yaml

# with open("./data_yaml.yaml", "r") as fr:
#     data_python = yaml.load(fr.read())
#     print(data_python, type(data_python))

with open("./data.yaml", "w", encoding="utf-8") as fw:
    with open("./data_yaml.yaml", "r", encoding="utf-8  ") as fr:
        data_python = yaml.load(fr)
        yaml.dump(data_python, fw)