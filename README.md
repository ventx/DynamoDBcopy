# DynamoDB Table Copy Script

## Overview
This Python script allows you to copy data from one DynamoDB table to another. It utilizes the Boto3 library, the AWS SDK for Python, to interact with DynamoDB.

> **_WARNING:_**  - Be cautious when running the script as it will overwrite existing data in the destination table.

> **_NOTE:_**  - Ensure that both the source and destination tables exist in your AWS account.
> **_NOTE:_**  - Ensure that the IAM user or role associated with the AWS credentials used by the script has the necessary permissions to read from the source DynamoDB table and write to the destination DynamoDB table.

## Prerequisites
1. Python3 installed on your system.
2. Boto3 library installed (`pip install boto3`).
3. AWS credentials configured on your system with appropriate permissions to read from the source DynamoDB table and write to the destination DynamoDB table.

## Exporting AWS Environment Variables
Before running the script, you need to export your AWS credentials as environment variables. You can do this using the following commands:

```bash
export AWS_ACCESS_KEY_ID=<your_access_key_id>
export AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
export AWS_DEFAULT_REGION=<your_aws_region>
```
or
```bash
export AWS_PROFILE=<your_profile_name>
export AWS_DEFAULT_REGION=<your_aws_region>
```

## Usage
1. Clone or download the script to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the following command:

    ```bash
    python DynamoDBcopy.py <source_table_name> <destination_table_name>
    ```

    Replace `<source_table_name>` and `<destination_table_name>` with the names of your source and destination DynamoDB tables respectively.

5. Once executed, the script will copy all data from the source table to the destination table.

## Example
Suppose you have two DynamoDB tables named `source_table` and `destination_table`, and you want to copy data from `source_table` to `destination_table`. You would run the script as follows:

```bash
python DynamoDBcopy.py source_table destination_table
```