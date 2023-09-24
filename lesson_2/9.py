import json

raw_json = [{"123": 123, "sdgfsd": [1, {"3": 123}]}, {"sdf": {"k": [1, 2, 3]}}]
json_ = json.dumps(raw_json)
with open("9.json", "w") as output_stream:
    json.dump(raw_json, output_stream)

with open("9.json", "r") as input_stream:
    raw_json_2 = json.load(input_stream)

print(json_)
print(raw_json_2)