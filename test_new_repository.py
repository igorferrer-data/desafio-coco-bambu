"""
Test Suite for NewRepository Module
====================================

This module contains unit tests for the NewRepository class.
"""

import unittest
import os
import json
import tempfile
import shutil
from new_repository import NewRepository


class TestNewRepository(unittest.TestCase):
    """Test cases for NewRepository class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.repo = NewRepository(
            base_path=self.test_dir,
            store_id=1,
            bus_dt="2024-01-01"
        )
        
        # Sample test data
        self.sample_lojas = [
            {
                "store_id": 1,
                "locRef": "99 CB CB",
                "nome_loja": "Loja Lago Sul"
            }
        ]
        
        self.sample_datas = [
            {
                "bus_dt": "2024-01-01",
                "ano": 2024,
                "mes": 1,
                "dia": 1,
                "dia_da_semana": "Segunda-feira"
            }
        ]
        
        self.sample_itens = [
            {
                "menuItemId": 101,
                "nome_item": "Camarão Internacional",
                "categoria": "Prato Principal",
                "preco": 45.50
            }
        ]
    
    def tearDown(self):
        """Clean up test fixtures after each test method."""
        # Remove the temporary directory
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_initialization(self):
        """Test NewRepository initialization."""
        self.assertEqual(self.repo.base_path, self.test_dir)
        self.assertEqual(self.repo.store_id, 1)
        self.assertEqual(self.repo.bus_dt, "2024-01-01")
    
    def test_path_creation(self):
        """Test that data path is created correctly."""
        self.repo._ensure_path_exists()
        self.assertTrue(os.path.exists(self.repo.data_path))
    
    def test_save_and_load_json(self):
        """Test saving and loading JSON files."""
        # Save data
        result = self.repo.save_json("test.json", self.sample_lojas)
        self.assertTrue(result)
        
        # Verify file exists
        filepath = os.path.join(self.repo.data_path, "test.json")
        self.assertTrue(os.path.exists(filepath))
        
        # Load data
        loaded_data = self.repo.load_json("test.json")
        self.assertIsNotNone(loaded_data)
        self.assertEqual(loaded_data, self.sample_lojas)
    
    def test_save_dim_lojas(self):
        """Test saving store dimension data."""
        result = self.repo.save_dim_lojas(self.sample_lojas)
        self.assertTrue(result)
        
        # Verify file exists
        filepath = os.path.join(self.repo.data_path, "dim_lojas.json")
        self.assertTrue(os.path.exists(filepath))
    
    def test_save_dim_datas(self):
        """Test saving date dimension data."""
        result = self.repo.save_dim_datas(self.sample_datas)
        self.assertTrue(result)
        
        # Verify file exists
        filepath = os.path.join(self.repo.data_path, "dim_datas.json")
        self.assertTrue(os.path.exists(filepath))
    
    def test_save_dim_itens(self):
        """Test saving items dimension data."""
        result = self.repo.save_dim_itens(self.sample_itens)
        self.assertTrue(result)
        
        # Verify file exists
        filepath = os.path.join(self.repo.data_path, "dim_itens.json")
        self.assertTrue(os.path.exists(filepath))
    
    def test_load_dim_lojas(self):
        """Test loading store dimension data."""
        # First save some data
        self.repo.save_dim_lojas(self.sample_lojas)
        
        # Then load it
        loaded_data = self.repo.load_dim_lojas()
        self.assertIsNotNone(loaded_data)
        self.assertEqual(loaded_data, self.sample_lojas)
    
    def test_load_dim_datas(self):
        """Test loading date dimension data."""
        # First save some data
        self.repo.save_dim_datas(self.sample_datas)
        
        # Then load it
        loaded_data = self.repo.load_dim_datas()
        self.assertIsNotNone(loaded_data)
        self.assertEqual(loaded_data, self.sample_datas)
    
    def test_load_dim_itens(self):
        """Test loading items dimension data."""
        # First save some data
        self.repo.save_dim_itens(self.sample_itens)
        
        # Then load it
        loaded_data = self.repo.load_dim_itens()
        self.assertIsNotNone(loaded_data)
        self.assertEqual(loaded_data, self.sample_itens)
    
    def test_load_nonexistent_file(self):
        """Test loading a file that doesn't exist."""
        loaded_data = self.repo.load_json("nonexistent.json")
        self.assertIsNone(loaded_data)
    
    def test_get_all_tables(self):
        """Test retrieving all tables."""
        # Save some data first
        self.repo.save_dim_lojas(self.sample_lojas)
        self.repo.save_dim_datas(self.sample_datas)
        self.repo.save_dim_itens(self.sample_itens)
        
        # Get all tables
        all_tables = self.repo.get_all_tables()
        
        # Verify structure
        self.assertIsInstance(all_tables, dict)
        self.assertIn("dim_lojas", all_tables)
        self.assertIn("dim_datas", all_tables)
        self.assertIn("dim_itens", all_tables)
        
        # Verify loaded data
        self.assertEqual(all_tables["dim_lojas"], self.sample_lojas)
        self.assertEqual(all_tables["dim_datas"], self.sample_datas)
        self.assertEqual(all_tables["dim_itens"], self.sample_itens)
    
    def test_list_available_files(self):
        """Test listing available JSON files."""
        # Initially no files
        files = self.repo.list_available_files()
        self.assertEqual(files, [])
        
        # Save some data
        self.repo.save_dim_lojas(self.sample_lojas)
        self.repo.save_dim_datas(self.sample_datas)
        
        # List files
        files = self.repo.list_available_files()
        self.assertEqual(len(files), 2)
        self.assertIn("dim_lojas.json", files)
        self.assertIn("dim_datas.json", files)
    
    def test_list_files_empty_directory(self):
        """Test listing files when directory doesn't exist."""
        # Create a repo with a different path that doesn't exist
        repo = NewRepository(
            base_path=self.test_dir,
            store_id=999,
            bus_dt="2099-12-31"
        )
        
        files = repo.list_available_files()
        self.assertEqual(files, [])


