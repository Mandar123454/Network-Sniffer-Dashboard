# Contributing to Network Sniffer Dashboard

Thank you for your interest in contributing to the Network Sniffer Dashboard! We welcome contributions from the community.

## 🤝 Code of Conduct

By participating in this project, you agree to our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

---

## 📋 How to Contribute

### 1. 🐛 Reporting Bugs

Found a bug? Please create an issue with:

- **Clear Title**: Brief description of the bug
- **Reproduction Steps**: How to reproduce the issue
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Screenshots/Logs**: If applicable
- **Environment**: OS, Python version, browser

**Example:**
```
Title: Search filter not working with special characters

Steps to Reproduce:
1. Enter "@" in search box
2. Click Apply Filters
3. Observe results

Expected: Packets containing "@" are filtered
Actual: Filter returns no results
```

### 2. 💡 Suggesting Features

Have an idea? Please create an issue with:

- **Clear Title**: Feature name or summary
- **Description**: Detailed explanation of the feature
- **Motivation**: Why this feature would be useful
- **Examples**: How it would work

**Example:**
```
Title: Add packet payload display

Description: Show first 100 bytes of packet payload

Motivation: Would help identify application-level protocols

Example: Display as hex and ASCII in expandable row
```

### 3. 🔧 Submitting Code

#### Setup Development Environment
```bash
# Clone repository
git clone https://github.com/yourusername/network-sniffer.git
cd network-sniffer

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install flask scapy

# Create a branch
git checkout -b feature/your-feature-name
```

#### Code Style Guidelines

- **Python**: Follow PEP 8
- **JavaScript**: Use consistent indentation (4 spaces)
- **CSS**: Use consistent formatting
- **Naming**: Use descriptive, meaningful names

#### Before Submitting

- ✅ Test your changes thoroughly
- ✅ Add comments for complex logic
- ✅ Update documentation if needed
- ✅ Keep commits atomic and well-described
- ✅ Rebase on main before pushing

#### Pull Request Process

1. **Create Branch**: `git checkout -b feature/your-feature`
2. **Make Changes**: Write clean, commented code
3. **Test Locally**: Ensure everything works
4. **Commit**: `git commit -m "Add: clear description"`
5. **Push**: `git push origin feature/your-feature`
6. **Create PR**: Include title, description, and related issues
7. **Respond to Reviews**: Address feedback promptly

**PR Template:**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Related Issues
Closes #123

## Testing
Describe testing performed

## Screenshots
If UI changes, include screenshots
```

### 4. 📚 Improving Documentation

Documentation improvements are highly valued:

- Update README with clearer instructions
- Add API documentation
- Create tutorials or guides
- Fix typos or grammar issues
- Add examples for features

---

## 📂 Project Structure

```
network-sniffer/
├── app.py                    # Flask app & packet capture
├── templates/                # HTML templates
│   ├── index.html           # Dashboard
│   └── login.html           # Login page
├── static/                   # Frontend assets
│   ├── style.css            # Styling
│   └── script.js            # JavaScript
├── README.md                # Main documentation
├── CONTRIBUTING.md          # This file
├── CODE_OF_CONDUCT.md       # Code of conduct
├── LICENSE                  # MIT License
└── requirements.txt         # Dependencies
```

---

## 🔨 Common Contribution Types

### Bug Fixes
```python
# Before
def capture():
    sniff(prn=process)  # Infinite loop without error handling

# After
def capture():
    try:
        sniff(prn=process)
    except Exception as e:
        logger.error(f"Capture error: {e}")
```

### Feature Additions
```python
@app.route("/export_csv")
@login_required
def export_csv():
    """New feature: Export packets as CSV"""
    # Implementation here
```

### UI Improvements
```css
/* Enhance button styling */
.btn-secondary:hover {
    transform: translateY(-2px);
    box-shadow: enhanced glow;
}
```

---

## ✨ Standards & Best Practices

### Python Code
```python
# Good
def filter_packets(packets, protocol):
    """Filter packets by protocol.
    
    Args:
        packets: List of packet dicts
        protocol: Protocol filter string
        
    Returns:
        Filtered list of packets
    """
    return [p for p in packets if p["proto"] == protocol]

# Avoid
def filter_packets(packets, protocol):
    return [p for p in packets if p["proto"] == protocol]  # No docstring
```

### JavaScript Code
```javascript
// Good
function loadData() {
    // Fetch and process data
    fetch('/data')
        .then(res => res.json())
        .then(data => updateUI(data))
        .catch(err => console.error(err));
}

// Avoid
function loadData(){fetch('/data').then(r=>r.json()).then(d=>updateUI(d))}
```

### Commit Messages
```
Good:
✅ Add: CSV export feature
✅ Fix: Search filter with special characters
✅ Docs: Update installation instructions
✅ Refactor: Simplify packet filtering logic

Avoid:
❌ fixed stuff
❌ WIP
❌ asdf
❌ changed things
```

---

## 🧪 Testing

Before submitting:

### Test the Application
```bash
python app.py
# Navigate to http://localhost:5000
# Test login, filtering, search, pagination, export
```

### Test Different Browsers
- Chrome/Chromium
- Firefox
- Safari
- Edge

### Test on Different OS
- Windows 10/11
- macOS
- Ubuntu/Debian

---

## 🚀 Development Workflow

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Commit** with clear messages
6. **Push** to your fork
7. **Create** a pull request
8. **Address** review feedback
9. **Celebrate** when merged! 🎉

---

## 💬 Communication

- **Issues**: Use for bugs and features
- **Discussions**: Use for questions and ideas
- **Pull Requests**: Use for code changes
- **Email**: For sensitive matters

---

## 🎖️ Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub acknowledgments

---

## ❓ Questions?

- Check existing issues and discussions
- Read the documentation
- Create a new discussion
- Contact the maintainers

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the same MIT License as the project.

---

**Thank you for contributing! Together we make Network Sniffer better. ❤️**
