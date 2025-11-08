# NewRepository - Repository Pattern Implementation

## Overview

`NewRepository` is a Python class that implements the Repository pattern for managing data access in the Coco Bambu data engineering project. It provides a clean abstraction layer between business logic and data storage operations.

## Features

- **Data Lake Integration**: Seamlessly interacts with the data lake directory structure
- **JSON Operations**: Save and load JSON files with built-in error handling
- **Dimension Tables Support**: Dedicated methods for dimension tables (lojas, datas, itens)
- **Fact Table Support**: Methods for managing fact tables (fato_pedidos)
- **Detail Data Management**: Support for detail_lines and detail_metadata
- **Batch Operations**: Load all tables at once with `get_all_tables()`
- **File Listing**: Easily discover available data files

## Installation

No additional dependencies required beyond Python's standard library.

## Usage

### Basic Usage

```python
from new_repository import NewRepository

# Initialize the repository
repo = NewRepository(
    base_path="./data_lake",
    store_id=1,
    bus_dt="2024-01-01"
)

# Save dimension data
lojas_data = [
    {
        "store_id": 1,
        "locRef": "99 CB CB",
        "nome_loja": "Loja Lago Sul"
    }
]
repo.save_dim_lojas(lojas_data)

# Load dimension data
lojas = repo.load_dim_lojas()
print(lojas)
```

### Working with Multiple Tables

```python
# Save multiple dimension tables
repo.save_dim_lojas(lojas_data)
repo.save_dim_datas(datas_data)
repo.save_dim_itens(itens_data)

# Load all tables at once
all_data = repo.get_all_tables()
print(all_data["dim_lojas"])
print(all_data["dim_datas"])
print(all_data["dim_itens"])
```

### Listing Available Files

```python
# List all JSON files in the current data path
files = repo.list_available_files()
print(f"Available files: {files}")
```

### Working with Different Stores and Dates

```python
# Repository for Store 1, Date 2024-01-01
repo1 = NewRepository(base_path="./data_lake", store_id=1, bus_dt="2024-01-01")

# Repository for Store 2, Date 2024-01-02
repo2 = NewRepository(base_path="./data_lake", store_id=2, bus_dt="2024-01-02")

# Each repository manages its own data path
repo1.save_dim_lojas(store1_data)
repo2.save_dim_lojas(store2_data)
```

## API Reference

### Constructor

```python
NewRepository(base_path="./data_lake", store_id=1, bus_dt=None)
```

**Parameters:**
- `base_path` (str): Base path for the data lake directory (default: "./data_lake")
- `store_id` (int): Store identifier (default: 1)
- `bus_dt` (str): Business date in YYYY-MM-DD format (default: current date)

### Save Methods

All save methods return `bool` (True if successful, False otherwise).

- `save_json(filename, data)`: Save generic JSON file
- `save_dim_lojas(data)`: Save store dimension data
- `save_dim_datas(data)`: Save date dimension data
- `save_dim_itens(data)`: Save items dimension data
- `save_fato_pedidos(data)`: Save orders fact table
- `save_detail_lines(data)`: Save detail lines
- `save_detail_metadata(data)`: Save detail metadata

**Parameters:**
- `data` (List[Dict]): List of dictionaries containing the data

### Load Methods

All load methods return `Optional[List[Dict]]` (data if successful, None if error).

- `load_json(filename)`: Load generic JSON file
- `load_dim_lojas()`: Load store dimension data
- `load_dim_datas()`: Load date dimension data
- `load_dim_itens()`: Load items dimension data
- `load_fato_pedidos()`: Load orders fact table
- `load_detail_lines()`: Load detail lines
- `load_detail_metadata()`: Load detail metadata

### Utility Methods

- `get_all_tables()`: Load all tables and return as a dictionary
  - Returns: `Dict[str, Optional[List[Dict]]]`

- `list_available_files()`: List all JSON files in the current data path
  - Returns: `List[str]`

## Data Lake Structure

The repository manages data in the following structure:

```
data_lake/
└── store_id={store_id}/
    └── bus_dt={YYYY-MM-DD}/
        ├── dim_lojas.json
        ├── dim_datas.json
        ├── dim_itens.json
        ├── fato_pedidos.json
        ├── detail_lines.json
        └── detail_metadata.json
```

## Error Handling

The repository includes built-in error handling:
- All save/load operations catch exceptions and return appropriate values
- Error messages are printed to console for debugging
- Missing files return `None` rather than raising exceptions

## Testing

Run the test suite:

```bash
python -m unittest test_new_repository -v
```

## Examples

See the `main()` function in `new_repository.py` for complete examples.

## Integration with Existing Code

The NewRepository can be easily integrated with the existing `ingestao_dados.py`:

```python
from new_repository import NewRepository
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("Desafio Coco Bambu").getOrCreate()

# Initialize repository
repo = NewRepository(base_path="./data_lake", store_id=1, bus_dt="2024-01-01")

# Load data using Spark
df = spark.read.json(repo.data_path + "/dim_lojas.json")
df.show()
```

## License

Part of the Desafio Coco Bambu project.

## Author

Igor Ferrer