class TestNewRepositoryIntegration(unittest.TestCase):
    """Integration tests for NewRepository class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_multiple_stores_and_dates(self):
        """Test handling multiple stores and dates."""
        # Create repositories for different stores and dates
        repo1 = NewRepository(self.test_dir, store_id=1, bus_dt="2024-01-01")
        repo2 = NewRepository(self.test_dir, store_id=2, bus_dt="2024-01-01")
        repo3 = NewRepository(self.test_dir, store_id=1, bus_dt="2024-01-02")
        
        # Save data to each
        data1 = [{"store_id": 1, "nome_loja": "Loja 1"}]
        data2 = [{"store_id": 2, "nome_loja": "Loja 2"}]
        data3 = [{"store_id": 1, "nome_loja": "Loja 1 - Dia 2"}]
        
        repo1.save_dim_lojas(data1)
        repo2.save_dim_lojas(data2)
        repo3.save_dim_lojas(data3)
        
        # Verify each repository loads its own data
        self.assertEqual(repo1.load_dim_lojas(), data1)
        self.assertEqual(repo2.load_dim_lojas(), data2)
        self.assertEqual(repo3.load_dim_lojas(), data3)
    
    def test_full_data_workflow(self):
        """Test a complete data workflow."""
        repo = NewRepository(self.test_dir, store_id=1, bus_dt="2024-01-01")
        
        # Prepare complete dataset
        lojas = [{"store_id": 1, "locRef": "99 CB CB", "nome_loja": "Loja Lago Sul"}]
        datas = [{"bus_dt": "2024-01-01", "ano": 2024, "mes": 1, "dia": 1}]
        itens = [{"menuItemId": 101, "nome_item": "Camarão", "preco": 45.50}]
        pedidos = [{"guestCheckId": 1122334455, "store_id": 1, "chkTtl": 45.50}]
        details = [{"lineItemId": 1, "guestCheckId": 1122334455, "dspQty": 1}]
        metadata = [{"metadataId": 1, "lineItemId": 1, "metadataType": "info"}]
        
        # Save all data
        self.assertTrue(repo.save_dim_lojas(lojas))
        self.assertTrue(repo.save_dim_datas(datas))
        self.assertTrue(repo.save_dim_itens(itens))
        self.assertTrue(repo.save_fato_pedidos(pedidos))
        self.assertTrue(repo.save_detail_lines(details))
        self.assertTrue(repo.save_detail_metadata(metadata))
        
        # Verify all files exist
        files = repo.list_available_files()
        self.assertEqual(len(files), 6)
        
        # Load all data
        all_tables = repo.get_all_tables()
        self.assertEqual(all_tables["dim_lojas"], lojas)
        self.assertEqual(all_tables["dim_datas"], datas)
        self.assertEqual(all_tables["dim_itens"], itens)
        self.assertEqual(all_tables["fato_pedidos"], pedidos)
        self.assertEqual(all_tables["detail_lines"], details)
        self.assertEqual(all_tables["detail_metadata"], metadata)


if __name__ == '__main__':
    unittest.main()
