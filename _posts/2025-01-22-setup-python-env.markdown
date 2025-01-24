---
layout: post
title: Setting Up a Python Environment with Miniconda
thumbnail: \public\img\conda.png
---

Miniconda is a lightweight version of Anaconda that includes only Conda, Python, and the packages they depend on. It's ideal for creating isolated Python environments without the bulk of a full Anaconda installation.

This tutorial will guide you through setting up a Python environment using Miniconda.

## 1. Install Miniconda
### Step 1: Download Miniconda
1. Visit the [Miniconda downloads page](https://docs.anaconda.com/miniconda/install/#).
2. Choose the appropriate installer for your operating system (Windows, macOS, or Linux).
![img](\public\img\minicon_download.png)
3. Download the installer.

### Step 2: Install Miniconda
1. Run the installer:
* Windows: Double-click the `.exe` file and follow the instructions.
![img](\public\img\minicon_install.png)
* macOS/Linux: Open a terminal and run the `.sh` script:
    ```
    bash
    bash Miniconda3-latest-Linux-x86_64.sh
    ```
2. Accept the license agreement.
3. Choose the installation location (e.g., `~/miniconda3`).
4. Add Miniconda to your PATH when prompted.

### Step 3: Verify Installation
Open a terminal (or command prompt) and run:

```
bash
conda --version
```
![img](\public\img\conda-ver.png)
You should see the Conda version displayed.

## 2. Create a New Python Environment
### Step 1: Update Conda
Before creating an environment, update Conda to the latest version:

```
bash
conda update -n base -c defaults conda
```

### Step 2: Create the Environment
Create a new environment with a specific Python version:
    
```
bash
conda create --name myenv python=3.9
```

* Replace `myenv` with your desired environment name.
* Replace `3.9` with the Python version you need.

### Step 3: Activate the Environment
Activate the newly created environment:

```
bash
conda activate myenv
```

Your terminal prompt should change to indicate the active environment (e.g., `(myenv)`).

## 3. Install Packages in the Environment
### Using Conda
Install packages available in the Conda repository:
    
```
bash
conda install numpy pandas matplotlib
```

### Using pip
For packages not available in Conda, use `pip`:
    
```
bash
pip install package_name
```

### Check Installed Packages
List all installed packages in the environment:
    
```
bash
conda list
```

## 4. Manage Environments
### Deactivate the Environment
When done, deactivate the environment:
    
```
bash
conda deactivate
```

### List All Environments
View all Conda environments on your system:
    
```
bash
conda env list
```

### Remove an Environment
Delete an unused environment:
    
```
bash
conda remove --name myenv --all
```

## 5. Configure Miniconda for Projects
### Step 1: Create a `requirements.txt` File
List all required packages for your project:

```
txt
numpy==1.21.0
pandas==1.3.0
```

### Step 2: Install Packages from `requirements.txt`
Install the listed packages:
```
bash
pip install -r requirements.txt
```

### Step 3: Export the Environment
Share your environment setup:
```
bash
conda env export > environment.yml
```

### Step 4: Recreate the Environment
Create a new environment from the `.yml` file:
```
bash
conda env create -f environment.yml
```

## 6. Troubleshooting
### Common Issues and Fixes
* Environment not activating: Ensure Conda is added to your PATH. Run:
    ```
    bash
    conda init
    ```

    Then restart your terminal.

* Package conflicts: Use Conda's solver to manage conflicts:
    ```
    bash
    conda install package_name --solver=libmamba
    ```

## Conclusion
Miniconda is a versatile tool for managing Python environments and dependencies efficiently. By following this tutorial, you can set up a clean, isolated environment for your Python projects, ensuring reproducibility and reducing conflicts.