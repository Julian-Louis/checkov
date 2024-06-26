from aws_cdk import core
from aws_cdk import aws_glue as glue

class MyGlueDataCatalogEncryptionSettingsStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define Data Catalog encryption settings
        data_catalog_encryption_settings = glue.CfnDataCatalogEncryptionSettings(
            self, 'MyGlueDataCatalogEncryptionSettings',
            data_catalog_encryption_settings={
                'ConnectionPasswordEncryption': {
                    'ReturnConnectionPasswordEncrypted': False
                },
                'EncryptionAtRest': {
                    'CatalogEncryptionMode': 'SSE-KMS'
                }
            }
        )

app = core.App()
MyGlueDataCatalogEncryptionSettingsStack(app, "MyGlueDataCatalogEncryptionSettingsStack")
app.synth()

class MyGlueDataCatalogEncryptionSettingsStack2(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define Data Catalog encryption settings
        data_catalog_encryption_settings = glue.CfnDataCatalogEncryptionSettings(
            self, 'MyGlueDataCatalogEncryptionSettings',
            data_catalog_encryption_settings={
                'ConnectionPasswordEncryption': {
                    'ReturnConnectionPasswordEncrypted': True
                },
            }
        )

app = core.App()
MyGlueDataCatalogEncryptionSettingsStack2(app, "MyGlueDataCatalogEncryptionSettingsStack2")
app.synth()
