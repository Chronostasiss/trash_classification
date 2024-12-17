import os

# Verify W&B API Key
wandb_key = os.getenv("WANDB_API_KEY")
hf_token = os.getenv("HF_TOKEN")

print(f"WANDB_API_KEY: {wandb_key}")
print(f"HF_TOKEN: {hf_token}")

if wandb_key and hf_token:
    print("Secrets are accessible locally!")
else:
    print("Secrets are missing. Check your environment setup.")