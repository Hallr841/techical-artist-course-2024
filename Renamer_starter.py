import os 
import argparse


def rename_files(source_path, target_path):
    """Rename files."""
    for filename in os.listdir(source_path):
        source_file = os.path.join(source_path,filename)
        target_file = os.path.join(target_path,filename)
        os.rename(source_file,target_file)
        print(f"Remaned {source_file}to{target_file}")

def main():
    parser = argparse.ArgumentParser(description="Batch remamer Python Script")
    parser.add_argument("source_path", type=str, help=" Full filepath to the source folder")
    parser.add_argument("target_path", type=str, help=" Full filepath to the target folder")
    args = parser.parse_args()

    #remane files   
    rename_files(args.source_path, args.target_path)

if __name__=="__main__":
  main()