class BraveInstaller:
    def __init__(self):
        self.installed = self.check_installed()

    def check_installed(self):
        import shutil
        return shutil.which('brave-browser') is not None

    def install(self):
        if self.installed:
            print("Brave is already installed.")
        else:
            print("Installing Brave...")
            import subprocess
            try:
                subprocess.run(
                    "curl -fsS https://dl.brave.com/install.sh | sh",
                    shell=True,
                    check=True
                )
                print("Brave installed successfully.")
                self.installed = True
            except subprocess.CalledProcessError as e:
                print(f"Installation failed: {e}")