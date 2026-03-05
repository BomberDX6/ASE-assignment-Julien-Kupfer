# Testing Strategy for Quick-Calc

## Overview
My testing strategy focuses on ensuring the mathematical reliability of the core functions, followed by verifying that sequential operations flow correctly. I extensively tested the basic arithmetic operations and mathematical edge cases. Because this is a backend logic implementation, I intentionally did not test graphical user interfaces (GUI) or performance under extreme system load.

## testing methods Applied : Testing pyramid, B-box & W-box testing, regression tests


## Test Results Summary

| Test Name | Type | Status |
| :--- | :--- | :--- |
| `test_addition` | Unit | Pass |
| `test_subtraction` | Unit | Pass |
| `test_multiplication` | Unit | Pass |
| `test_division` | Unit | Pass |
| `test_division_by_zero` | Unit | Pass |
| `test_addition_with_negatives` | Unit | Pass |
| `test_multiplication_with_floats` | Unit | Pass |
| `test_large_numbers_subtraction` | Unit | Pass |
| `test_integration_full_calculation_flow` | Integration | Pass |
| `test_integration_clear_after_calculation` | Integration | Pass |