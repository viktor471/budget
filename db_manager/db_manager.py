from typing import List
from records.record import Record

class DbManager:
    def get_record(self, condition) -> Record:
        pass

    def query(self, table: str, fields: List[str], condition) -> Record:
        pass

    def insert_record(self, record: Record) -> bool:
        pass
