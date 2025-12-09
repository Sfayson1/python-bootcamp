# week1/day2_async.py
"""
Day 2: Async/Await Mastery

Goal: Understand asynchronous programming and why async matters.

Key Concepts:
- asyncio event loop
- async/await syntax
- Concurrent vs. parallel execution
- When to use async (I/O bound, not CPU bound)
- Performance comparison: sync vs. async
"""

import asyncio
import time
from typing import List


# ============= PART 1: SYNCHRONOUS (BLOCKING) =============

def fetch_data_sync(url: str, delay: float = 2) -> str:
    """
    Simulates a synchronous network request that blocks.

    In real life: API calls, database queries, file reads
    Here: we use time.sleep() to simulate the network delay
    """
    print(f"[SYNC] Starting fetch from {url}")
    time.sleep(delay)  # Blocks everything!
    print(f"[SYNC] Completed fetch from {url}")
    return f"Data from {url}"


def main_sync():
    """
    Synchronous approach: fetch 5 URLs one at a time

    Total time = 2s + 2s + 2s + 2s + 2s = 10 seconds (SLOW!)
    """
    print("\n" + "="*60)
    print("SYNCHRONOUS (Blocking) - Fetch 5 URLs sequentially")
    print("="*60)

    start = time.time()

    # TODO: Fetch 5 URLs and collect results
    results = []
    for i in range(1, 6):
        result = fetch_data_sync(f"http://api{i}.com")
        results.append(result)

    elapsed = time.time() - start

    print(f"\nResults: {results}")
    print(f"⏱️  Total time (SYNC): {elapsed:.2f} seconds")
    print("❌ This is SLOW because we wait for each request to complete before starting the next one")

    return elapsed


# ============= PART 2: ASYNCHRONOUS (CONCURRENT) =============

async def fetch_data_async(url: str, delay: float = 2) -> str:
    """
    Simulates an asynchronous network request that doesn't block.

    Key difference: uses 'await asyncio.sleep()' instead of 'time.sleep()'
    This allows OTHER tasks to run while we wait.
    """
    print(f"[ASYNC] Starting fetch from {url}")
    await asyncio.sleep(delay)  # Doesn't block! Other tasks can run
    print(f"[ASYNC] Completed fetch from {url}")
    return f"Data from {url}"


async def main_async():
    """
    Asynchronous approach: fetch 5 URLs concurrently

    Total time ≈ 2 seconds (FAST!)
    Why? All 5 requests start at the same time and run concurrently
    """
    print("\n" + "="*60)
    print("ASYNCHRONOUS (Concurrent) - Fetch 5 URLs concurrently")
    print("="*60)

    start = time.time()

    # TODO: Create 5 async tasks and run them concurrently
    # Use asyncio.gather() to run multiple coroutines at the same time
    tasks = [
        fetch_data_async(f"http://api{i}.com")
        for i in range(1, 6)
    ]

    results = await asyncio.gather(*tasks)

    elapsed = time.time() - start

    print(f"\nResults: {results}")
    print(f"⏱️  Total time (ASYNC): {elapsed:.2f} seconds")
    print("✅ This is FAST because all requests run concurrently!")

    return elapsed


# ============= PART 3: COMPARISON =============

def compare_performance():
    """
    Run both sync and async versions and compare performance
    """
    print("\n\n" + "="*60)
    print("PERFORMANCE COMPARISON")
    print("="*60)

    # Run sync version
    sync_time = main_sync()

    # Run async version
    async_time = asyncio.run(main_async())

    # Calculate speedup
    speedup = sync_time / async_time

    print(f"\n" + "="*60)
    print("RESULTS:")
    print(f"  Synchronous time: {sync_time:.2f}s")
    print(f"  Asynchronous time: {async_time:.2f}s")
    print(f"  Speedup: {speedup:.1f}x faster with async!")
    print("="*60)


# ============= PART 4: ADVANCED ASYNC =============

async def fetch_with_timeout(url: str, timeout: float = 3) -> str:
    """
    Fetch with a timeout - if it takes too long, raise an error
    """
    try:
        result = await asyncio.wait_for(
            fetch_data_async(url, delay=2),
            timeout=timeout
        )
        return result
    except asyncio.TimeoutError:
        return f"TIMEOUT: {url} took too long"


