# Archi-Cloud-FINOPS-Course Lab5

## Steps

### 1. Deploy an Azure SQL Database Instance


1. **Create a SQL Database**:
   - Click on **Create a resource** > **Databases** > **SQL Database**.
   ![SQL Database Creation](./creatingDB.png)

### 2. Configure Firewall Settings to Allow Client Access

1. **Navigate to Your SQL Server**:
   - In the Azure portal, navigate to **SQL Servers** > select your server.

2. **Set Up Firewall Rules**:
   - Under **Security + networking**, click on **Firewalls and virtual networks**.
   - Click **Add client IP** to automatically add your current IP address for access.
   - You can also manually add IP ranges if necessary.
   - Click **Save** to apply the firewall rules.

3. **Enable Azure Services Access**:
   - Ensure the option **Allow Azure services and resources to access this server** is set to **Yes** if you want to allow other Azure resources to connect.


   - still working on it 

### 3. Import Data into the Database
1. **Connect to Azure SQL Database via Azure CLI**:
   ```bash
   az sql db show --resource-group lab5 --server serverlab5 --name lab5-DB

2. **Execute this commande**:
    ```bash
    sqlcmd -S serverlab5.database.windows.net -U anass -P Azerty12345@+ -d lab5-DB -i PATH/data.sql


 - still working on it 

### 4. Implement Geo-replication for High Availability

1. **Enable Geo-replication**:
    ```bash
    az sql db replica create --resource-group <ResourceGroupName> --server <ServerName> --name <DatabaseName> --partner-server <SecondaryServerName> --partner-resource-group <SecondaryResourceGroup>

2. **Monitor Replication**:
    ```bash
    az sql db replica list-links --resource-group <ResourceGroupName> --server <ServerName> --name <DatabaseName>

 - still working on it 