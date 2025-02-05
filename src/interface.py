from abc import ABC, abstractmethod

from sqlalchemy import text

from . import HiscoreRecord, get_session


class BenchmarkABC(ABC):
    def get_size(self):
        query = text(
            """
            SELECT table_name AS `Table`, 
                ROUND(((data_length + index_length) / 1024 / 1024), 2) AS `Size (MB)` 
            FROM information_schema.TABLES 
            WHERE table_schema = :database
        """
        )
        with get_session() as session:
            result = session.execute(query, params={"database": "playerdata"})
            data = result.fetchall()
        return data

    @abstractmethod
    def insert_many_records(self, records: list[HiscoreRecord]) -> None:
        """
        Insert multiple records into the database.

        Args:
            records (list[HiscoreRecord]): A list of HiscoreRecord instances to be inserted into the database.
        """
        pass

    @abstractmethod
    def get_latest_record_for_player(self, player_id: int) -> HiscoreRecord:
        """
        Retrieve the latest record for a specific player.

        Args:
            player_id (int): The ID of the player whose latest record is to be retrieved.

        Returns:
            HiscoreRecord: The latest record for the specified player.
        """
        pass

    @abstractmethod
    def get_latest_record_for_many_players(
        self, players: list[int]
    ) -> list[HiscoreRecord]:
        """
        Retrieve the latest record for each of the specified players.

        Args:
            players (list[int]): A list of player IDs whose latest records are to be retrieved.

        Returns:
            list[HiscoreRecord]: A list of the latest records for the specified players.
        """
        pass

    @abstractmethod
    def get_all_records_for_player(self, player_id: int) -> list[HiscoreRecord]:
        """
        Retrieve all records for a specific player.

        Args:
            player_id (int): The ID of the player whose records are to be retrieved.

        Returns:
            list[HiscoreRecord]: A list of all records for the specified player.
        """
        pass

    @abstractmethod
    def get_all_records_for_many_players(
        self, players: list[int]
    ) -> list[HiscoreRecord]:
        """
        Retrieve all records for each of the specified players.

        Args:
            players (list[int]): A list of player IDs whose records are to be retrieved.

        Returns:
            list[HiscoreRecord]: A list of all records for the specified players.
        """
        pass
