'''helper suite for interacting with AWS S3. primarily for reading and writing
list uploads for the wargaming side of the app.'''

import boto3

class TTUtilsS3:
    '''S3 connection wrapper class'''

    def __init__(self, bucket, prefix=None):
        self.bucket = bucket
        self.prefix = prefix if prefix else ''
        self.client = boto3.client('s3')

    def get_user_object(self, object_name):
        '''retrieve an object for a particular user'''

        key = f"{self.prefix}/{object_name}"
        obj = self.client.get_object(Bucket=self.bucket, Key=key)

        return obj['Body'].read().decode('utf-8')

    def list_user_objects(self, limit=10, public=False, user=None):
        '''list the latest objects uploaded by the user'''

        # short-circuit if public or user left unspecified
        if not public and not user:
            return []

        response = self.client.list_objects_v2(
            Bucket=self.bucket,
            Prefix=self.prefix
        )

        # short-circuit if no contents
        if not response['Contents']:
            return []

        # need most recent first
        contents = sorted(response['Contents'], key=lambda r: r['LastModified'])

        # iterate over the recent objects and skip anything not belonging to a
        # user or is specified public
        objects = []
        for row in contents:
            if len(objects) == limit:
                break

            tags = self.client.get_object_tagging(
                Bucket=self.bucket,
                Key=row['Key']
            )

            # set tags on the object so they're easier to access in templates
            obj = {}
            for tag in tags['TagSet']:
                obj[tag['Key']] = tag['Value']

            if user and user == obj.get('owner', None):
                objects.append(obj)
            elif public and bool(obj.get('public', False)):
                objects.append(obj)

        return objects
