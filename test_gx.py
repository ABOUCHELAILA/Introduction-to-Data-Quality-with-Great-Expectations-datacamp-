import great_expectations as gx
import pandas as pd

print("=== Minimal Great Expectations Test ===")
print(f"GX Version: {gx.__version__}")

# Create simple data
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
})

print(f"DataFrame:\n{df}")

# Get context
context = gx.get_context()
print(f"Context type: {type(context)}")

# List available methods to see what we can use
print("\nAvailable context methods:")
methods = [method for method in dir(context) if not method.startswith('_')]
print(methods)

print("\nTest completed.")