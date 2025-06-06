import argparse
from train import train_model
from eval import evaluate_model
import yaml
import wandb
from dotenv import load_dotenv
import os

def main():
    
    # wandb 로그인
    load_dotenv(verbose=True)               # .env심기
    wandb_api_key = os.getenv("WANDB_API_KEY")
    if wandb_api_key:
        wandb.login(key=wandb_api_key)
    else:
        print("Warning: WANDB_API_KEY not set. wandb login skipped.")
        assert False, "WANDB_API_KEY environment variable is missing."

    parser = argparse.ArgumentParser(description="LLaMA 3 Instruction Tuning with Unsloth and wandb")
    parser.add_argument('--mode', choices=['train', 'eval'], required=True)
    parser.add_argument('--config', type=str, required=True, help='Path to config YAML')
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    if args.mode == 'train':
        train_model(config)
    else:
        evaluate_model(config)


if __name__ == "__main__":
    main()