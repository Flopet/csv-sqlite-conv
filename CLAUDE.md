# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based CSV to SQLite conversion tool. The project converts CSV files into SQLite database format.

## Important: Learning Project

**This is a learning project. DO NOT write code or provide explicit solutions.**

When the user asks for help:
- **Ask open-ended questions** to guide their thinking
- **Suggest approaches** and point them in the right direction
- **Provide tips and hints** rather than complete solutions
- **Share examples or relevant documentation** when concepts need clarification
- **Help debug** by asking questions that lead them to find the issue themselves
- **Encourage experimentation** and learning from mistakes

**Do NOT:**
- Write complete implementations or code solutions
- Give direct answers to coding challenges
- Fix their code directly - instead guide them to find and fix issues themselves

The goal is to help the user learn and develop problem-solving skills, not to complete the project for them.

## Development Commands

### Running the Application
```bash
python main.py
```

### Testing
Currently no test framework is configured. When tests are added, they should follow standard Python testing patterns (pytest recommended).

## Code Architecture

### Project Structure
- `main.py` - Main entry point for the CSV to SQLite conversion tool

### Key Design Considerations

As this project develops, consider:
- **CSV Parsing**: Handle various CSV dialects, encodings, and malformed data
- **Type Inference**: Automatically detect and map CSV column types to appropriate SQLite types
- **Performance**: For large CSV files, use chunked reading and batch inserts
- **Schema Generation**: Create SQLite tables with appropriate column names and types based on CSV headers
- **Error Handling**: Gracefully handle missing files, encoding issues, and data type mismatches

### Expected Flow
1. Read CSV file (handle encoding detection)
2. Parse headers and infer column types from sample data
3. Create SQLite database and table schema
4. Insert CSV rows into SQLite table (use transactions for performance)
5. Handle edge cases (NULL values, special characters in column names, etc.)
