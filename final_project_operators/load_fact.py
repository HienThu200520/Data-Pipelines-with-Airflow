from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):
    ui_color = '#F98866'

    @apply_defaults
    def __init__(
        self,
        sql_statement='',
        table='',
        redshift_conn_id='',
        *args, **kwargs
    ):
        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.sql_statement = sql_statement
        self.table = table
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        self.log.info(f"Transforming staging data and inserting query result into fact table - {self.table}")
        results = redshift_hook.get_records(self.sql_statement)

        redshift_hook.insert_rows(self.table, results)
        self.log.info(f"Successfully inserted data into fact table - {self.table}.")
