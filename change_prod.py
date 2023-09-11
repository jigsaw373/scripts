import os

path = "."
target_directory = ".github/workflows"
target_file = "release-production.yml"

old_strings = [
    "AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}",
    "AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}",
    "KUBE_CONFIG_DATA: ${{ secrets.KUBE_CONFIG_DATA }}"
]
new_strings = [
    "AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID_PROD }}",
    "AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY_PROD }}",
    "KUBE_CONFIG_DATA: ${{ secrets.KUBE_CONFIG_DATA_PROD }}"
]

for root, dirs, files in os.walk(path):
    if target_directory in os.path.join(root):
        for file in files:
            if file == target_file:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for old_str, new_str in zip(old_strings, new_strings):
                    content = content.replace(old_str, new_str)
                
                with open(os.path.join(root, file), 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Replacements made in: {os.path.join(root, file)}")
                break

