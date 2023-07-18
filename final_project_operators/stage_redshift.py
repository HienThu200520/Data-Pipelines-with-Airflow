from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'

    @apply_defaults
    def __init__(
        self,
        table='',
        s3_bucket='',
        s3_key='',
        aws_iam_role='',
        region='us-west-2',
        json='auto',
        redshift_conn_id='',
        provide_context=False,
        *args, **kwargs
    ):
        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.table = table
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.aws_iam_role = aws_iam_role
        self.region = region
        self.json = json
        self.redshift_conn_id = redshift_conn_id
        self.provide_context = provide_context

    def execute(self, context):
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info(f"Copying data from S3 to {self.table} table in Redshift")

        # Generate the copy statement dynamically using parameters
        copy_sql = """
            COPY {table}
            FROM 's3://{s3_bucket}/{s3_key}'
            CREDENTIALS 'aws_iam_role={aws_iam_role}'
            REGION '{region}'
            JSON '{json}'
        """.format(
            table=self.table,
            s3_bucket=self.s3_bucket,
            s3_key=self.s3_key,
            aws_iam_role=self.aws_iam_role,
            region=self.region,
            json=self.json
        )

        redshift_hook.run(copy_sql)
        self.log.info(f"Finished copying data to {self.table} table")
