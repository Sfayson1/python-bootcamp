# Week 1: Python Fundamentals (Professional Grade)

## Goals
- Master type hints and dataclasses
- Learn async/await in Python
- Implement proper error handling and logging
- Write tests with pytest
- Understand project structure and packaging

## Daily Breakdown

### Day 1: Type Hints + Dataclasses + Pydantic ✅
**Status:** COMPLETE

**What you learned:**
- Type hints (str, int, List, Dict, Optional, Union)
- Dataclasses for clean data structures
- Pydantic for validation and serialization
- Custom validators with field_validator

**Deliverable:** `day1_types.py`
- User, Product, Order dataclasses
- Corresponding Pydantic models with validation
- Conversion functions (dataclass ← Pydantic)
- Test cases showing success and error handling

**Run:** `python day1_types.py`

### Day 2: Async/Await Mastery ✅
**Status:** COMPLETE

**What you learned:**
- asyncio basics and event loop
- async/await syntax
- Concurrent vs. parallel execution
- When to use async (I/O bound operations)
- Performance comparison: 5x speedup with async!

**Deliverable:** `day2_async.py`
- Synchronous vs. asynchronous comparison
- Concurrent API calls using asyncio.gather()
- Performance measurement (10s sync vs 2s async)
- Advanced patterns (timeouts, retries)
- Tests for async code

**Key Results:**
- Synchronous: 10.02 seconds (blocking)
- Asynchronous: 2.00 seconds (concurrent)
- **Speedup: 5.0x faster!**

**Run:** `python day2_async.py`

### Day 3: Error Handling + Logging (In Progress)
**What you'll learn:**
- Exception handling (try/except/finally)
- Custom exceptions
- Logging best practices
- Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Context managers (__enter__/__exit__)

**Deliverable:** `day3_errors.py`
- User validation with proper error handling
- Database operations with exception catching
- API calls with error recovery
- Resource cleanup with context managers
- Structured logging throughout

### Day 4: Testing (pytest)
**What you'll learn:**
- pytest fundamentals
- Writing assertions
- Fixtures (setup/teardown)
- Mocking
- Code coverage

**Deliverable:** `test_app.py` with 90%+ coverage

### Day 5: Packaging + Project Structure
**What you'll learn:**
- Proper project layout (src/ structure)
- __init__.py and imports
- pyproject.toml
- Virtual environments
- How to install and distribute packages

**Deliverable:** Reorganized project with proper structure

## Setup

### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Tests
```bash
pytest --cov=. tests/
```

## Project Structure
```
week1/
├── venv/                    # Virtual environment
├── day1_types.py           # Day 1: Types + Dataclasses ✅
├── day2_async.py           # Day 2: Async/Await ✅
├── day3_errors.py          # Day 3: Error handling ⏳
├── test_app.py             # Day 4: Tests ⏳
├── requirements.txt        # Dependencies
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

## Key Concepts

### Type Hints
```python
from typing import List, Optional

def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age}"

users: List[str] = ["Alice", "Bob"]
maybe_user: Optional[str] = None
```

### Dataclasses
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int
```

### Pydantic Validation
```python
from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    name: str
    age: int
    
    @field_validator('age')
    @classmethod
    def age_positive(cls, v):
        if v <= 0:
            raise ValueError('Age must be positive')
        return v
```

### Async/Await
```python
import asyncio

async def fetch_data(url: str) -> str:
    await asyncio.sleep(2)  # Simulates I/O
    return f"Data from {url}"

async def main():
    results = await asyncio.gather(
        fetch_data("http://api1.com"),
        fetch_data("http://api2.com"),
    )
    return results

asyncio.run(main())
```

### Error Handling
```python
try:
    result = risky_operation()
except ValueError as e:
    logger.error(f"Validation failed: {e}")
except Exception as e:
    logger.critical(f"Unexpected error: {e}", exc_info=True)
finally:
    cleanup()
```

## Resources

- [Real Python: Type Checking](https://realpython.com/python-type-checking/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Real Python: Asyncio](https://realpython.com/async-io-python/)
- [pytest Docs](https://docs.pytest.org/)
- [Python Logging](https://docs.python.org/3/library/logging.html)

## Time Tracking

| Day | Focus | Hours | Status |
|-----|-------|-------|--------|
| 1 | Type Hints + Dataclasses | 2h | ✅ Complete |
| 2 | Async/Await | 2h | ✅ Complete |
| 3 | Error Handling + Logging | 2h | ⏳ In Progress |
| 4 | Testing (pytest) | 3h | ⏳ Pending |
| 5 | Packaging + Structure | 2h | ⏳ Pending |
| **Total** | **Python Fundamentals** | **11h** | |

## Next Steps
- Day 3: Start `day3_errors.py`
- Focus on logging, custom exceptions, and error recovery
- Understand context managers

---

*Last updated: Dec 8, 2025*
