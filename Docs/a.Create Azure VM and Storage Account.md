# Create Azure Virtual Machine on Azure, Storage Account and containers

## Step 0. Create Azure Account
## Step 1. Create Virtual Machine service
#### 1.1 Navigate to the Home of Azure, click "Create a resource"
#### 1.2 Click Virtual Machine
#### 1.3. Configure the new Virtual Machine
##### 1.3.1 Basics:
	- Subscription: if you have "Free trial" subscription, please select this, it is free; otherwise select the default one -- "Pay-As-You-Go";
	- Resource Group: click "Create New" and assign a meaningful name "AzureProjectRG"
	- Virtual machine name: Give the virtual machine a meaningful name
	- Region: select your region
	- Image: Ubuntu 20.04 LTS
	- Size: "Standard_B1s"
	- Authentication type: SSH public key
	- Username
	- SSH public key source: Create a new key pair, and download it later when generating the virtual machine; save it to the place where you put all the key pair files on you local computer
	- Public inbound port: Allow selected ports> select SSH(22) port
##### 1.3.2 Disks:
	- OS disk type: Standard HDD(local-redundant storage)
##### 1.3.3 Review + Create 
#### 1.4. Connect to the Virtual Machine using the pem file generated in 1.3.1

## Step 2. Create Storage service
#### 2.1 Navigate to the Home of Azure, click "Create a resource"
#### 2.2 Find Storage and Click Storage account
#### 2.3. Configure the new Storage account
##### 2.3.1 Basics:
	- Resource Group: select the one created for VM in Step 1.3.1
	- Storage account name: Give the Storage account name a meaningful name
	- Region: select your region
	- Redundancy: Locally-redundant storage（LRS) (this is the lowest cost one)
##### 2.3.2 Advanced, this is where the data lake is created by ticking the following property:
	- Enable hierarchical namespace: True

##### 2.3.3 Networking:
	- Network access: Enable public access from all networks
##### 2.3.4 Review + Create 

## Step 3. Create Container

#### 3.1 Navigate to the Storage Account in Step 2
#### 3.2 Click on Overview > Containers, and create a new container to store the input files to the container
	- select Name of the container "bd-project"


