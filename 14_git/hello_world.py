import time

class GitSimulator:
    def __init__(self):
        self.working_directory = ["hello_world.py", "notes.md"]
        self.staging_area = []
        self.local_repo = []
        self.remote_repo = []

    def status(self):
        print("\n--- git status ---")
        print(f"Working Directory (Modified/New): {self.working_directory}")
        print(f"Staging Area (Ready to commit):   {self.staging_area}")
        print(f"Local Repository (Commits):       {len(self.local_repo)} saved versions")
        print(f"Remote Repository (GitHub):       {len(self.remote_repo)} uploaded versions")
        print("------------------")

    def add(self):
        print("\nExecuting: git add .")
        time.sleep(1)
        self.staging_area = list(self.working_directory)
        self.working_directory = []
        print("Changes successfully moved to the Staging Area!")

    def commit(self, message):
        if not self.staging_area:
            print("\nNothing to commit! Staging area is empty.")
            return
        print(f"\nExecuting: git commit -m '{message}'")
        time.sleep(1)
        commit_hash = "894a7b0"
        commit_data = {"hash": commit_hash, "msg": message, "files": self.staging_area}
        self.local_repo.append(commit_data)
        self.staging_area = []
        print(f"Saved snapshot locally as Commit [{commit_hash}]!")

    def push(self):
        if not self.local_repo:
            print("\nNothing to push! Local repository has no new commits.")
            return
        print("\nExecuting: git push origin main")
        print("Connecting to GitHub...")
        time.sleep(1.5)
        self.remote_repo = list(self.local_repo)
        print("Upload complete! GitHub repository is now up to date.")

if __name__ == "__main__":
    print("=== WELCOME TO THE PYTHON GIT SIMULATOR ===")
    sim = GitSimulator()
    
    # Step 1: Check initial status
    sim.status()
    
    # Step 2: Add files to staging
    sim.add()
    sim.status()
    
    # Step 3: Commit changes
    sim.commit("Complete Chapter 14: Git Basics")
    sim.status()
    
    # Step 4: Push to GitHub
    sim.push()
    sim.status()
    
    print("\n=== SIMULATION ENDED SUCCESSFULLY ===")
