from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'

    copy_sql = """
        COPY {} 
        FROM '{}'
        CREDENTIALS 'aws_iam_role={}'
        COMPUPDATE OFF 
        REGION '{}' 
        JSON '{}'
    """

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
        execution_date = context['execution_date']
        s3_path = 's3://{}/{}/{}/{}/{}'
        
        if self.s3_key == 'log-data':
            full_s3_path = s3_path.format(
                self.s3_bucket,
                self.s3_key,
                execution_date.strftime('%Y'),
                execution_date.strftime('%m'),
                f"{execution_date.strftime('%Y-%m-%d')}-events.json"
            )
        else:
            full_s3_path = s3_path.format(
                self.s3_bucket,
                self.s3_key,
                'A',
                'A',
                'A'
            )

        formatted_sql = self.copy_sql.format(
            self.table,
            full_s3_path,
            self.aws_iam_role,
            self.region,
            self.json
        )
        
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info(f"Copying data from S3 to {self.table} table in Redshift Serverless")
        redshift_hook.run(formatted_sql)
        self.log.info(f"Finished copying data to {self.table} table")
