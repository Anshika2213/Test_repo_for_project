# Sample Bug Repo

Small demo repo for testing StateLock's automated program repair pipeline.

## The bug
`calculate_average([])` and `divide(10, 0)` currently raise `ZeroDivisionError`
instead of returning `0.0`.

## Expected fix
Both functions should return `0.0` when the denominator would be zero,
instead of crashing.

## Run tests
    pip install -r requirements.txt
    pytest
