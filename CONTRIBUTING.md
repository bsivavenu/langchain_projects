# Contributing to LangChain Projects

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this repository.

## Code of Conduct

Please be respectful and constructive in all interactions. We aim to maintain a welcoming and inclusive community.

## Getting Started

1. **Fork the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/langchain_projects.git
   cd langchain_projects
   ```

2. **Set Up Development Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv sync  # or: pip install -r requirements.txt
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

### Code Style
- Follow PEP 8 conventions
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Refactor, etc.)
- Example: `Add document loader for invoice extraction`

### Testing
- Test your changes locally before submitting
- Ensure all notebooks run without errors
- For Streamlit apps, test the UI functionality

### Documentation
- Update README files if adding new features
- Add docstrings to new functions
- Include usage examples for new tools

## Types of Contributions

### 1. New Features/Tools
- Create a new folder for your tool/application
- Include a `README.md` with documentation
- Add `.env.example` for required environment variables
- Update main `README.md` to reference your addition

### 2. Educational Content (Notebooks)
- Create clear, well-commented notebooks
- Include practical examples and explanations
- Follow the naming convention: `Topic_Description.ipynb`

### 3. Bug Fixes
- Describe the bug in your PR
- Include steps to reproduce
- Show how your fix resolves the issue

### 4. Improvements
- Refactoring for better performance
- Improving documentation
- Updating dependencies
- Enhancing user experience

## Pull Request Process

1. **Before Submitting**
   - Ensure your code works locally
   - Update documentation if needed
   - Run a final check on your changes

2. **Submit PR**
   - Create a pull request to the `main` branch
   - Use a descriptive title
   - Reference any related issues
   - Provide a clear description of your changes

3. **PR Template**
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] New feature
   - [ ] Bug fix
   - [ ] Documentation update
   - [ ] Improvement

   ## How to Test
   Steps to verify the changes

   ## Related Issues
   Closes #(issue number)
   ```

4. **Review Process**
   - Maintainers will review your PR
   - Be responsive to feedback
   - Make requested changes in new commits

## Project Structure Guidelines

When adding a new project/application:

```
your_new_tool/
├── README.md                 # Project documentation
├── .env.example             # Example environment variables
├── app.py                   # Main application file
├── requirements.txt         # Project dependencies
├── pages/                   # (for Streamlit apps)
│   └── page1.py
└── data/                    # (for sample data)
    └── sample.csv
```

## Environment Variables

- Never commit `.env` files
- Use `.env.example` with placeholder values
- Document required API keys in README

## Dependencies

- Update `requirements.txt` if adding new packages
- Keep dependencies up-to-date and minimal
- Prefer official LangChain integrations

## Documentation Standards

### For Notebooks
- Add descriptive cell comments
- Include output examples
- Explain key concepts

### For Scripts/Apps
- Add module docstrings
- Document function parameters
- Include usage examples

### For README Files
- Clear, concise descriptions
- Setup instructions
- Example usage
- Required API keys

## Running Lint and Format Checks

```bash
# Format code (optional, for consistency)
black *.py

# Check code style
flake8 *.py
```

## Common Issues

### Issue: ImportError for langchain modules
**Solution**: Ensure you've installed all dependencies
```bash
pip install -r requirements.txt
```

### Issue: API Key errors
**Solution**: Check that `.env` file is properly configured
```bash
cp .env.example .env
# Edit .env with your actual API keys
```

### Issue: Notebook kernel errors
**Solution**: Restart kernel and run cells in order
```bash
# In Jupyter: Kernel > Restart & Run All
```

## Getting Help

- Check existing issues and discussions
- Review documentation in README files
- Look at similar implementations for examples
- Open an issue with detailed description

## Licensing

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- README acknowledgments
- Commit history
- GitHub contributors page

---

Thank you for contributing to make this project better! 🎉

For questions, feel free to open an issue or discussion.
