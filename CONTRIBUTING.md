# 🤝 Contributing to Google Dork Generator

Thank you for your interest in contributing to the Google Dork Generator! We welcome contributions from the community and are excited to see how you can help improve this OSINT tool.

## 🌟 Ways to Contribute

### 🐛 **Bug Reports**
- Found a bug? Please open an issue with detailed information
- Include steps to reproduce the problem
- Mention your operating system and Python version
- Provide error messages if any

### 💡 **Feature Requests**
- Have an idea for a new dork type? We'd love to hear it!
- Open an issue with the "enhancement" label
- Describe the use case and expected behavior
- Provide examples of the desired output

### 🔧 **Code Contributions**
We welcome pull requests for:
- **New Dork Types**: Add support for additional search patterns
- **UI Improvements**: Enhance the user interface and experience
- **Bug Fixes**: Resolve existing issues
- **Documentation Updates**: Improve README, comments, or guides
- **Performance Optimizations**: Make the app faster and more efficient

## 🚀 Getting Started

### 1. **Fork the Repository**
- Click the "Fork" button at the top of the repository
- Clone your fork locally:
  ```bash
  git clone https://github.com/your-username/google-dork-generator.git
  cd google-dork-generator
  ```

### 2. **Set Up Development Environment**
- Create a virtual environment:
  ```cmd
  pip install virtualenv
  virtualenv .env
  .env\Scripts\activate
  ```
- Install dependencies:
  ```cmd
  pip install -r requirements.txt
  ```
- Test that everything works:
  ```cmd
  streamlit run main.py
  ```

### 3. **Create a Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

## 🛠️ Development Guidelines

### **Adding New Dork Types**
When adding a new dork type, follow this pattern:

1. **Add Session State Variable**
   ```python
   if 'your_new_dork_result' not in st.session_state:
       st.session_state.your_new_dork_result = None
   ```

2. **Create Formatting Function**
   ```python
   def format_your_dork(input_param):
       """Generate Google dork for your specific use case."""
       formatted_dork = f'your dork pattern here: {input_param}'
       return formatted_dork
   ```

3. **Add UI Section**
   Follow the existing pattern with:
   - Title with relevant emoji
   - Input field
   - Generate button
   - Copy and clear buttons with proper session state management

### **Code Style**
- Follow Python PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and concise
- Add comments for complex logic

### **Testing Your Changes**
- Test all existing functionality still works
- Test your new feature thoroughly
- Try edge cases and invalid inputs
- Ensure the UI remains responsive

## 📝 Pull Request Process

### 1. **Before Submitting**
- Ensure your code follows the project's style guidelines
- Test your changes thoroughly
- Update documentation if needed
- Make sure all existing tests pass

### 2. **Submit Your PR**
- Push your changes to your fork
- Create a pull request with a clear title and description
- Reference any related issues
- Include screenshots for UI changes

### 3. **PR Description Template**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tested locally
- [ ] All existing features work
- [ ] New feature works as expected

## Screenshots (if applicable)
Add screenshots here
```

## 🎯 Priority Areas

We're particularly interested in contributions for:

1. **New Dork Types**
   - Email search patterns
   - Social security numbers (various countries)
   - License plate formats
   - Financial data (credit cards, bank accounts)
   - Educational records

2. **UI/UX Improvements**
   - Better mobile responsiveness
   - Dark mode support
   - Export functionality (save dorks to file)
   - History of generated dorks

3. **Advanced Features**
   - Batch processing multiple inputs
   - Custom dork templates
   - Integration with search APIs
   - Results validation

## 🔍 Code Review Process

1. **Automated Checks**: Your PR will be checked for basic formatting
2. **Manual Review**: A maintainer will review your changes
3. **Feedback**: You may receive suggestions for improvements
4. **Approval**: Once approved, your changes will be merged

## 📞 Getting Help

- **Questions**: Open a discussion or issue
- **Chat**: Mention @juansilvadesign in issues
- **Documentation**: Check the README.md for setup help
- **Security Issues**: See our [SECURITY.md](SECURITY.md) for vulnerability reporting

## 🏆 Recognition

Contributors will be recognized in the project! Regular contributors may be invited to become maintainers.

## 📜 Code of Conduct

### Our Standards
- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn and contribute
- Maintain a professional and welcoming environment

### Not Acceptable
- Harassment or discriminatory language
- Malicious or unethical use suggestions
- Spam or off-topic discussions

## 🎉 Thank You!

Every contribution, no matter how small, helps make this tool better for the OSINT community. Thank you for taking the time to contribute!

---

**Happy Contributing! 🚀✨**