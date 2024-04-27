#!/usr/bin/env python3
"""
DynamoDB Table Copy Script

This script copies data from one DynamoDB table to another.

Author: Martin Wawrzynek
Email: martin@ventx.de
Company: ventx GmbH

Usage:
    python script.py <source_table_name> <destination_table_name>
"""

import boto3
import sys

def copy_dynamodb_table(source_table_name, destination_table_name):
    """
    Copies data from a source DynamoDB table to a destination DynamoDB table.

    :param source_table_name: The name of the source DynamoDB table.
    :param destination_table_name: The name of the destination DynamoDB table.
    """
    # Initialize DynamoDB clients for both source and destination tables
    dynamodb_source = boto3.resource('dynamodb')
    dynamodb_destination = boto3.resource('dynamodb')

    # Get reference to the source and destination tables
    table_source = dynamodb_source.Table(source_table_name)
    table_destination = dynamodb_destination.Table(destination_table_name)

    # Scan the source table and copy each item to the destination table
    response = table_source.scan()
    for item in response['Items']:
        table_destination.put_item(Item=item)
    
    print("Data copied successfully from {} to {}".format(source_table_name, destination_table_name))

# Check if correct number of command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <source_table_name> <destination_table_name>")
    sys.exit(1)

# Extract source and destination table names from command-line arguments
source_table_name = sys.argv[1]
destination_table_name = sys.argv[2]

# Call the function to copy data from source to destination table
copy_dynamodb_table(source_table_name, destination_table_name)
