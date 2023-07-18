from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):
    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(
        self,
        sql_statement='',
        table='',
        append_only=False,
        redshift_conn_id='',
        *args, **kwargs
    ):
        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.sql_statement = sql_statement
        self.table = table
        self.append_only = append_only
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        if not self.append_only:
            self.log.info(f"Deleting all records from dimension table - {self.table}")
            redshift_hook.run(f"TRUNCATE {self.table}")

        self.log.info(f"Transforming staging data and inserting query result into dimension table - {self.table}")
        results = redshift_hook.get_records(self.sql_statement)

        redshift_hook.insert_rows(self.table, results)
        self.log.info(f"Successfully inserted data into dimension table - {self.table}.")
