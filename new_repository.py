"""
New Repository Module
=====================

This module implements a Repository pattern for data access in the Coco Bambu data engineering project.
The Repository pattern provides an abstraction layer between the business logic and data access logic.

Classes:
    NewRepository: Main repository class for managing data operations
"""

import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime


class NewRepository:
    """
    NewRepository class implements the Repository pattern for data access.
    
    This class provides methods to interact with the data lake structure,
    allowing for easy data retrieval, storage, and management operations.
    
    Attributes:
        base_path (str): Base path for the data lake
        store_id (int): Store identifier
        bus_dt (str): Business date in YYYY-MM-DD format
    """
    
    def __init__(self, base_path: str = "./data_lake", store_id: int = 1, bus_dt: str = None):
        """
        Initialize the NewRepository.
        
        Args:
            base_path (str): Base path for the data lake directory
            store_id (int): Store identifier (default: 1)
            bus_dt (str): Business date in YYYY-MM-DD format (default: today)
        """
        self.base_path = base_path
        self.store_id = store_id
        self.bus_dt = bus_dt or datetime.now().strftime("%Y-%m-%d")
        self.data_path = os.path.join(
            base_path,
            f"store_id={store_id}",
            f"bus_dt={self.bus_dt}"
        )
    
    def _ensure_path_exists(self) -> None:
        """Create the data path directory structure if it doesn't exist."""
        os.makedirs(self.data_path, exist_ok=True)
    
    def save_json(self, filename: str, data: List[Dict[str, Any]]) -> bool:
        """
        Save data to a JSON file in the data lake.
        
        Args:
            filename (str): Name of the JSON file (e.g., 'dim_lojas.json')
            data (List[Dict]): List of dictionaries containing the data to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self._ensure_path_exists()
            filepath = os.path.join(self.data_path, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving JSON file {filename}: {str(e)}")
            return False
    
    def load_json(self, filename: str) -> Optional[List[Dict[str, Any]]]:
        """
        Load data from a JSON file in the data lake.
        
        Args:
            filename (str): Name of the JSON file to load
            
        Returns:
            Optional[List[Dict]]: List of dictionaries with the data, or None if error
        """
        try:
            filepath = os.path.join(self.data_path, filename)
            
            if not os.path.exists(filepath):
                print(f"File not found: {filepath}")
                return None
            
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return data
        except Exception as e:
            print(f"Error loading JSON file {filename}: {str(e)}")
            return None
    
    def save_dim_lojas(self, data: List[Dict[str, Any]]) -> bool:
        """Save store dimension data."""
        return self.save_json("dim_lojas.json", data)
    
    def save_dim_datas(self, data: List[Dict[str, Any]]) -> bool:
        """Save date dimension data."""
        return self.save_json("dim_datas.json", data)
    
    def save_dim_itens(self, data: List[Dict[str, Any]]) -> bool:
        """Save items dimension data."""
        return self.save_json("dim_itens.json", data)
    
    def save_fato_pedidos(self, data: List[Dict[str, Any]]) -> bool:
        """Save orders fact table data."""
        return self.save_json("fato_pedidos.json", data)
    
    def save_detail_lines(self, data: List[Dict[str, Any]]) -> bool:
        """Save detail lines data."""
        return self.save_json("detail_lines.json", data)
    
    def save_detail_metadata(self, data: List[Dict[str, Any]]) -> bool:
        """Save detail metadata."""
        return self.save_json("detail_metadata.json", data)
    
    def load_dim_lojas(self) -> Optional[List[Dict[str, Any]]]:
        """Load store dimension data."""
        return self.load_json("dim_lojas.json")
    
    def load_dim_datas(self) -> Optional[List[Dict[str, Any]]]:
        """Load date dimension data."""
        return self.load_json("dim_datas.json")
    
    def load_dim_itens(self) -> Optional[List[Dict[str, Any]]]:
        """Load items dimension data."""
        return self.load_json("dim_itens.json")
    
    def load_fato_pedidos(self) -> Optional[List[Dict[str, Any]]]:
        """Load orders fact table data."""
        return self.load_json("fato_pedidos.json")
    
    def load_detail_lines(self) -> Optional[List[Dict[str, Any]]]:
        """Load detail lines data."""
        return self.load_json("detail_lines.json")
    
    def load_detail_metadata(self) -> Optional[List[Dict[str, Any]]]:
        """Load detail metadata."""
        return self.load_json("detail_metadata.json")
    
    def get_all_tables(self) -> Dict[str, Optional[List[Dict[str, Any]]]]:
        """
        Load all available tables from the data lake.
        
        Returns:
            Dict: Dictionary with table names as keys and their data as values
        """
        return {
            "dim_lojas": self.load_dim_lojas(),
            "dim_datas": self.load_dim_datas(),
            "dim_itens": self.load_dim_itens(),
            "fato_pedidos": self.load_fato_pedidos(),
            "detail_lines": self.load_detail_lines(),
            "detail_metadata": self.load_detail_metadata()
        }
    
    def list_available_files(self) -> List[str]:
        """
        List all JSON files available in the current data path.
        
        Returns:
            List[str]: List of available JSON filenames
        """
        try:
            if not os.path.exists(self.data_path):
                return []
            
            files = [f for f in os.listdir(self.data_path) if f.endswith('.json')]
            return files
        except Exception as e:
            print(f"Error listing files: {str(e)}")
            return []


def main():
    """
    Example usage of NewRepository class.
    """
    # Initialize repository
    repo = NewRepository(base_path="./data_lake", store_id=1, bus_dt="2024-01-01")
    
    # Example: Save sample data
    sample_lojas = [
        {
            "store_id": 1,
            "locRef": "99 CB CB",
            "nome_loja": "Loja Lago Sul"
        }
    ]
    
    sample_datas = [
        {
            "bus_dt": "2024-01-01",
            "ano": 2024,
            "mes": 1,
            "dia": 1,
            "dia_da_semana": "Segunda-feira"
        }
    ]
    
    # Save data
    repo.save_dim_lojas(sample_lojas)
    repo.save_dim_datas(sample_datas)
    
    print("Sample data saved successfully!")
    
    # Load and display data
    lojas = repo.load_dim_lojas()
    print(f"\nLoaded lojas data: {lojas}")
    
    # List available files
    files = repo.list_available_files()
    print(f"\nAvailable files: {files}")


if __name__ == "__main__":
    main()