async def fetch_with_retry(url: str, max_retries: int = 3) -> str:
    """
    Fetch with retry logic - if it fails, try again
    """
    for attempt in range(1, max_retries + 1):
        try:
            print(f"[RETRY] Attempt {attempt}/{max_retries} for {url}")
            # Simulate random failures (in real life, this would be network errors)
            await asyncio.sleep(0.5)
            if attempt < 2:  # Fail first attempt, succeed on retry
                raise Exception("Simulated network error")
            return f"Success on attempt {attempt}: {url}"
        except Exception as e:
            if attempt == max_retries:
                return f"FAILED after {max_retries} attempts: {url}"
            await asyncio.sleep(1)  # Wait before retrying


async def advanced_examples():
    """
    Demonstrate advanced async patterns
    """
    print("\n" + "="*60)
    print("ADVANCED ASYNC PATTERNS")
    print("="*60)

    # Example 1: Timeout
    print("\n1. Fetching with timeout (3 seconds):")
    result = await fetch_with_timeout("http://api-slow.com", timeout=3)
    print(f"   Result: {result}")

    # Example 2: Retry logic
    print("\n2. Fetching with retry (3 attempts):")
    result = await fetch_with_retry("http://api-flaky.com", max_retries=3)
    print(f"   Result: {result}")

    # Example 3: Multiple operations with different delays
    print("\n3. Fetching multiple URLs with different delays:")

    async def fetch_variable(url: str, delay: float) -> str:
        await asyncio.sleep(delay)
        return f"{url} (waited {delay}s)"

    results = await asyncio.gather(
        fetch_variable("http://api1.com", 1),
        fetch_variable("http://api2.com", 2),
        fetch_variable("http://api3.com", 0.5),
    )
    for result in results:
        print(f"   {result}")


# ============= PART 5: TESTS =============

async def test_async_execution():
    """
    Test that async functions actually run concurrently
    """
    print("\n" + "="*60)
    print("TEST: Verify concurrent execution")
    print("="*60)

    start = time.time()

    # Run 3 tasks that each take 2 seconds
    results = await asyncio.gather(
        fetch_data_async("http://test1.com", delay=2),
        fetch_data_async("http://test2.com", delay=2),
        fetch_data_async("http://test3.com", delay=2),
    )

    elapsed = time.time() - start

    # If truly concurrent, should take ~2 seconds (not 6)
    assert elapsed < 3, f"Tasks didn't run concurrently! Took {elapsed:.2f}s instead of ~2s"
    assert len(results) == 3

    print(f"✅ PASSED: Tasks ran concurrently in {elapsed:.2f}s")
    print(f"✅ PASSED: Got {len(results)} results")


# ============= MAIN =============

if __name__ == "__main__":
    print("\n" + "="*60)
    print("DAY 2: ASYNC/AWAIT MASTERY")
    print("="*60)

    # Run performance comparison
    compare_performance()

    # Run advanced examples
    asyncio.run(advanced_examples())

    # Run tests
    asyncio.run(test_async_execution())

    print("\n" + "="*60)
    print("KEY TAKEAWAYS:")
    print("="*60)
    print("""
1. SYNC (blocking):
   - Tasks run one at a time
   - Total time = sum of all tasks
   - Simple but SLOW for I/O operations

2. ASYNC (concurrent):
   - Tasks run at the same time
   - Total time = longest single task
   - FAST for I/O operations
   - Uses asyncio event loop

3. WHEN TO USE ASYNC:
   ✅ I/O operations (network, file, database)
   ✅ Multiple operations that can run in parallel
   ❌ NOT CPU-intensive work (use multiprocessing instead)

4. KEY FUNCTIONS:
   - async def: define async function
   - await: pause until operation completes
   - asyncio.gather(): run multiple coroutines concurrently
   - asyncio.wait_for(): add timeout
   - asyncio.run(): run async function from sync code

5. REAL-WORLD EXAMPLES:
   - Fetching data from multiple APIs
   - Database queries in parallel
   - WebSocket connections
   - File I/O operations
   - Web scraping
    """)
    print("="*60)
